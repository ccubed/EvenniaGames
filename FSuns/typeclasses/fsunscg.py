"""
typeclasses/fsunscg.py

File to hold the menu for the fading suns cg system.

Nodes have a labeling scheme:
menunode_x

Where X is:
    start - first node
    lifepath - First node in the lifepath CG
    custom - First node in the custom CG
    lpnX# - This indicates LifePath node step # in archetype X (IE: lpn2 is lifepath noble step 2)
    lpnq# - This indicates a questing knight deviation because they're annoying
    c# - This is step # in the custom CG path

"""

from evennia.utils import evmenu
from evennia.utils.evmenu import get_input
from evennia import Command

"""

Begin helper section. This section is nothing but helper variables and dictionaries for parsing user input in the menus.

"""
# Parses the input on noble house from the keys into the name.
househelper = {'0': 'Hawkwood', '1': 'Decados', '2': 'Hazat', '3': 'Li Halan', '4': 'al-Malik', '5': 'Questing Knight'}


# Applies bonuses for paths and stages per house for nobles
# This is huge and there are four of them but it beats having them in the middle of the menus.
def apply_path_noble(stage, which, house, pc):
    if stage == 0:
        # Upbringing
        if which == 0:
            # high court
            if house == 'Hawkwood':
                pc.db.attributes['Strength'] = 1
                pc.db.attributes['Dexterity'] = 1
                pc.db.attributes['Wits'] = 1
                pc.db.attributes['Extrovert'] = 2
                pc.db.skills['Melee'] = 1
                pc.db.skills['Etiquette'] = 1
                pc.db.skills['Lore'] = {'Heraldry': 1}
                pc.db.languages['Urthish'] = 3
                pc.db.blessings.append('Unyielding')
                pc.db.curses.append('Prideful')
            elif house == 'Decados':
                pc.db.attributes['Dexterity'] = 1
                pc.db.attributes['Perception'] = 2
                pc.db.attributes['Ego'] = 2
                pc.db.skills['Inquiry'] = 1
                pc.db.skills['Etiquette'] = 1
                pc.db.choices.append('Rival House')
                pc.db.languages['Urthish'] = 3
                pc.db.blessings.append('Suspicious')
                pc.db.curses.append('Vain')
            elif house == 'Hazat':
                pc.db.attributes['Endurance'] = 1
                pc.db.attributes['Perception'] = 2
                pc.db.attributes['Passion'] = 2
                pc.db.skills['Impress'] = 1
                pc.db.skills['Melee'] = 1
                pc.db.skills['Etiquette'] = 1
                pc.db.languages['Urthish'] = 3
                pc.db.blessings.append('Disciplined')
                pc.db.curses.append('Vengeful')
            elif house == "Li Halan":
                pc.db.attributes['Wits'] = 1
                pc.db.choices.append("ExIn")
                pc.db.choices.append("PasCalm")
                pc.db.attributes['Faith'] = 2
                pc.db.skills['Focus'] = 1
                pc.db.skills['Etiquette'] = 1
                pc.db.skills['Lore'] = {'Theology': 1}
                pc.db.languages['Latin'] = 1
                pc.db.languages['Urthish'] = 3
                pc.db.blessings.append('Pious')
                pc.db.curses.append('Guilty')
            else:
                pc.db.attributes['Dexterity'] = 1
                pc.db.attributes['Wits'] = 1
                pc.db.choices.append("ExIn")
                pc.db.attributes['Calm'] = 2
                pc.db.skills['Etiquette'] = 1
                pc.db.languages['Graceful Tongue'] = 3
                pc.db.languages['Urthish'] = 3
                pc.db.blessings.append('Gracious')
                pc.db.curses.append('Impetuous')


def menunode_start(caller):
    text = "Beginning Fading Suns Character Generation. You will be able to execute other commands.\n"
    text += "You can exit early but will have to start over. Select your character's path."
    options = ({"desc": "Lifepath CG", "goto": "menunode_lifepath"}, {"desc": "Custom CG", "goto": "menunode_custom"})
    return text, options


