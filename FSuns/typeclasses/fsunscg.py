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
from world import fsutils

"""

Begin helper section. This section is nothing but helper variables and dictionaries for parsing user input in the menus.

"""
# Parses the input on noble house from the keys into the name.
househelper = {'0': 'Hawkwood', '1': 'Decados', '2': 'Hazat', '3': 'Li Halan', '4': 'al-Malik', '5': 'Questing Knight'}


# Applies bonuses for paths and stages per house for nobles
def apply_path_noble(stage, which, house, pc):
    # Upbringing
    if stage == 0:

        # High Court
        if which == 0:

            if house == 'Hawkwood':
                pc.db.attributes['Strength'] = 1
                pc.db.attributes['Dexterity'] = 1
                pc.db.attributes['Wits'] = 1
                pc.db.attributes['Extrovert'] = 2
                pc.db.skills['Melee'] = 1
                pc.db.skills['Etiquette'] = 1
                pc.db.skills['Lore'] = {'Heraldry': 1}
                pc.db.languages.append('Read Urthish')
                pc.db.blessings.append('Unyielding')
                pc.db.curses.append('Prideful')
            elif house == 'Decados':
                pc.db.attributes['Dexterity'] = 1
                pc.db.attributes['Perception'] = 2
                pc.db.attributes['Ego'] = 2
                pc.db.skills['Inquiry'] = 1
                pc.db.skills['Etiquette'] = 1
                pc.db.choices.append('Rival House')
                pc.db.languages.append('Read Urthish')
                pc.db.blessings.append('Suspicious')
                pc.db.curses.append('Vain')
            elif house == 'Hazat':
                pc.db.attributes['Endurance'] = 1
                pc.db.attributes['Perception'] = 2
                pc.db.attributes['Passion'] = 2
                pc.db.skills['Impress'] = 1
                pc.db.skills['Melee'] = 1
                pc.db.skills['Etiquette'] = 1
                pc.db.languages.append('Read Urthish')
                pc.db.blessings.append('Disciplined')
                pc.db.curses.append('Vengeful')
            elif house == "Li Halan":
                pc.db.attributes['Wits'] = 1
                pc.db.choices.append("ExIn")
                pc.db.choices.append("PasCalm")
                pc.db.attributes['Faith'] = 2
                pc.db.skills['Focus'] = 1
                pc.db.skills['Etiquette'] = 1
                pc.db.skills['Lore Theology'] = 1
                pc.db.languages.append('Read Latin')
                pc.db.languages.append('Read Urthish')
                pc.db.blessings.append('Pious')
                pc.db.curses.append('Guilty')
            else:
                pc.db.attributes['Dexterity'] = 1
                pc.db.attributes['Wits'] = 1
                pc.db.choices.append("ExIn")
                pc.db.attributes['Calm'] = 2
                pc.db.skills['Etiquette'] = 1
                pc.db.languages.append('Speak Graceful Tongue')
                pc.db.languages.append('Read Urthish')
                pc.db.blessings.append('Gracious')
                pc.db.curses.append('Impetuous')

        # Rural Estate
        elif which == 1:
            if house == "Hawkwood":
                pc.db.attributes['Strength'] = 2
                pc.db.attributes['Dexterity'] = 1
                pc.db.attributes['Wits'] = 1
                pc.db.attributes['Extrovert'] = 1
                pc.db.skills['Etiquette'] = 1
                pc.db.choices.append('Fief')
                pc.db.languages.append('Read Urthish')
                pc.db.skills['Ride'] = 1
                pc.db.blessings.append('Unyielding')
                pc.db.curses.append('Prideful')
            elif house == "Decados":
                pc.db.attributes['Dexterity'] = 2
                pc.db.attributes['Perception'] = 2
                pc.db.attributes['Ego'] = 1
                pc.db.skills['Etiquette'] = 1
                pc.db.choices.append('Rival')
                pc.db.skills['Knavery'] = 1
                pc.db.languages.append('Read Urthish')
                pc.db.blessings.append('Suspicious')
                pc.db.curses.append('Vain')
            elif house == "Hazat":
                pc.db.attributes['Endurance'] = 2
                pc.db.attributes['Perception'] = 2
                pc.db.attributes['Passion'] = 1
                pc.db.skills['Impress'] = 1
                pc.db.skills['Melee'] = 1
                pc.db.skills['Etiquette'] = 1
                pc.db.languages.append('Read Urthish')
                pc.db.blessings.append('Disciplined')
                pc.db.curses.append('Vengeful')
            elif house == "Li Halan":
                pc.db.attributes['Wits'] = 1
                pc.db.choices.append("ExIn")
                pc.db.choices.append("PasCalm")
                pc.db.attributes['Faith'] = 2
                pc.db.skills['Etiquette'] = 1
                pc.db.skills['Focus'] = 1
                pc.db.skills['Lore Theology'] = 1
                pc.db.languages.append('Read Latin')
                pc.db.blessings.append('Pious')
                pc.db.curses.append('Guilty')
            else:
                pc.db.attributes['Dexterity'] = 2
                pc.db.attributes['Wits'] = 1
                pc.db.choices.append("ExIn")
                pc.db.attributes['Calm'] = 1
                pc.db.skills['Etiquette'] = 1
                pc.db.languages.append('Speak Graceful Tongue')
                pc.db.languages.append('Read Urthish')
                pc.db.blessings.append('Gravious')
                pc.db.blessings.append('Vain')

        # Landless
        elif which == 2:
            if house == "Hawkwood":
                pc.db.attributes['Strength'] = 1
                pc.db.attributes['Dexterity'] = 2
                pc.db.attributes['Wits'] = 1
                pc.db.attributes['Extrovert'] = 1
                pc.db.skills['Impress'] = 1
                pc.db.skills['Vigor'] = 1
                pc.db.skills['Melee'] = 2
                pc.db.skills['Ride'] = 1
                pc.db.blessings.append('Unyielding')
                pc.db.curses.append('Prideful')
            elif house == "Decaods":
                pc.db.attributes['Dexterity'] = 2
                pc.db.attributes['Perception'] = 2
                pc.db.attributes['Ego'] = 1
                pc.db.skills['Melee'] = 1
                pc.db.skills['Observe'] = 1
                pc.db.skills['Sneak'] = 1
                pc.db.skills['Knavery'] = 2
                pc.db.blessings.append('Suspicious')
                pc.db.curses.append('Vain')
            elif house == "Hazat":
                pc.db.attributes['Endurance'] = 2
                pc.db.attributes['Perception'] = 2
                pc.db.attributes['Passion'] = 1
                pc.db.skills['Impress'] = 1
                pc.db.skills['Melee'] = 1
                pc.db.skills['Shoot'] = 1
                pc.db.skills['Vigor'] = 1
                pc.db.skills['Remedy'] = 1
                pc.db.blessings.append('Disciplined')
                pc.db.curses.append('Vengeful')
            elif house == "Li Halan":
                pc.db.attributes['Wits'] = 1
                pc.db.choices.append("ExIn")
                pc.db.choices.append("PasCalm")
                pc.db.attributes['Faith'] = 2
                pc.db.skills['Melee'] = 1
                pc.db.skills['Observe'] = 1
                pc.db.skills['Focus'] = 1
                pc.db.skills['Lore Theology'] = 1
                pc.db.skills['Remedy'] = 1
                pc.db.blessings.append('Pious')
                pc.db.curses.append('Guilty')
            else:
                pc.db.attributes['Dexterity'] = 2
                pc.db.attributes['Wits'] = 2
                pc.db.choices.append('ExIn')
                pc.db.attributes['Faith'] = 2
                pc.db.skills['Melee'] = 1
                pc.db.skills['Inquiry'] = 1
                pc.db.skills['Lore Trading'] = 1
                pc.db.languages.append('Speak Graceful Tongue')
                pc.db.blessings.append('Gracious')
                pc.db.curses.append('Impetuous')

    # Apprenticeship
    else stage == 1:
        if which == 0:  # Soldier
            addsheet(pc, 'Strength', 'Attributes', 2)
            addsheet(pc, 'Dexterity', 'Attributes', 2)
            addsheet(pc, 'Endurance', 'Attributes', 1)
            addsheet(pc, 'Fight', 'Skills', 1)
            addsheet(pc, 'Shoot', 'Skills', 2)
            addsheet(pc, 'Vigor', 'Skills', 1)
            pc.db.skills['Remedy'] = 1
            pc.db.skills['Social Leadership'] = 3
            pc.db.skills['Survival'] = 1
            pc.db.skills['Warfare Military Tactics'] = 1
        elif which == 1:  # Starman
            addsheet(pc, 'Dexterity', 'Attributes', 1)
            addsheet(pc, 'Wits', 'Attributes', 2)
            addsheet(pc, 'Perception', 'Attributes', 1)
            addsheet(pc, 'Extrovert', 'Attributes', 1)
            addsheet(pc, 'Impress', 'Skills', 1)
            addsheet(pc, 'Melee', 'Skills', 1)
            addsheet(pc, 'Shoot', 'Skills', 2)
            pc.db.skills['Remedy'] = 1
            pc.db.skills['Social Leadership'] = 2
            pc.db.skills['Spacesuit'] = 0
            pc.db.skills['Think Machine'] = 1
            pc.db.skills['Warfare Gunnery'] = 1
        elif which == 2:  # Diplomacy and Intrigue
            addsheet(pc, 'Wits', 'Attributes', 2)
            addsheet(pc, 'Perception', 'Attributes', 1)
            addsheet(pc, 'Extrovert', 'Attributes', 1)
            addsheet(pc, 'Calm', 'Attributes', 1)
            addsheet(pc, 'Charm', 'Skills', 2)
            addsheet(pc, 'Observe', 'Skills', 1)
            addsheet(pc, 'Sneak', 'Skills', 1)
            pc.db.skills['Arts Rhetoric'] = 1
            pc.db.skills['Etiquette'] = 2
            pc.db.choices.append("NADip")
            pc.db.choices.append("NADip2")
        elif which == 3:  # Duelist
            addsheet(pc, 'Strength', 'Attributes', 1)
            addsheet(pc, 'Dexterity', 'Attributes', 2)
            addsheet(pc, 'Endurance', 'Attributes', 1)
            pc.db.choices.append("PasCalm")
            pc.db.choices.append("NADuelist")
            addsheet(pc, 'Melee', 'Skills', 2)
            pc.db.skills['Remedy'] = 1
            pc.db.actions['Fencing'] = ['Parry', 'Thrust', 'Slash']
        elif which == 4:  # Dandy
            addsheet(pc, 'Dexterity', 'Attributes', 1)
            addsheet(pc, 'Wits', 'Attributes', 2)
            addsheet(pc, 'Perception', 'Attributes', 1)
            pc.db.choices.append('PasCalm')
            pc.db.choices.append('NADandy')
            addsheet(pc, 'Charm', 'Skills', 1)
            addsheet(pc, 'Observe', 'Skills', 1)
            addsheet(pc, 'Shoot', 'Skills', 1)
            pc.db.choices.append('NADandy2')
            pc.db.choices.append('NADandy3')
            pc.db.skills['Empathy'] = 1
            pc.db.skills['Gambling'] = 1
            pc.db.skills['Ride'] = 1
        elif which == 5:  # Study
            addsheet(pc, 'Wits', 'Attributes', 2)
            addsheet(pc, 'Introvert', 'Attributes', 2)
            pc.db.choices.append('PasCalm')
            pc.db.skills['Academia'] = 1
            pc.db.skills['Focus'] = 3
            pc.db.skills['Inquiry'] = 1
            pc.db.choices.append('NAStudy')
            pc.db.choices.append('NAStudy2')

    # Early Career
    else stage == 2:
        if which == 0:  # Soldier
            addsheet(pc, 'Strength', 'Attributes', 2)
            addsheet(pc, 'Dexterity', 'Attributes', 2)
            addsheet(pc, 'Endurance', 'Attributes', 2)
            addsheet(pc, 'Wits', 'Attributes', 1)
            addsheet(pc, 'Perception', 'Attributes', 1)
            addsheet(pc, 'Extrovert', 'Attributes', 1)
            pc.db.choices.append('PasCalm')
            addsheet(pc, 'Dodge', 'Skills', 1)
            addsheet(pc, 'Fight', 'Skills', 1)
            addsheet(pc, 'Impress', 'Skills', 1)
            addsheet(pc, 'Observe', 'Skills', 1)
            addsheet(pc, 'Melee', 'Skills', 1)
            addsheet(pc, 'Shoot', 'Skills', 2)
            addsheet(pc, 'Vigor', 'Skills', 1)
            pc.db.skills['Remedy'] = 1
            pc.db.skills['Social Leadership'] = 4
            pc.db.skills['Survival'] = 1
            pc.db.skills['Warfare Military Tactics'] = 1
            pc.db.benefices['Rank'] = 'Knight'
        elif which == 1:  # Starman
            addsheet(pc, 'Dexterity', 'Attributes', 2)
            addsheet(pc, 'Endurance', 'Attributes', 2)
            addsheet(pc, 'Wits', 'Attributes', 2)
            addsheet(pc, 'Perception', 'Attributes', 1)
            addsheet(pc, 'Extrovert', 'Attributes', 1)
            pc.db.choices.append('PasCalm2')
            addsheet(pc, 'Impress', 'Skills', 1)
            addsheet(pc, 'Melee', 'Skills', 1)
            addsheet(pc, 'Shoot', 'Skills', 2)
            pc.db.skills['Drive Spacecraft'] = 1
            addsheet(pc, 'Read Urthish', 'Languages', 1)
            pc.db.skills['Remedy'] = 1
            pc.db.skills['Social Leadership'] = 2
            pc.db.skills['Warfare Gunnery'] = 1
            pc.db.skills['Spacesuit'] = 0
            pc.db.skills['Think Machine'] = 1
            pc.db.skills['Warfare Starfleet Tactics'] = 1
            pc.db.benefices['Rank'] = 'Knight'
        elif which == 2:  # Duelist
            addsheet(pc, 'Strength', 'Attributes', 1)
            addsheet(pc, 'Dexterity', 'Attributes', 2)
            addsheet(pc, 'Endurance', 'Attributes', 2)
            addsheet(pc, 'Wits', 'Attributes', 1)
            addsheet(pc, 'Perception', 'Attributes', 1)
            pc.db.choices.append('ExIn')
            pc.db.choices.append('PasCalm2')
            addsheet(pc, 'Dodge', 'Skills', 1)
            addsheet(pc, 'Melee', 'Skills', 2)
            pc.db.skills['Etiquette'] = 1
            pc.db.skills['Remedy'] = 1
            pc.db.choices.append('NAECDuelist')
            pc.db.benefices['Rank'] = 'Knight'
        elif which == 3:  # Ambassador
            addsheet(pc, 'Dexterity', 'Attributes', 1)
            addsheet(pc, 'Wits', 'Attributes', 2)
            addsheet(pc, 'Perception', 'Attributes', 2)
            addsheet(pc, 'Extrovert', 'Attributes', 2)
            addsheet(pc, 'Calm', 'Attributes', 2)
            pc.db.choices.add('FaiEgo')
            addsheet(pc, 'Charm', 'Skills', 2)
            addsheet(pc, 'Observe', 'Skills', 1)
            addsheet(pc, 'Sneak', 'Skills', 1)
            pc.db.skills['Arts Rhetoric'] = 1
            addsheet(pc, 'Read Urthish', 'Languages', 1)
            pc.db.skills['Etiquette'] = 2
            pc.db.skills['Warfare Gunnery'] = 1
            pc.db.skills['Ride'] = 1
            pc.db.benefices['Rank'] = 'Knight'
            pc.db.choices.append('NECA1')
            pc.db.choices.append('NECA2')


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
        caller.db.questing = 1
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
    options = ({"key": "0", "desc": "High Court", "goto": "menunode_lpnq4"},
               {"key": "1", "desc": "Rural Estate", "goto": "menunode_lpnq4"},
               {"key": "2", "desc": "Landless", "goto": "menunode_lpnq4"})
    return text, options


