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

Reading this: hahaha, good luck.

"""

from evennia.utils import evmenu
from evennia.utils.evmenu import get_input
from evennia import Command
from world import fsutils

"""

Begin helper section. This section is nothing but helper variables and dictionaries for parsing user input in the menus.

"""
# Parses the input on noble house from the keys into the name.
househelper = {'0': 'Hawkwood', '1': 'Decados', '2': 'Hazat', '3': 'Li Halan', '4': 'al-Malik'}


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
                pc.db.skills['Lore Heraldry'] = 1
                pc.db.languages.append('Read Urthish')
                pc.db.blessings.append('Unyielding')
                pc.db.curses.append('Prideful')
            elif house == 'Decados':
                pc.db.attributes['Dexterity'] = 1
                pc.db.attributes['Perception'] = 2
                pc.db.attributes['Ego'] = 2
                pc.db.skills['Inquiry'] = 1
                pc.db.skills['Etiquette'] = 1
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
                pc.db.languages.append('Read Urthish')
                pc.db.skills['Ride'] = 1
                pc.db.blessings.append('Unyielding')
                pc.db.curses.append('Prideful')
            elif house == "Decados":
                pc.db.attributes['Dexterity'] = 2
                pc.db.attributes['Perception'] = 2
                pc.db.attributes['Ego'] = 1
                pc.db.skills['Etiquette'] = 1
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
            addsheet(pc, 'Remedy', 'Skills', 1)
            addsheet(pc, 'Social Leadership', 'Skills', 3)
            addsheet(pc, 'Survival', 'Skills', 1)
            addsheet(pc, 'Warfare Military Tactics', 'Skills', 1)
        elif which == 1:  # Starman
            addsheet(pc, 'Dexterity', 'Attributes', 1)
            addsheet(pc, 'Wits', 'Attributes', 2)
            addsheet(pc, 'Perception', 'Attributes', 1)
            addsheet(pc, 'Extrovert', 'Attributes', 1)
            addsheet(pc, 'Impress', 'Skills', 1)
            addsheet(pc, 'Melee', 'Skills', 1)
            addsheet(pc, 'Shoot', 'Skills', 2)
            addsheet(pc, 'Remedy', 'Skills', 1)
            addsheet(pc, 'Social Leadership', 'Skills', 2)
            addsheet(pc, 'Think Machine', 'Skills', 1)
            addsheet(pc, 'Warfare Gunnery', 'Skills', 1)
            pc.db.skills['Spacesuit'] = 0  # Spacesuit has no levels. You either have it or you don't.
        elif which == 2:  # Diplomacy and Intrigue
            addsheet(pc, 'Wits', 'Attributes', 2)
            addsheet(pc, 'Perception', 'Attributes', 1)
            addsheet(pc, 'Extrovert', 'Attributes', 1)
            addsheet(pc, 'Calm', 'Attributes', 1)
            addsheet(pc, 'Charm', 'Skills', 2)
            addsheet(pc, 'Observe', 'Skills', 1)
            addsheet(pc, 'Sneak', 'Skills', 1)
            addsheet(pc, 'Arts Rhetoric', 'Skills', 1)
            addsheet(pc, 'Etiquette', 'Skills', 2)
            pc.db.choices.append("NADip")
            pc.db.choices.append("NADip2")
        elif which == 3:  # Duelist
            addsheet(pc, 'Strength', 'Attributes', 1)
            addsheet(pc, 'Dexterity', 'Attributes', 2)
            addsheet(pc, 'Endurance', 'Attributes', 1)
            pc.db.choices.append("PasCalm")
            pc.db.choices.append("NADuelist")
            addsheet(pc, 'Melee', 'Skills', 2)
            addsheet(pc, 'Remedy', 'Skills', 1)
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
            addsheet(pc, 'Empathy', 'Skills', 1)
            addsheet(pc, 'Gambling', 'Skills', 1)
            addsheet(pc, 'Ride', 'Skills', 1)s
        elif which == 5:  # Study
            addsheet(pc, 'Wits', 'Attributes', 2)
            addsheet(pc, 'Introvert', 'Attributes', 2)
            pc.db.choices.append('PasCalm')
            addsheet(pc, 'Academia', 'Skills', 1)
            addsheet(pc, 'Focus', 'Skills', 3)
            addsheet(pc, 'Inquiry', 'Skills', 1)
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

#  Begin Noble Section
def menumode_lpn1(caller):
    caller.db.archetype = "Noble"
    caller.db.recbenefices = ('Nobility', 'Riches')
    text = "As nobility, your first step is picking a house. Please pick one.\n"
    text += "If you are going to use minor house and not follow an existing house, use custom cg."
    options = ({"key": "0", "desc": "Hawkwood", "goto": "menunode_lpn2"},
               {"key": "1", "desc": "Decados", "goto": "menumode_lpn2"},
               {"key": "2", "desc": "Hazat", "goto": "menumode_lpn2"},
               {"key": "3", "desc": "Li Halan", "goto": "menumode_lpn2"},
               {"key": "4", "desc": "al-Malik", "goto": "menumode_lpn2"},
               {"key": "5", "desc": "Questing Knight", "goto": "menumode_lpn2"},
               {"key": "6", "desc": "Minor House", "goto": "menumode_lpn2"})


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
    elif raw_input == 6:
        caller.db.minor = 1
        text = "Which existing house are you mirroring?"
        options = ({"key": "0", "desc": "Hawkwood", "goto": "menunode_lpnmh"},
                   {"key": "1", "desc": "Decados", "goto": "menumode_lpnmh"},
                   {"key": "2", "desc": "Hazat", "goto": "menumode_lpnmh"},
                   {"key": "3", "desc": "Li Halan", "goto": "menumode_lpnmh"},
                   {"key": "4", "desc": "al-Malik", "goto": "menumode_lpnmh"},
                   {"key": "5", "desc": "Questing Knight", "goto": "menumode_lpnmh"})
        return text, options

    if raw_input == 3:
        caller.db.recbenefices.append('Church Ally')
    elif raw_input == 4:
        caller.db.recbenefices.append('Passage Contract')

    caller.db.house = househelper[raw_input]

    if raw_input == 3:
        text = "Li Halan need to make some choices. First would you like a point of Extrovert or Introvert?"
        options = ({"key": "0", "desc": "Extrovert", "exec": addsheet(caller, 'Extrovert', 'Attributes', 1), "goto": "menunode_lpnlhs"},
                   {"key": "1", "desc": "Introvert", "exec": addsheet(caller, 'Introvert', 'Attributes', 1), "goto": "menunode_lpnlhs"})
        return text, options
    elif raaw_input == 4:
        text = "Al-Malik need to pick between a point of Extrovert or Introvert."
        options = ({"key": "0", "desc": "Extrovert", "exec": addsheet(caller, 'Extrovert', 'Attributes', 1), "goto": "menunode_lpnams"},
                   {"key": "1", "desc": "Introvert", "exec": addsheet(caller, 'Introvert', 'Attributes', 1), "goto": "menunode_lpnams"})
        return text, options

    text = "At this point you select your upbringing. Depending on your house you will gain various bonuses."
    options = ({"key": "0", "desc": "High Court", "goto": "menunode_lpn3"},
               {"key": "1", "desc": "Rural Estate", "goto": "menunode_lpn3"},
               {"key": "2", "desc": "Landless", "goto": "menunode_lpn3"})
    return text, options


def menunode_lpnds(caller):
    text = "At this stage you pick an apprenticeship under another noble.\n"
    text += "However, nobles also have the option of switching to any of the other archetypes as well.\n"
    text += "At this stage, please choose whether or not you want to move to another Archetype."


    def merchants(caller):
        caller.db.archetype = "Merchant"


    def priests(caller):
        caller.db.archetype = "Priest"


    options = ({"key": "0", "desc": "Stay a Noble", "goto": "menunode_lpn4"},
               {"key": "1", "desc": "Move to Priests", "exec": priests, "goto": "menunode_NOBLE_TO_PRIEST"},
               {"key": "2", "desc": "Move to Merchants", "exec": merchants, "goto": "menunode_NOBLE_TO_MERCHANT"})
    return text, options


def menunode_lpnlhs(caller):
    text = "Lastly, would you like a point of Passion or Calm?"
    options = ({"key": "0", "desc": "Passion", "exec": addsheet(caller, 'Passion', 'Attributes', 1), "goto": "menunode_lpnlhs2"},
               {"key": "1", "desc": "Calm", "exec": addsheet(caller, 'Calm', 'Attributes', 1), "goto": "menunode_lpnlhs2"})
    return text, options


def menunode_lpnlhs2(caller):
    text = "At this point you select your upbringing. Depending on your house you will gain various bonuses."
    options = ({"key": "0", "desc": "High Court", "goto": "menunode_lpn3"},
               {"key": "1", "desc": "Rural Estate", "goto": "menunode_lpn3"},
               {"key": "2", "desc": "Landless", "goto": "menunode_lpn3"})
    return text, options


def menunode_lpnams(caller):
    text = "At this point you select your upbringing. Depending on your house you will gain various bonuses."
    options = ({"key": "0", "desc": "High Court", "goto": "menunode_lpn3"},
               {"key": "1", "desc": "Rural Estate", "goto": "menunode_lpn3"},
               {"key": "2", "desc": "Landless", "goto": "menunode_lpn3"})
    return text, options


def menunode_lpnmh(caller, raw_input):
    if raw_input == 5:
        caller.db.questing = 1
        text = "You selected questing knight. Please select the noble house you intend to mirror for bonuses."
        options = ({"key": "0", "desc": "Hawkwood", "goto": "menunode_lpnq"},
               {"key": "1", "desc": "Decados", "goto": "menumode_lpnq"},
               {"key": "2", "desc": "Hazat", "goto": "menumode_lpnq"},
               {"key": "3", "desc": "Li Halan", "goto": "menumode_lpnq"},
               {"key": "4", "desc": "al-Malik", "goto": "menumode_lpnq"})
        return text, options

    caller.db.house = househelper[raw_input]

    if raw_input == 3:
        caller.db.recbenefices.append('Church Ally')
    elif raw_input == 4:
        caller.db.recbenefices.append('Passage Contract')

    if raw_input == 1:
        text = "Decados need to pick another house for their lore rival house specialty."
        options = ({"key": "0", "desc": "Hawkwood", "exec": addsheet(caller, 'Lore Hawkwood', 'Skills', 1), "goto": "menunode_lpnds"},
                   {"key": "1", "desc": "Decados", "exec": addsheet(caller, 'Lore Decados', 'Skills', 1), "goto": "menumode_lpnds"},
                   {"key": "2", "desc": "Hazat", "exec": addsheet(caller, 'Lore Hazat', 'Skills', 1), "goto": "menumode_lpnds"},
                   {"key": "3", "desc": "Li Halan", "exec": addsheet(caller, 'Lore Li Halan', 'Skills', 1), "goto": "menumode_lpnds"},
                   {"key": "4", "desc": "al-Malik", "exec": addsheet(caller, 'Lore al-Malik', 'Skills', 1), "goto": "menumode_lpnds"})
        return text, options
    elif raw_input == 3:
        text = "Li Halan need to make some choices. First would you like a point of Extrovert or Introvert?"
        options = ({"key": "0", "desc": "Extrovert", "exec": addsheet(caller, 'Extrovert', 'Attributes', 1), "goto": "menunode_lpnlhs"},
                   {"key": "1", "desc": "Introvert", "exec": addsheet(caller, 'Introvert', 'Attributes', 1), "goto": "menunode_lpnlhs"})
        return text, options
    elif raaw_input == 4:
        text = "Al-Malik need to pick between a point of Extrovert or Introvert."
        options = ({"key": "0", "desc": "Extrovert", "exec": addsheet(caller, 'Extrovert', 'Attributes', 1), "goto": "menunode_lpnams"},
                   {"key": "1", "desc": "Introvert", "exec": addsheet(caller, 'Introvert', 'Attributes', 1), "goto": "menunode_lpnams"})
        return text, options

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

    if raw_input == 3:
        text = "Li Halan need to make some choices. First would you like a point of Extrovert or Introvert?"
        options = ({"key": "0", "desc": "Extrovert", "exec": addsheet(caller, 'Extrovert', 'Attributes', 1), "goto": "menunode_lpnlhsq"},
                   {"key": "1", "desc": "Introvert", "exec": addsheet(caller, 'Introvert', 'Attributes', 1), "goto": "menunode_lpnlhsq"})
        return text, options
    elif raaw_input == 4:
        text = "Al-Malik need to pick between a point of Extrovert or Introvert."
        options = ({"key": "0", "desc": "Extrovert", "exec": addsheet(caller, 'Extrovert', 'Attributes', 1), "goto": "menunode_lpnamsq"},
                   {"key": "1", "desc": "Introvert", "exec": addsheet(caller, 'Introvert', 'Attributes', 1), "goto": "menunode_lpnamsq"})
        return text, options

    text = "At this point you select your upbringing. Depending on your house you will gain various bonuses."
    options = ({"key": "0", "desc": "High Court", "goto": "menunode_lpnq4"},
               {"key": "1", "desc": "Rural Estate", "goto": "menunode_lpnq4"},
               {"key": "2", "desc": "Landless", "goto": "menunode_lpnq4"})
    return text, options


def menunode_lpndsq(caller):
    text = "Please select your noble apprenticeship."
    options = ({"key": "0", "desc": "Soldier", "goto": "menunode_lpnq5"},
               {"key": "1", "desc": "Starman", "goto": "menumode_lpnq5"},
               {"key": "2", "desc": "Diplomacy and Intrigue", "goto": "menumode_lpnq5"},
               {"key": "3", "desc": "Duelist", "goto": "menumode_lpnq5"},
               {"key": "4", "desc": "Dandy", "goto": "menumode_lpnq5"},
               {"key": "5", "desc": "Study", "goto": "menumode_lpnq5"})
    return text, options

def menunode_lpnlhsq(caller):
    text = "Lastly, would you like a point of Passion or Calm?"
    options = ({"key": "0", "desc": "Passion", "exec": addsheet(caller, 'Passion', 'Attributes', 1), "goto": "menunode_lpnlhs2q"},
               {"key": "1", "desc": "Calm", "exec": addsheet(caller, 'Calm', 'Attributes', 1), "goto": "menunode_lpnlhs2q"})
    return text, options


def menunode_lpnlhs2q(caller):
    text = "At this point you select your upbringing. Depending on your house you will gain various bonuses."
    options = ({"key": "0", "desc": "High Court", "goto": "menunode_lpnq4"},
               {"key": "1", "desc": "Rural Estate", "goto": "menunode_lpnq4"},
               {"key": "2", "desc": "Landless", "goto": "menunode_lpnq4"})
    return text, options


def menunode_lpnamsq(caller):
    text = "At this point you select your upbringing. Depending on your house you will gain various bonuses."
    options = ({"key": "0", "desc": "High Court", "goto": "menunode_lpnq4"},
               {"key": "1", "desc": "Rural Estate", "goto": "menunode_lpnq4"},
               {"key": "2", "desc": "Landless", "goto": "menunode_lpnq4"})
    return text, options


def menunode_lpnhws(caller, raw_input):
    addsheet(caller, 'Lore ' + raw_input, 'Skills', 1)
    text = "At this stage you pick an apprenticeship under another noble.\n"
    text += "However, nobles also have the option of switching to any of the other archetypes as well.\n"
    text += "At this stage, please choose whether or not you want to move to another Archetype."


    def merchants(caller):
        caller.db.archetype = "Merchant"


    def priests(caller):
        caller.db.archetype = "Priest"


    options = ({"key": "0", "desc": "Stay a Noble", "goto": "menunode_lpn4"},
               {"key": "1", "desc": "Move to Priests", "exec": priests, "goto": "menunode_NOBLE_TO_PRIEST"},
               {"key": "2", "desc": "Move to Merchants", "exec": merchants, "goto": "menunode_NOBLE_TO_MERCHANT"})
    return text, options


def menunode_lpnhwsq(caller, raw_input):
    addsheet(caller, 'Lore ' + raw_input, 'Skills', 1)

    text = "Please select your noble apprenticeship."
    options = ({"key": "0", "desc": "Soldier", "goto": "menunode_lpnq5"},
               {"key": "1", "desc": "Starman", "goto": "menumode_lpnq5"},
               {"key": "2", "desc": "Diplomacy and Intrigue", "goto": "menumode_lpnq5"},
               {"key": "3", "desc": "Duelist", "goto": "menumode_lpnq5"},
               {"key": "4", "desc": "Dandy", "goto": "menumode_lpnq5"},
               {"key": "5", "desc": "Study", "goto": "menumode_lpnq5"})
    return text, options


def menunode_lpn3(caller, raw_input):

    apply_path_noble(0, raw_input, caller.db.house, caller)

    if caller.db.house == 'Decados' and raw_input != 2:
        text = "Decados need to pick another house for their lore rival house specialty."
        options = ({"key": "0", "desc": "Hawkwood", "exec": addsheet(caller, 'Lore Hawkwood', 'Skills', 1), "goto": "menunode_lpnds"},
                   {"key": "1", "desc": "Decados", "exec": addsheet(caller, 'Lore Decados', 'Skills', 1), "goto": "menumode_lpnds"},
                   {"key": "2", "desc": "Hazat", "exec": addsheet(caller, 'Lore Hazat', 'Skills', 1), "goto": "menumode_lpnds"},
                   {"key": "3", "desc": "Li Halan", "exec": addsheet(caller, 'Lore Li Halan', 'Skills', 1), "goto": "menumode_lpnds"},
                   {"key": "4", "desc": "al-Malik", "exec": addsheet(caller, 'Lore al-Malik', 'Skills', 1), "goto": "menumode_lpnds"})
        return text, options
    elif caller.db.house == 'Hawkwood' and raw_input == 1:
        text = "Hawkwood need to specify a location for their Lore Fief. Enter one now."
        options = ({"key": "_default", "goto": "menunode_lpnhws"})
        return text, options

    text = "At this stage you pick an apprenticeship under another noble.\n"
    text += "However, nobles also have the option of switching to any of the other archetypes as well.\n"
    text += "At this stage, please choose whether or not you want to move to another Archetype."


    def merchants(caller):
        caller.db.archetype = "Merchant"


    def priests(caller):
        caller.db.archetype = "Priest"


    options = ({"key": "0", "desc": "Stay a Noble", "goto": "menunode_lpn4"},
               {"key": "1", "desc": "Move to Priests", "exec": priests, "goto": "menunode_NOBLE_TO_PRIEST"},
               {"key": "2", "desc": "Move to Merchants", "exec": merchants, "goto": "menunode_NOBLE_TO_MERCHANT"})
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


def menunode_lpnq4(caller, raw_input):

    apply_path_noble(0, raw_input, caller.db.house, caller)

    if raw_input != 2 and caller.db.house == 'Decados':
        text = "Decados need to pick another house for their lore rival house specialty."
        options = ({"key": "0", "desc": "Hawkwood", "exec": addsheet(caller, 'Lore Hawkwood', 'Skills', 1), "goto": "menunode_lpndsq"},
                   {"key": "1", "desc": "Decados", "exec": addsheet(caller, 'Lore Decados', 'Skills', 1), "goto": "menumode_lpndsq"},
                   {"key": "2", "desc": "Hazat", "exec": addsheet(caller, 'Lore Hazat', 'Skills', 1), "goto": "menumode_lpndsq"},
                   {"key": "3", "desc": "Li Halan", "exec": addsheet(caller, 'Lore Li Halan', 'Skills', 1), "goto": "menumode_lpndsq"},
                   {"key": "4", "desc": "al-Malik", "exec": addsheet(caller, 'Lore al-Malik', 'Skills', 1), "goto": "menumode_lpndsq"})
        return text, options
    elif raw_input == 1 and caller.db.house == 'Hawkwood':
        text = "Hawkwood need to specify a location for their Lore Fief. Enter one now."
        options = ({"key": "_default", "goto": "menunode_lpnhwsq"})
        return text, options

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

    if raw_input == 2:
        text = "Do you want Inquiry or Knavery at +2?"
        options = ({"key": "0", "desc": "Inquiry", "exec": addsheet(caller, 'Inquiry', 'Skills', 2), "goto": "menunode_lpn5id2"},
                   {"key": "1", "desc": "Knavery", "exec": addsheet(caller, 'Knavery', 'Skills', 2), "goto": "menunode_lpn5id2"})
        return text, options
    elif raw_input == 3:
        text = "Do you want Passion or Calm +1??"
        options = ({"key": "0", "desc": "Passion", "exec": addsheet(caller, 'Passion', 'Attributes', 1), "goto": "menunode_lpn5d2"},
                   {"key": "1", "desc": "Calm", "exec": addsheet(caller, 'Calm', 'Attributes', 1), "goto": "menunode_lpn5d2"})
        return text, options
    elif raw_input == 4:
        text = "Do you want Passion or Calm +1??"
        options = ({"key": "0", "desc": "Passion", "exec": addsheet(caller, 'Passion', 'Attributes', 1), "goto": "menunode_lpn5da2"},
                   {"key": "1", "desc": "Calm", "exec": addsheet(caller, 'Calm', 'Attributes', 1), "goto": "menunode_lpn5da2"})
        return text, options
    elif raw_input == 5:
        text = "Do you want Passion or Calm +1??"
        options = ({"key": "0", "desc": "Passion", "exec": addsheet(caller, 'Passion', 'Attributes', 1), "goto": "menunode_lpn5s2"},
                   {"key": "1", "desc": "Calm", "exec": addsheet(caller, 'Calm', 'Attributes', 1), "goto": "menunode_lpn5s2"})
        return text, options

    text = "Please select your noble's Early Career."
    options = ({"key": "0", "desc": "Soldier", "goto": "menunode_lpn6"},
               {"key": "1", "desc": "Starman", "goto": "menunode_lpn6"},
               {"key": "2", "desc": "Duelist", "goto": "menunode_lpn6"},
               {"key": "3", "desc": "Ambassador", "goto": "menunode_lpn6"})

    return text, options


def menunode_lpn5id2(caller):
    text = "Do you want debate or oratory for you Social specialty?"
    options = ({"key": "0", "desc": "Debate", "exec": addsheet(caller, 'Social Debate', 'Skills', 1), "goto": "menunode_lpn5c"},
               {"key": "1", "desc": "Oratory", "exec": addsheet(caller, 'Social Oratory', 'Skills', 1), "goto": "menunode_lpn5c"})
    return text, options


def menunode_lpn5d2(caller):
    text = "Do you want Dodge or Vigor +1?"
    options = ({"key": "0", "desc": "Dodge", "exec": addsheet(caller, 'Dodge', 'Skills', 1), "goto": "menunode_lpn5c"},
               {"key": "1", "desc": "Vigor", "exec": addsheet(caller, 'Vigor', 'Skills', 1), "goto": "menunode_lpn5c"})
    return text, options


def menunode_lpn5da2(caller):
    text = "You can select any skill for +2. Please enter it now."
    options = ({"key": "_default", "goto": "menunode_lpn5da3"})
    return text, options


def menunode_lpn5da3(caller, raw_input):
    addsheet(caller, raw_input, 'Skills', 2)

    text = "What specialty would you like for your Arts skill at +1? Enter it now."
    options = ({"key": "_default", "goto": "menunode_lpn5da4"})
    return text, options


def menunode_lpn5da4(caller, raw_input):
    addsheet(caller, 'Arts ' + raw_input, 'Skills', 1)

    text = "Do you want Aircraft or Landcraft for your drive specialty?"
    options = ({"key": "0", "desc": "Aircraft", "exec": addsheet(caller, 'Drive Aircraft', 'Skills', 1), "goto": "menunode_lpn5c"},
               {"key": "1", "desc": "Landcraft", "exec": addsheet(caller, 'Drive Landcraft', 'Skills', 1), "goto": "menunode_lpn5c"})
    return text, options


def menunode_lpn5s2(caller):
    text = "Please enter Lore or Science followed by your object of study. Ex: Lore War or Science Landcraft."
    options = ({"key": "_default", "goto": "menunode_lpn5s3"})
    return text, options


def menunode_lpn5s3(caller, raw_input):
    if not 'Lore' in raw_input or not 'Science' in raw_input:
        text = "You did not enter Lore or Science. Enter Lore or Science followed by your object of study. Ex: Lore War or Science Landcraft."
        options = ({"key": "_default", "goto": "menunode_lpn5s3"})
        return text, options

    addsheet(caller, raw_input, 'Skills', 3)

    text = "Do you want Read Urthish or Read Lating?"
    options = ({"key": "0", "desc": "Urthish", "exec": addsheet(caller, 'Read Urthish', 'Languages', 1), "goto": "menunode_lpn5c"},
               {"key": "1", "desc": "Latin", "exec": addsheet(caller, 'Read Latin', 'Languages', 1), "goto": "menunode_lpn5c"})
    return text, options

def menunode_lpn5c(caller):
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
    text = "Now let's begin the long process of setting your choices for questing knight.\n"
    text += "Pick your first Body attribute. This one gets +2."
    options = ({"Key": "0", "desc": "Strength", "exec": addsheet(caller, 'Strength', 'Attributes', 2), "goto": "menunode_lpnq52"},
               {"Key": "1", "desc": "Dexterity", "exec": addsheet(caller, 'Dexterity', 'Attributes', 2), "goto": "menunode_lpnq52"},
               {"Key": "2", "desc": "Endurance", "exec": addsheet(caller, 'Endurance', 'Attributes', 2), "goto": "menunode_lpnq52"})

    return text, options


def menunode_lpnq52(caller):
    text = "Now pick your second body attribute. It gets +1."
    options = ({"Key": "0", "desc": "Strength", "exec": addsheet(caller, 'Strength', 'Attributes', 1), "goto": "menunode_lpnq53"},
               {"Key": "1", "desc": "Dexterity", "exec": addsheet(caller, 'Dexterity', 'Attributes', 1). "goto": "menunode_lpnq53"},
               {"Key": "2", "desc": "Endurance", "exec": addsheet(caller, 'Endurance', 'Attributes', 1), "goto": "menunode_lpnq53"})

    return text, options


def menunode_lpnq53(caller):
    text = "Now pick your third body attribute. It gets +1."
    options = ({"Key": "0", "desc": "Strength", "exec": addsheet(caller, 'Strength', 'Attributes', 1), "goto": "menunode_lpnq54"},
               {"Key": "1", "desc": "Dexterity", "exec": addsheet(caller, 'Strength', 'Attributes', 1), "goto": "menunode_lpnq54"},
               {"Key": "2", "desc": "Endurance", "exec": addsheet(caller, 'Strength', 'Attributes', 1), "goto": "menunode_lpnq54"})

    return text, options


def menunode_lpnq54(caller):
    text = "Now pick your first mind attribute. It gets +2."
    options = ({"Key": "0", "desc": "Perception", "exec": addsheet(caller, 'Perception', 'Attributes', 2), "goto": "menunode_lpnq55"},
               {"Key": "1", "desc": "Wits", "exec": addsheet(caller, 'Wits', 'Attributes', 2), "goto": "menunode_lpnq55"},
               {"Key": "2", "desc": "Tech", "exec": addsheet(caller, 'Tech', 'Attributes', 2), "goto": "menunode_lpnq55"})

    return text, options


def menunode_lpnq55(caller):
    text = "Now pick your second mind attribute. It gets +1."
    options = ({"Key": "0", "desc": "Perception", "exec": addsheet(caller, 'Perception', 'Attributes', 1), "goto": "menunode_lpnq56"},
               {"Key": "1", "desc": "Wits", "exec": addsheet(caller, 'Wits', 'Attributes', 1), "goto": "menunode_lpnq56"},
               {"Key": "2", "desc": "Tech", "exec": addsheet(caller, 'Tech', 'Attributes', 1), "goto": "menunode_lpnq56"})

    return text, options


def menunode_lpnq56(caller):
    text = "Now pick your first spirit attribute. It gets +2."
    options = ({"Key": "0", "desc": "Presence", "exec": addsheet(caller, 'Presence', 'Attributes', 2), "goto": "menunode_lpnq57"},
               {"Key": "1", "desc": "Will", "exec": addsheet(caller, 'Will', 'Attributes', 2), "goto": "menunode_lpnq57"},
               {"Key": "2", "desc": "Faith", "exec": addsheet(caller, 'Faith', 'Attributes', 2), "goto": "menunode_lpnq57"})

    return text, options


def menumode_lpnq57(caller):
    text = "Now pick your second spirit attribute. It gets +1."
    options = ({"Key": "0", "desc": "Presence", "exec": addsheet(caller, 'Presence', 'Attributes', 1), "goto": "menunode_lpnq58"},
               {"Key": "1", "desc": "Will", "exec": addsheet(caller, 'Will', 'Attributes', 1), "goto": "menunode_lpnq58"},
               {"Key": "2", "desc": "Faith", "exec": addsheet(caller, 'Faith', 'Attributes', 1), "goto": "menunode_lpnq58"})

    return text, options



def menunode_lpnq58(caller):
    text = "Do you want Charm or Impress +1?"
    options = ({"Key": "0", "desc": "Impress", "exec": addsheet(caller, 'Impress', 'Skills', 1), "goto": "menunode_lpnq59"},
               {"Key": "1", "desc": "Charm", "exec": addsheet(caller, 'Charm', 'Skills', 1), "goto": "menunode_lpnq59"})

    return text, options


def menunode_lpnq59(caller):
    addsheet(caller, 'Dodge', 'Skills', 1)

    text = "Pick your primary combat skill. It gets +2."
    options = ({"Key": "0", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 2), "goto": "menunode_lpnq591"},
               {"Key": "1", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 2), "goto": "menunode_lpnq591"},
               {"Key": "2", "desc": "Shoot", "exec": addsheet(caller, 'Shoot', 'Skills', 2), "goto": "menunode_lpnq591"})

    return text, options


def menunode_lpnq591(caller, raw_input):
    text = "Pick your secondary combat skill. It gets +1."
    options = ({"Key": "0", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 1), "goto": "menunode_lpnq592"},
               {"Key": "1", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 1), "goto": "menunode_lpnq592"},
               {"Key": "2", "desc": "Shoot", "exec": addsheet(caller, 'Shoot', 'Skills', 1), "goto": "menunode_lpnq592"})

    if raw_input == 0:
        options = tuple([x for x in options if x['Name'] != 'Fight'])
    elif raw_input == 1:
        options = tuple([x for x in options if x['Name'] != 'Melee'])
    else:
        options = tuple([x for x in options if x['Name'] != 'Shoot'])

    return text, options


def menunode_lpnq592(caller):
    addsheet(caller, 'Observe', 'Skills', 1)
    addsheet(caller, 'Sneak', 'Skills', 1)
    addsheet(caller, 'Vigor', 'Skills', 1)

    text = "Please pick a specialty for Drive."
    options = ({"Key": "0", "desc": "Landcraft", "exec": addsheet(caller, 'Drive Landcraft', 'Skills', 1), "goto": "menunode_lpnq593"},
               {"Key": "1", "desc": "Aircraft", "exec": addsheet(caller, 'Drive Aircraft', 'Skills', 1), "goto": "menunode_lpnq593"})

    return text, options


def menunode_lpnq593(caller):
    text = "Do you want inquiry or knavery +1?"
    options = ({"Key": "0", "desc": "Inquiry", "exec": addsheet(caller, 'Inquiry', 'Skills', 1), "goto": "menunode_lpnq594"},
               {"Key": "1", "desc": "Knavery", "exec": addsheet(caller, 'Knavery', 'Skills', 1), "goto": "menunode_lpnq594"})

    return text, options


def menunode_lpnq594(caller):
    text = "Please enter a specialty for your lore for People and Places seen."
    options = {"key": "_default", "goto": "menunode_lpnq595"}

    return text, options


def menunode_lpnq595(caller, raw_input):
    addsheet(caller, 'Lore ' + raw_input, 'Skills', 1)
    addsheet(caller, 'Remedy', 'Skills', 1)

    text = "Please enter a dialect for your free language choice."
    options = {"key": "_default", "goto": "menunode_lpnq596"}

    return text, options


def menunode_lpnq596(caller, raw_input):
    caller.db.languages.append('Speak ' + raw_input)
    addsheet(caller, 'Streetwise', 'Skills', 1)
    caller.db.benefices['Rank'] = 'Knight'

    # Tour of Duty

def menunode_lpn6(caller, raw_input):
    apply_path_noble(2, raw_input, 'None', caller)

    # Tour of Duty