def menumode_lifepath(caller):
    text = "Lifepath CG Beginning. This CG module uses the Lifepaths as described in Revised.\n"
    text += "Please begin by selecting an archetype."
    options = ({"desc": "Nobles", "goto": "menunode_lpn1"}, {"desc": "Priests", "goto": "menunode_lpp1"},
               {"desc": "Merchants", "goto": "menunode_lpm1"}, {"desc": "Aliens", "goto": "menumode_lpa1"})
    return text, options


def menumode_lpn1(caller):
    caller.db.archetype = "Noble"
    caller.db.recbenefices = ('Nobility', 'Riches')
    text = "As nobility, your first step is picking a house. Please pick one.\n"
    text += "If you are looking for minor house, please use custom CG."
    options = ({"key": "0", "desc": "Hawkwood", "goto": "menunode_lpn2"},
               {"key": "1", "desc": "Decados", "goto": "menumode_lpn2"},
               {"key": "2", "desc": "Hazat", "goto": "menumode_lpn2"},
               {"key": "3", "desc": "Li Halan", "goto": "menumode_lpn2"},
               {"key": "4", "desc": "al-Malik", "goto": "menumode_lpn2"},
               {"key": "5", "desc": "Questing Knight", "goto": "menumode_lpn2"})


def menumode_lpn2(caller, raw_input):
    if raw_input == 5 and caller.db.house == 'None':
        text = "You selected questing knight. Please select your noble house."
        options = ({"key": "0", "desc": "Hawkwood", "goto": "menunode_lpnq"},
               {"key": "1", "desc": "Decados", "goto": "menumode_lpnq"},
               {"key": "2", "desc": "Hazat", "goto": "menumode_lpnq"},
               {"key": "3", "desc": "Li Halan", "goto": "menumode_lpnq"},
               {"key": "4", "desc": "al-Malik", "goto": "menumode_lpnq"})
        return text, options

    if raw_input == 3:
        caller.db.recbenefices.append('Church Ally')
    elif raw_input == 4:
        caller.db.recbenefices.append('Passage Contract')

    caller.db.house = househelper[raw_input]

    text = "At this point you select your upbringing. Depending on your house you will gain various bonuses."
    options = ({"key": "0", "desc": "High Court", "goto": "menunode_lpn3"},
               {"key": "1", "desc": "Rural Estate", "goto": "menunode_lpn3"},
               {"key": "2", "desc": "Landless", "goto": "menunode_lpn3"})
    return text, options


def menunode_lpnq(caller, raw_input):
    caller.db.house = househelper[raw_input]

    if raw_input == 3:
        caller.db.recbenefices.append('Church Ally')
    elif raw_input == 4:
        caller.db.recbenefices.append('Passage Contract')

    text = "At this point you select your upbringing. Depending on your house you will gain various bonuses."
    options = ({"key": "0", "desc": "High Court", "goto": "menunode_lpn3"},
               {"key": "1", "desc": "Rural Estate", "goto": "menunode_lpn3"},
               {"key": "2", "desc": "Landless", "goto": "menunode_lpn3"})
    return text, options


def menunode_lpn3(caller, raw_input):

    apply_path_noble(0, raw_input, caller.db.house, caller)

    text = "At this stage you pick an apprenticeship under another noble.\n"
    text += "However, nobles also have the option of switching to any of the other archetypes as well.\n"
    text += "Please make your choice now as to stick with the noble archetype or switch to another."


    def merchants(caller):
        caller.db.archetype = "Priest"


    def priests(caller):
        caller.db.archetype = "Merchant"


    options = ({"key": "0", "desc": "Stay a Noble", "goto": "menunode_lpn4"},
               {"key": "1", "desc": "Move to Priests", "goto": "menunode_lppn3"},
               {"key": "2", "desc": "Move to Merchants", "goto": "menunode_lpmn3"})
    return text, options


def menunode_lpn4(caller):
    text = "Please select your noble apprenticeship."
    options = ({"key": "0", "desc": "Soldier", "goto": "menunode_lpn5"},
               {"key": "1", "desc": "Starman", "goto": "menumode_lpn"})