def menunode_lpn3(caller, raw_input):

    apply_path_noble(0, raw_input, caller.db.house, caller)

    text = "At this stage you pick an apprenticeship under another noble.\n"
    text += "However, nobles also have the option of switching to any of the other archetypes as well.\n"
    text += "At this stage, please choose whether or not you want to move to another Archetype."


    def merchants(caller):
        caller.db.archetype = "Merchant"


    def priests(caller):
        caller.db.archetype = "Priest"


    options = ({"key": "0", "desc": "Stay a Noble", "goto": "menunode_lpn4"},
               {"key": "1", "desc": "Move to Priests", "exec": priests, "goto": "menunode_lppn3"},
               {"key": "2", "desc": "Move to Merchants", "exec": merchants, "goto": "menunode_lpmn3"})
    return text, options


def menunode_lpn4(caller):
    text = "Please select your noble apprenticeship."
    options = ({"key": "0", "desc": "Soldier", "goto": "menunode_lpn5"},
               {"key": "1", "desc": "Starman", "goto": "menumode_lpn5"},
               {"key": "2", "desc": "Diplomacy and Intrigue", "goto": "menumode_lpn5"},
               {"key": "3", "desc": "Duelist", "goto": "menumode_lpn5"},
               {"key": "4", "desc": "Dandy", "goto": "menumode_lpn5"},
               {"key": "5", "desc": "Study", "goto": "menumode_lpn5"})
    return text, options


def menunode_lpnq4(caller):
    text = "Please select your noble apprenticeship."
    options = ({"key": "0", "desc": "Soldier", "goto": "menunode_lpnq5"},
               {"key": "1", "desc": "Starman", "goto": "menumode_lpnq5"},
               {"key": "2", "desc": "Diplomacy and Intrigue", "goto": "menumode_lpnq5"},
               {"key": "3", "desc": "Duelist", "goto": "menumode_lpnq5"},
               {"key": "4", "desc": "Dandy", "goto": "menumode_lpnq5"},
               {"key": "5", "desc": "Study", "goto": "menumode_lpnq5"})
    return text, options


def menunode_lpn5(caller, raw_input):

    apply_path_noble(1, raw_input, 'None', caller)

    text = "Please select your noble's Early Career."
    options = ({"key": "0", "desc": "Soldier", "goto": "menunode_lpn6"},
               {"key": "1", "desc": "Starman", "goto": "menunode_lpn6"},
               {"key": "2", "desc": "Duelist", "goto": "menunode_lpn6"},
               {"key": "3", "desc": "Ambassador", "goto": "menunode_lpn6"})

    return text, options


def menunode_lpnq5(caller, raw_input):
    # Questing knights are mostly the same, but they can't suddenly switch to other archetypes and their early career is set in stone.
    apply_path_noble(1, raw_input, 'None', caller)

    # Questing knights have so many choices. Good lord.


def menunode_lpn6(caller, raw_input):

    apply_path_noble(2, raw_input, 'None', caller)

    # Paths converge on Tours of Duty
