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
This implements the lifepaths as described by FAS21901, the Lifepaths source released on the web as a supplement to revised in 2014.

"""

from evennia.utils import evmenu
from evennia.utils.evmenu import get_input
from evennia import Command
from world import fsutils

"""

Begin helper section. This section is nothing but helper variables and dictionaries for parsing user input in the menus.

"""
# Parses the input on noble house from the keys into the name.
househelper = {'0': 'Hawkwood', '1': 'Decados', '2': 'Hazat', '3': 'Li Halan', '4': 'al-Malik', '5': 'Alba', '6': 'Juandaastas', '7': 'Justinian', '8': 'Keddah', '9': 'Masseri', '10': 'Shelit', '11': 'Thana', '12': 'Torenson', '13': 'Trusnikron', '14': 'Van Gelder', '15': 'Xanthippe'}
# Parses priests like househelper
priesthelper = {'0': 'Urth Orthodox', '1': 'Brother Battle', '2': 'Eskatonic Order', '3': 'Temple Avesti', '4': 'Sanctuary Aeon'}
# Parses guilds like househelper
guildhelper = {'0': 'Charioteers', '1': 'Engineers', '2': 'Scravers', '3': 'Muster', '4': 'Reeves'}


# apply blessing and curse
def apply_blessing_curse(pc, house):
    if house == 'Hawkwood':
        addsheet(pc, 'Unyielding', 'Blessings', 0)
        addsheet(pc, 'Prideful', 'Curses', 0)
    
    elif house == 'Decados':
        addsheet(pc, 'Suspicious', 'Blessings', 0)
        addsheet(pc, 'Vain', 'Curses', 0)
        
    elif house == 'Hazat':
        addsheet(pc, 'Disciplined', 'Blessings', 0)
        addsheet(pc, 'Vengeful', 'Curses', 0)
        
    elif house == 'Li Halan':
        addsheet(pc, 'Pious', 'Blessings', 0)
        addsheet(pc, 'Guilty', 'Curses', 0)
        
    elif house == 'al-Malik':
        addsheet(pc, 'Graceful', 'Blessings', 0)
        addsheet(pc, 'Impetuous', 'Curses', 0)
    
    elif house == 'Alba':
        addsheet(pc, 'Connected', 'Blessings', 0)
        addsheet(pc, 'Uncouth', 'Curses', 0)
        
    elif house == 'Juandaastas':
        addsheet(pc, 'Strong-Willed', 'Blessings', 0)
        addsheet(pc, 'Outraged', 'Curses', 0)
        
    elif house == 'Justinian':
        addsheet(pc, 'Loyal', 'Blessings', 0)
        addsheet(pc, 'Stubborn', 'Curses', 0)
        
    elif house == 'Keddah':
        addsheet(pc, 'Alert', 'Blessings', 0)
        addsheet(pc, 'Untrustworthy', 'Curses', 0)
        
    elif house == 'Masseri':
        addsheet(pc, 'Hardy', 'Blessings', 0)
        addsheet(pc, 'Bitter', 'Curses', 0)
        
    elif house == 'Shelit':
        addsheet(pc, 'Cybersympathy', 'Blessings', 0)
        addsheet(pc, 'Weird', 'Curses', 0)
        
    elif house == 'Thana':
        addsheet(pc, 'Angelic', 'Blessings', 0)
        addsheet(pc, 'Guilty', 'Curses', 0)
        
    elif house == 'Torenson':
        addsheet(pc, 'Elan', 'Blessings', 0)
        addsheet(pc, 'Indignant', 'Curses', 0)
        
    elif house == 'Trusnikron':
        addsheet(pc, 'Xeno Equestrian', 'Blessings', 0)
        addsheet(pc, 'Uncouth', 'Curses', 0)
        
    elif house == 'Van Gelder':
        addsheet(pc, 'Chameleon', 'Blessings', 0)
        addsheet(pc, 'Alienated', 'Curses', 0)
        
    elif house == 'Xanthippe':
        addsheet(pc, 'Disciplined', 'Blessings', 0)
        addsheet(pc, 'Condescending', 'Curses', 0)

# Applies bonuses for paths and stages per house for nobles
def apply_path_noble(stage, which, house, pc):
    # Upbringing
    if stage == 0:

        # High Court
        if which == 0:

            if house == 'Hawkwood':
                addsheet(pc, 'Strength', 'Attributes', 1)
                addsheet(pc, 'Dexterity', 'Attributes', 1)
                addsheet(pc, 'Wits', 'Attributes', 1)
                addsheet(pc, 'Presence', 'Attributes', 2)
                addsheet(pc, 'Melee', 'Skills', 1)
                addsheet(pc, 'Etiquette', 'Skills', 1)
                addsheet(pc, 'Influence', 'Skills', 1)
                addsheet(pc, 'Leadership', 'Skills', 1)
                
            elif house == 'Decados':
                addsheet(pc, 'Dexterity', 'Attributes', 1)
                addsheet(pc, 'Perception', 'Attributes', 2)
                addsheet(pc, 'Will', 'Attributes', 2)
                addsheet(pc, 'Etiquette', 'Skills', 1)
                addsheet(pc, 'Investigation', 'Skills', 1)
                addsheet(pc, 'Influence', 'Skills', 1)

            elif house == 'Hazat':
                addsheet(pc, 'Endurance', 'Attributes', 1)
                addsheet(pc, 'Perception', 'Attributes', 2)
                addsheet(pc, 'Presence', 'Attributes', 2)
                addsheet(pc, 'Influence', 'Skills', 1)
                addsheet(pc, 'Melee', 'Skills', 2)
                addsheet(pc, 'Etiquette', 'Skills', 1)
                addsheet(pc, 'Communication', 'Skills', 1)

            elif house == "Li Halan":
                addsheet(pc, 'Wits', 'Attributes', 1)
                addsheet(pc, 'Will', 'Attributes', 1)
                addsheet(pc, 'Presence', 'Attributes', 1)
                addsheet(pc, 'Faith', 'Attributes', 2)
                addsheet(pc, 'Etiquette', 'Skills', 1)
                addsheet(pc, 'Self Control', 'Skills', 1)
                addsheet(pc, 'Latin', 'Languages', 0)

            else:
                addsheet(pc, 'Dexterity', 'Attributes', 1)
                addsheet(pc, 'Wits', 'Attributes', 1)
                addsheet(pc, 'Tech', 'Attributes', 1)
                addsheet(pc, 'Will', 'Attributes', 2)
                addsheet(pc, 'Etiquette', 'Skills', 1)
                addsheet(pc, 'Influence', 'Skills', 1)
                addsheet(pc, 'Graceful Tongue', 'Languages', 0)

        # Rural Estate
        elif which == 1:
            if house == "Hawkwood":
                addsheet(pc, 'Strength', 'Attributes', 2)
                addsheet(pc, 'Dexterity', 'Attributes', 1)
                addsheet(pc, 'Wits', 'Attributes', 1)
                addsheet(pc, 'Presence', 'Attributes', 1)
                addsheet(pc, 'Etiquette', 'Skills', 1)
                addsheet(pc, 'Vigor', 'Skills', 1)
                addsheet(pc, 'Observe', 'Skills', 1)
                addsheet(pc, 'Survival', 'Skills', 1)

            elif house == "Decados":
                addsheet(pc, 'Dexterity', 'Attributes', 2)
                addsheet(pc, 'Perception', 'Attributes', 2)
                addsheet(pc, 'Will', 'Attributes', 1)
                addsheet(pc, 'Etiquette', 'Skills', 1)
                addsheet(pc, 'Sneak', 'Skills', 1)
                addsheet(pc, 'Survival', 'Skills', 1)

            elif house == "Hazat":
                addsheet(pc, 'Endurance', 'Attributes', 2)
                addsheet(pc, 'Perception', 'Attributes', 2)
                addsheet(pc, 'Presence', 'Attributes', 1)
                addsheet(pc, 'Influence', 'Skills', 1)
                addsheet(pc, 'Melee', 'Skills', 1)
                addsheet(pc, 'Etiquette', 'Skills', 1)
                addsheet(pc, 'Survival', 'Skills', 1)
                addsheet(pc, 'Leadership', 'Skills', 1)

            elif house == "Li Halan":
                addsheet(pc, 'Wits', 'Attributes', 1)
                addsheet(pc, 'Will', 'Attributes', 1)
                addsheet(pc, 'Presence', 'Attributes', 1)
                addsheet(pc, 'Faith', 'Attributes', 2)
                addsheet(pc, 'Etiquette', 'Skills', 1)
                addsheet(pc, 'Self Control', 'Skills', 1)
                addsheet(pc, 'Survival', 'Skills', 1)
                addsheet(pc, 'Latin', 'Languages', 0)

            else:
                addsheet(pc, 'Dexterity', 'Attributes', 2)
                addsheet(pc, 'Wits', 'Attributes', 1)
                addsheet(pc, 'Presence', 'Attributes', 1)
                addsheet(pc, 'Will', 'Attributes', 1)
                addsheet(pc, 'Etiquette', 'Skills', 1)
                addsheet(pc, 'Survival', 'Skills', 1)
                addsheet(pc, 'Influence', 'Skills', 1)
                addsheet(pc, 'Graceful Tongue', 'Languages', 0)

        # Landless
        elif which == 2:
            if house == "Hawkwood":
                addsheet(pc, 'Strength', 'Attributes', 1)
                addsheet(pc, 'Dexterity', 'Attributes', 2)
                addsheet(pc, 'Wits', 'Attributes', 1)
                addsheet(pc, 'Presence', 'Attributes', 1)
                addsheet(pc, 'Influence', 'Skills', 1)
                addsheet(pc, 'Vigor', 'Skills', 1)
                addsheet(pc, 'Melee', 'Skills', 2)
                addsheet(pc, 'Survival', 'Skills', 1)

            elif house == "Decaods":
                addsheet(pc, 'Dexterity', 'Attributes', 2)
                addsheet(pc, 'Perception', 'Attributes', 2)
                addsheet(pc, 'Will', 'Attributes', 1)
                addsheet(pc, 'Melee', 'Skills', 1)
                addsheet(pc, 'Observe', 'Skills', 1)
                addsheet(pc, 'Sneak', 'Skills', 1)

            elif house == "Hazat":
                addsheet(pc, 'Endurance', 'Attributes', 2)
                addsheet(pc, 'Perception', 'Attributes', 2)
                addsheet(pc, 'Presence', 'Attributes', 1)
                addsheet(pc, 'Influence', 'Skills', 1)
                addsheet(pc, 'Melee', 'Skills', 1)
                addsheet(pc, 'Vigor', 'Skills', 1)
                addsheet(pc, 'Warfare', 'Skills', 1)

            elif house == "Li Halan":
                addsheet(pc, 'Wits', 'Attributes', 1)
                addsheet(pc, 'Presence', 'Attributes', 1)
                addsheet(pc, 'Will', 'Attributes', 1)
                addsheet(pc, 'Faith', 'Attributes', 2)
                addsheet(pc, 'Melee', 'Skills', 1)
                addsheet(pc, 'Observe', 'Skills', 1)
                addsheet(pc, 'Self Control', 'Skills', 1)
                addsheet(pc, 'Vigor', 'Skills', 1)
                addsheet(pc, 'Physick', 'Skills', 1)

            else:
                addsheet(pc, 'Dexterity', 'Attributes', 2)
                addsheet(pc, 'Wits', 'Attributes', 1)
                addsheet(pc, 'Presence', 'Attributes', 1)
                addsheet(pc, 'Will', 'Attributes', 1)
                addsheet(pc, 'Melee', 'Skills', 1)
                addsheet(pc, 'Investigation', 'Skills', 1)
                addsheet(pc, 'Athletics', 'Skills', 1)
                addsheet(pc, 'Graceful Tongue', 'Languages', 0)

    # Apprenticeship
    elif stage == 1:
        if which == 0:  # Soldier
            addsheet(pc, 'Strength', 'Attributes', 2)
            addsheet(pc, 'Dexterity', 'Attributes', 2)
            addsheet(pc, 'Endurance', 'Attributes', 1)
            addsheet(pc, 'Vigor', 'Skills', 1)
            addsheet(pc, 'Physick', 'Skills', 1)
            addsheet(pc, 'Influence', 'Skills', 1)
            addsheet(pc, 'Leadership', 'Skills', 2)
            addsheet(pc, 'Survival', 'Skills', 1)
            addsheet(pc, 'Warfare', 'Skills', 1)
        elif which == 1:  # Starman
            addsheet(pc, 'Dexterity', 'Attributes', 1)
            addsheet(pc, 'Wits', 'Attributes', 2)
            addsheet(pc, 'Perception', 'Attributes', 1)
            addsheet(pc, 'Presence', 'Attributes', 1)
            addsheet(pc, 'Influence', 'Skills', 1)
            addsheet(pc, 'Melee', 'Skills', 2)
            addsheet(pc, 'Gunnery', 'Skills', 2)
            addsheet(pc, 'Physick', 'Skills', 1)
            addsheet(pc, 'Leadership', 'Skills', 2)
            addsheet(pc, 'Warfare', 'Skills', 1)
        elif which == 2:  # Diplomacy and Intrigue
            addsheet(pc, 'Wits', 'Attributes', 2)
            addsheet(pc, 'Perception', 'Attributes', 1)
            addsheet(pc, 'Presence', 'Attributes', 2)
            addsheet(pc, 'Influence', 'Skills', 2)
            addsheet(pc, 'Observe', 'Skills', 1)
            addsheet(pc, 'Sneak', 'Skills', 1)
            addsheet(pc, 'Etiquette', 'Skills', 2)
            addsheet(pc, 'Leadership', 'Skills', 2)
        elif which == 3:  # Duelist
            addsheet(pc, 'Strength', 'Attributes', 1)
            addsheet(pc, 'Dexterity', 'Attributes', 2)
            addsheet(pc, 'Endurance', 'Attributes', 1)
            addsheet(pc, 'Will', 'Attributes', 1)
            addsheet(pc, 'Vigor', 'Skills', 1)
            addsheet(pc, 'Melee', 'Skills', 2)
            addsheet(pc, 'Physick', 'Skills', 1)
            addsheet(pc, 'Etiquette', 'Skills', 1)
        elif which == 4:  # Dandy
            addsheet(pc, 'Dexterity', 'Attributes', 1)
            addsheet(pc, 'Wits', 'Attributes', 2)
            addsheet(pc, 'Perception', 'Attributes', 1)
            addsheet(pc, 'Presence', 'Attributes', 1)
            addsheet(pc, 'Vigor', 'Skills', 2)
            addsheet(pc, 'Influence', 'Skills', 1)
            addsheet(pc, 'Observe', 'Skills', 1)
            addsheet(pc, 'Empathy', 'Skills', 1)
            addsheet(pc, 'Gambling', 'Skills', 1)
            addsheet(pc, 'Survival', 'Skills', 1)
        elif which == 5:  # Student
            addsheet(pc, 'Wits', 'Attributes', 2)
            addsheet(pc, 'Faith', 'Attributes', 2)
            addsheet(pc, 'Will', 'Attributes', 1)
            addsheet(pc, 'Investigation', 'Skills', 2)
            addsheet(pc, 'Self Control', 'Skills', 3)

    # Early Career
    elif stage == 2:
        if which == 0:  # Soldier
            addsheet(pc, 'Strength', 'Attributes', 2)
            addsheet(pc, 'Dexterity', 'Attributes', 2)
            addsheet(pc, 'Endurance', 'Attributes', 2)
            addsheet(pc, 'Wits', 'Attributes', 1)
            addsheet(pc, 'Perception', 'Attributes', 1)
            addsheet(pc, 'Presence', 'Attributes', 1)
            addsheet(pc, 'Will', 'Attributes', 1)
            addsheet(pc, 'Fight', 'Skills', 1)
            addsheet(pc, 'Influence', 'Skills', 1)
            addsheet(pc, 'Observe', 'Skills', 1)
            addsheet(pc, 'Vigor', 'Skills', 2)
            addsheet(pc, 'Physick', 'Skills', 1)
            addsheet(pc, 'Survival', 'Skills', 1)
            addsheet(pc, 'Warfare', 'Skills', 2)
            pc.db.benefices['Rank'] = 'Knight'
        elif which == 1:  # Starman
            addsheet(pc, 'Dexterity', 'Attributes', 2)
            addsheet(pc, 'Endurance', 'Attributes', 2)
            addsheet(pc, 'Wits', 'Attributes', 2)
            addsheet(pc, 'Perception', 'Attributes', 1)
            addsheet(pc, 'Presence', 'Attributes', 1)
            addsheet(pc, 'Will', 'Attributes', 2)
            addsheet(pc, 'Influence', 'Skills', 1)
            addsheet(pc, 'Gunnery', 'Skills', 1)
            addsheet(pc, 'Spacecraft Operations', 'Skills', 2)
            addsheet(pc, 'Physick', 'Skills', 1)
            addsheet(pc, 'Think Machine', 'Skills', 2)
            addsheet(pc, 'Warfare', 'Skills', 2)
            addsheet(pc, 'Vigor', 'Skills', 2)
            pc.db.benefices['Rank'] = 'Knight'
        elif which == 2:  # Duelist
            addsheet(pc, 'Strength', 'Attributes', 1)
            addsheet(pc, 'Dexterity', 'Attributes', 2)
            addsheet(pc, 'Endurance', 'Attributes', 2)
            addsheet(pc, 'Wits', 'Attributes', 1)
            addsheet(pc, 'Perception', 'Attributes', 1)
            addsheet(pc, 'Presence', 'Attributes', 1)
            addsheet(pc, 'Will', 'Attributes', 2)
            addsheet(pc, 'Athletics', 'Skills', 2)
            addsheet(pc, 'Vigor', 'Skills', 1)
            addsheet(pc, 'Melee', 'Skills', 2)
            addsheet(pc, 'Etiquette', 'Skills', 1)
            addsheet(pc, 'Physick', 'Skills', 1)
            pc.db.benefices['Rank'] = 'Knight'
        elif which == 3:  # Ambassador
            addsheet(pc, 'Dexterity', 'Attributes', 1)
            addsheet(pc, 'Wits', 'Attributes', 2)
            addsheet(pc, 'Perception', 'Attributes', 2)
            addsheet(pc, 'Presence', 'Attributes', 2)
            addsheet(pc, 'Will', 'Attributes', 2)
            addsheet(pc, 'Faith', 'Attributes', 1)
            addsheet(pc, 'Influence', 'Skills', 4)
            addsheet(pc, 'Observe', 'Skills', 1)
            addsheet(pc, 'Sneak', 'Skills', 1)
            addsheet(pc, 'Etiquette', 'Skills', 2)
            addsheet(pc, 'Leadership', 'Skills', 2)
            addsheet(pc, 'Survival', 'Skills', 1)
            pc.db.benefices['Rank'] = 'Knight'


# Merchants and Priests share an upbringing. So they have the same function.
def apply_path_uppm(caller, which, what):
    # Environemnt
    if which == 0:
        # City
        if what == 0:
            addsheet(caller, 'Wits', 'Attributes', 2)
            addsheet(caller, 'Perception', 'Attributes', 2)
            addsheet(caller, 'Observe', 'Skills', 1)
            addsheet(caller, 'Investigation', 'Skills', 1)
            addsheet(caller, 'Empathy', 'Skills', 1)

        # Town
        elif what == 1:
            addsheet(caller, 'Wits', 'Attributes', 1)
            addsheet(caller, 'Perception', 'Attributes', 1)
            addsheet(caller, 'Presence', 'Attributes', 2)
            addsheet(caller, 'Influence', 'Skills', 1)
            addsheet(caller, 'Vigor', 'Skills', 1)
            addsheet(caller, 'Investigaiton', 'Skills', 1)

        # Rural
        elif what == 2:
            addsheet(caller, 'Strength', 'Attributes', 1)
            addsheet(caller, 'Endurance', 'Attributes', 2)
            addsheet(caller, 'Faith', 'Attributes', 1)
            addsheet(caller, 'Vigor', 'Skills', 1)
            addsheet(caller, 'Survival', 'Skills', 2)
            
        # Space Habitat
        elif what == 3:
            addsheet(caller, 'Dexterity', 'Attributes', 1)
            addsheet(caller, 'Tech', 'Attributes', 1)
            addsheet(caller, 'Will', 'Attributes', 1)
            addsheet(caller, 'Presence', 'Attributes', 1)
            addsheet(caller, 'Observe', 'Skills', 1)
            addsheet(caller, 'Tech Redemption', 'Skills', 1)
            addsheet(caller, 'Self Control', 'Skills', 1)

    # Class
    elif which == 1:
        # Wealthy
        if what == 0:
            addsheet(caller, 'Presence', 'Attributes', 1)
            addsheet(caller, 'Etiquette', 'Skills', 1)

        # Middle
        elif what == 1:
            addsheet(caller, 'Will', 'Attributes', 1)
            addsheet(caller, 'Influence', 'Skills', 1)

        # poor
        elif what == 2:
            addsheet(caller, 'Faith', 'Attributes', 1)
            addsheet(caller, 'Survival', 'Skills', 1)
            

def apply_path_priest(caller, which, what, house):
    # Apprenticeship
    if which == 0:
        
        # Cathedral
        if what == 0:
            
            # Urth Orthodox
            if house == "Urth Orthodox":
                addsheet(caller, 'Wits', 'Attributes', 1)
                addsheet(caller, 'Presence', 'Attributes', 1)
                addsheet(caller, 'Will', 'Attributes', 1)
                addsheet(caller, 'Faith', 'Attributes', 2)
                addsheet(caller, 'Influence', 'Skills', 1)
                addsheet(caller, 'Investigation', 'Skills', 1)
                addsheet(caller, 'Self Control', 'Skills', 1)
                addsheet(caller, 'Physick', 'Skills', 2)
                addsheet(caller, 'Leadership', 'Skills', 1)
                addsheet(caller, 'Bureaucracy', 'Skills', 2)
                addsheet(caller, 'Latin', 'Languages', 0)
                addsheet(caller, 'Pious', 'Blessings', 0)
                addsheet(caller, 'Austere', 'Curses', 0)
                
            # Eskatonic
            elif house == "Eskatonic Order":
                addsheet(caller, 'Wits', 'Attributes', 1)
                addsheet(caller, 'Will', 'Attributes', 2)
                addsheet(caller, 'Faith', 'Attributes', 2)
                addsheet(caller, 'Observe', 'Skills', 2)
                addsheet(caller, 'Investigation', 'Skills', 2)
                addsheet(caller, 'Empathy', 'Skills', 1)
                addsheet(caller, 'Self Control', 'Skills', 3)
                addsheet(caller, 'Latin', 'Languages', 0)
                addsheet(caller, 'Curious', 'Blessings', 0)
                addsheet(caller, 'Subtle', 'Curses', 0)
                
            # Temple Avesti
            elif house == "Temple Avesti":
                addsheet(caller, 'Endurance', 'Attributes', 1)
                addsheet(caller, 'Perception', 'Attributes', 2)
                addsheet(caller, 'Faith', 'Attributes', 2)
                addsheet(caller, 'Influence', 'Skills', 1)
                addsheet(caller, 'Melee', 'Skills', 1)
                addsheet(caller, 'Observe', 'Skills', 2)
                addsheet(caller, 'Investigation', 'Skills', 1)
                addsheet(caller, 'Pious', 'Blessings', 0)
                addsheet(caller, 'Righteous', 'Curses', 0)
                
            # Sanctuary Aeon
            elif house == "Sanctuary Aeon":
                addsheet(caller, 'Dexterity', 'Attributes', 2)
                addsheet(caller, 'Tech', 'Attributes', 1)
                addsheet(caller, 'Will', 'Attributes', 1)
                addsheet(caller, 'Faith', 'Attributes', 1)
                addsheet(caller, 'Influence', 'Skills', 1)
                addsheet(caller, 'Empathy', 'Skills', 2)
                addsheet(caller, 'Life Science', 'Skills', 1)
                addsheet(caller, 'Physick', 'Skills', 4)
                addsheet(caller, 'Self Control', 'Skills', 1)
                addsheet(caller, 'Compassionate', 'Blessings', 0)
                addsheet(caller, 'Gullible', 'Curses', 0)
            
        # Parish
        elif what == 1:
            
            # Urth Orthodox
            if house == "Urth Orthodox":
                addsheet(caller, 'Wits', 'Attributes', 1)
                addsheet(caller, 'Presence', 'Attributes', 1)
                addsheet(caller, 'Will', 'Attributes', 1)
                addsheet(caller, 'Faith', 'Attributes', 2)
                addsheet(caller, 'Influence', 'Skills', 1)
                addsheet(caller, 'Empathy', 'Skills', 1)
                addsheet(caller, 'Self Control', 'Skills', 1)
                addsheet(caller, 'Leadership', 'Skills', 1)
                addsheet(caller, 'Physick', 'Skills', 2)
                addsheet(caller, 'Bureaucracy', 'Skills', 2)
                addsheet(caller, 'Pious', 'Blessings', 0)
                addsheet(caller, 'Auster', 'Curses', 0)
                
            # Eskatonic
            elif house == "Eskatonic Order":
                addsheet(caller, 'Wits', 'Attributes', 1)
                addsheet(caller, 'Will', 'Attributes', 2)
                addsheet(caller, 'Faith', 'Attributes', 2)
                addsheet(caller, 'Observe', 'Skills', 1)
                addsheet(caller, 'Empathy', 'Skills', 1)
                addsheet(caller, 'Physick', 'Skills', 2)
                addsheet(caller, 'Self Control', 'Skills', 3)
                addsheet(caller, 'Curious', 'Blessings', 0)
                addsheet(caller, 'Subtle', 'Curses', 0)
                
            # Temple Avesti
            elif house == "Temple Avesti":
                addsheet(caller, 'Endurance', 'Attributes', 1)
                addsheet(caller, 'Perception', 'Attributes', 2)
                addsheet(caller, 'Faith', 'Attributes', 2)
                addsheet(caller, 'Influence', 'Skills', 1)
                addsheet(caller, 'Melee', 'Skills', 1)
                addsheet(caller, 'Observe', 'Skills', 2)
                addsheet(caller, 'Investigation', 'Skills', 1)
                addsheet(caller, 'Pious', 'Blessings', 0)
                addsheet(caller, 'Righteous', 'Curses', 0)
                
            # Sanctuary Aeon
            elif house == "Sanctuary Aeon":
                addsheet(caller, 'Dexterity', 'Attributes', 2)
                addsheet(caller, 'Will', 'Attributes', 1)
                addsheet(caller, 'Faith', 'Attributes', 2)
                addsheet(caller, 'Influence', 'Skills', 1)
                addsheet(caller, 'Arts', 'Skills', 1)
                addsheet(caller, 'Empathy', 'Skills', 2)
                addsheet(caller, 'Life Science', 'Skills', 1)
                addsheet(caller, 'Physick', 'Skills', 3)
                addsheet(caller, 'Self Control', 'Skills', 2)
                addsheet(caller, 'Compassionate', 'Blessings', 0)
                addsheet(caller, 'Gullible', 'Curses', 0)
            
        # Monastery
        elif what == 2:
            
            # Urth Orthodox
            if house == "Urth Orthodox":
                addsheet(caller, 'Wits', 'Attributes', 1)
                addsheet(caller, 'Presence', 'Attributes', 1)
                addsheet(caller, 'Will', 'Attributes', 1)
                addsheet(caller, 'Faith', 'Attributes', 2)
                addsheet(caller, 'Investigation', 'Skills', 2)
                addsheet(caller, 'Bureaucracy', 'Skills', 1)
                addsheet(caller, 'Physick', 'Skills', 1)
                addsheet(caller, 'Communication', 'Skills', 1)
                addsheet(caller, 'Self Control', 'Skills', 3)
                addsheet(caller, 'Latin', 'Languages', 0)
                addsheet(caller, 'Pious', 'Blessings', 0)
                addsheet(caller, 'Auster', 'Curses', 0)
                
            # Eskatonic
            elif house == "Eskatonic Order":
                addsheet(caller, 'Wits', 'Attributes', 1)
                addsheet(caller, 'Will', 'Attributes', 2)
                addsheet(caller, 'Faith', 'Attributes', 2)
                addsheet(caller, 'Investigation', 'Skills', 3)
                addsheet(caller, 'Self Control', 'Skills', 3)
                addsheet(caller, 'Latin', 'Languages', 0)
                addsheet(caller, 'Curious', 'Blessings', 0)
                addsheet(caller, 'Subtle', 'Curses', 0)
                
            # Temple Avesti
            elif house == "Temple Avesti":
                addsheet(caller, 'Endurance', 'Attributes', 1)
                addsheet(caller, 'Perception', 'Attributes', 2)
                addsheet(caller, 'Faith', 'Attributes', 2)
                addsheet(caller, 'Influence', 'Skills', 1)
                addsheet(caller, 'Melee', 'Skills', 1)
                addsheet(caller, 'Observe', 'Skills', 2)
                addsheet(caller, 'Investigation', 'Skills', 1)
                addsheet(caller, 'Pious', 'Blessings', 0)
                addsheet(caller, 'Righteous', 'Curses', 0)
                
            # Sanctuary Aeon
            elif house == "Sanctuary Aeon":
                addsheet(caller, 'Dexterity', 'Attributes', 1)
                addsheet(caller, 'Presence', 'Attributes', 1)
                addsheet(caller, 'Will', 'Attributes', 1)
                addsheet(caller, 'Faith', 'Attributes', 2)
                addsheet(caller, 'Empathy', 'Skills', 1)
                addsheet(caller, 'Life Science', 'Skills', 1)
                addsheet(caller, 'Physick', 'Skills', 3)
                addsheet(caller, 'Influence', 'Skills', 1)
                addsheet(caller, 'Self Control', 'Skills', 2)
                addsheet(caller, 'Latin', 'Languages', 0)
                addsheet(caller, 'Compassionate', 'Blessings', 0)
                addsheet(caller, 'Gullible', 'Curses', 0)
            
    # Early Career
    elif which == 1:
        
        # Preacher Pastor
        if what == 0:
            addsheet(caller, 'Wits', 'Attributes', 2)
            addsheet(caller, 'Perception', 'Attributes', 1)
            addsheet(caller, 'Presence', 'Attributes', 2)
            addsheet(caller, 'Will', 'Attributes', 2)
            addsheet(caller, 'Faith', 'Attributes', 3)
            addsheet(caller, 'Influence', 'Skills', 2)
            addsheet(caller, 'Observe', 'Skills', 2)
            addsheet(caller, 'Empathy', 'Skills', 2)
            addsheet(caller, 'Self Control', 'Skills', 2)
            addsheet(caller, 'Investigation', 'Skills', 2)
            addsheet(caller, 'Bureaucracy', 'Skills', 1)
            addsheet(caller, 'Physick', 'Skills', 2)
            addsheet(caller, 'Communication', 'Skills', 2)
            caller.db.benefices['Rank'] = 'Novitiate'
            
        # Monk
        elif what == 1:
            addsheet(caller, 'Wits', 'Attributes', 2)
            addsheet(caller, 'Perception', 'Attributes', 1)
            addsheet(caller, 'Presence', 'Attributes', 2)
            addsheet(caller, 'Will', 'Attributes', 2)
            addsheet(caller, 'Faith', 'Attributes', 2)
            addsheet(caller, 'Observe', 'Skills', 2)
            addsheet(caller, 'Investigation', 'Skills', 2)
            addsheet(caller, 'Empathy', 'Skills', 2)
            addsheet(caller, 'Self Control', 'Skills', 3)
            addsheet(caller, 'Vigor', 'Skills', 1)
            addsheet(caller, 'Physick', 'Skills', 1)
            addsheet(caller, 'Survival', 'Skills', 2)
            caller.db.benefices['Rank'] = 'Novitiate'
            
        # Missionary
        elif what == 2:
            addsheet(caller, 'Endurance', 'Attributes', 2)
            addsheet(caller, 'Wits', 'Attributes', 1)
            addsheet(caller, 'Perception', 'Attributes', 2)
            addsheet(caller, 'Presence', 'Attributes', 2)
            addsheet(caller, 'Will', 'Attributes', 1)
            addsheet(caller, 'Faith', 'Attributes', 2)
            addsheet(caller, 'Influence', 'Skills', 3)
            addsheet(caller, 'Observe', 'Skills', 1)
            addsheet(caller, 'Empathy', 'Skills', 1)
            addsheet(caller, 'Self Control', 'Skills', 1)
            addsheet(caller, 'Investigation', 'Skills', 1)
            addsheet(caller, 'Vigor', 'Skills', 1)
            addsheet(caller, 'Physick', 'Skills', 2)
            addsheet(caller, 'Survival', 'Skills', 2)
            addsheet(caller, 'Communication', 'Skills', 2)
            caller.db.benefices['Rank'] = 'Novitiate'
            
        # Healer
        elif what == 3:
            addsheet(caller, 'Dexterity', 'Attributes', 2)
            addsheet(caller, 'Endurance', 'Attributes', 1)
            addsheet(caller, 'Wits', 'Attributes', 1)
            addsheet(caller, 'Tech', 'Attributes', 1)
            addsheet(caller, 'Presence', 'Attributes', 2)
            addsheet(caller, 'Will', 'Attributes', 1)
            addsheet(caller, 'Faith', 'Attributes', 2)
            addsheet(caller, 'Influence', 'Skills', 2)
            addsheet(caller, 'Observe', 'Skills', 1)
            addsheet(caller, 'Empathy', 'Skills', 2)
            addsheet(caller, 'Self Control', 'Skills', 1)
            addsheet(caller, 'Life Science', 'Skills', 1)
            addsheet(caller, 'Physick', 'Skills', 4)
            addsheet(caller, 'Communication', 'Skills', 2)
            addsheet(caller, 'Tech Redemption', 'Skills', 2)
            caller.db.benefices['Rank'] = 'Novitiate'
            
        # Inquisitor
        elif what == 4:
            addsheet(caller, 'Strength', 'Attributes', 2)
            addsheet(caller, 'Dexterity', 'Attributes', 1)
            addsheet(caller, 'Endurance', 'Attributes', 2)
            addsheet(caller, 'Perception', 'Attributes', 2)
            addsheet(caller, 'Will', 'Attributes', 2)
            addsheet(caller, 'Faith', 'Attributes', 1)
            addsheet(caller, 'Influence', 'Skills', 2)
            addsheet(caller, 'Observe', 'Skills', 2)
            addsheet(caller, 'Sneak', 'Skills', 1)
            addsheet(caller, 'Vigor', 'Skills', 1)
            addsheet(caller, 'Investigation', 'Skills', 2)
            addsheet(caller, 'Bureaucracy', 'Skills', 1)
            addsheet(caller, 'Self Control', 'Skills', 1)
            addsheet(caller, 'Survival', 'Skills', 1)
            caller.db.benefices['Rank'] = 'Novitiate'
            
            
def apply_path_guild(caller, which, what, house):
    # Apprenticeship
    if which == 0:
        
        # Academy
        if what == 0:
    
            # Charioteers
            if house == 'Charioteers':
                addsheet(caller, 'Dexterity', 'Attributes', 2)
                addsheet(caller, 'Wits', 'Attributes', 1)
                addsheet(caller, 'Presence', 'Attributes', 2)
                addsheet(caller, 'Influence', 'Skills', 2)
                addsheet(caller, 'Spacecraft Operations', 'Skills', 2)
                addsheet(caller, 'Tech Redemption', 'Skills', 2)
                addsheet(caller, 'Physick', 'Skills', 1)
                addsheet(caller, 'Curious', 'Blessings', 0)
                addsheet(caller, 'Nosy', 'Blessings', 0)
                
            # Engineers
            elif house == 'Engineers':
                addsheet(caller, 'Dexterity', 'Attributes', 1)
                addsheet(caller, 'Wits', 'Attributes', 1)
                addsheet(caller, 'Tech', 'Attributes', 3)
                addsheet(caller, 'Investigation', 'Skills', 1)
                addsheet(caller, 'Tech Redemption', 'Skills', 4)
                addsheet(caller, 'Think Machine', 'Skills', 2)
                addsheet(caller, 'Urthtech', 'Languages', 0)
                addsheet(caller, 'Innovative', 'Blessings', 0)
                addsheet(caller, 'Unnerving', 'Blessings', 0)
                
            # Scravers
            elif house == 'Scravers':
                addsheet(caller, 'Strength', 'Attributes', 2)
                addsheet(caller, 'Perception', 'Attributes', 2)
                addsheet(caller, 'Will', 'Attributes', 1)
                addsheet(caller, 'Influence', 'Skills', 1)
                addsheet(caller, 'Sneak', 'Skills', 1)
                addsheet(caller, 'Gaming', 'Skills', 1)
                addsheet(caller, 'Investigation', 'Skills', 1)
                addsheet(caller, 'Scravers Cant', 'Languages', 0)
                addsheet(caller, 'The Man', 'Blessings', 0)
                addsheet(caller, 'Possessive', 'Blessings', 0)
                
            # Muster
            elif house == 'Muster':
                addsheet(caller, 'Strength', 'Attributes', 1)
                addsheet(caller, 'Dexterity', 'Attributes', 2)
                addsheet(caller, 'Tech', 'Attributes', 2)
                addsheet(caller, 'Influence', 'Skills', 1)
                addsheet(caller, 'Observe', 'Skills', 1)
                addsheet(caller, 'Tech Redemption', 'Skills', 1)
                addsheet(caller, 'Physick', 'Skills', 1)
                addsheet(caller, 'Bold', 'Blessings', 0)
                addsheet(caller, 'Callous', 'Blessings', 0)
                
            # Reeves
            elif house == 'Reeves':
                addsheet(caller, 'Wits', 'Attributes', 2)
                addsheet(caller, 'Perception', 'Attributes', 2)
                addsheet(caller, 'Will', 'Attributes', 1)
                addsheet(caller, 'Influence', 'Skills', 1)
                addsheet(caller, 'Investigation', 'Skills', 2)
                addsheet(caller, 'Bureaucracy', 'Skills', 3)
                addsheet(caller, 'Etiquette', 'Skills', 1)
                addsheet(caller, 'Leadership', 'Skills', 1)
                addsheet(caller, 'Latin', 'Languages', 0)
                addsheet(caller, 'Shrewd', 'Blessings', 0)
                addsheet(caller, 'Mammon', 'Blessings', 0)
                
        # Guild Hall
        elif what == 1:
            
            # Charioteers
            if house == 'Charioteers':
                addsheet(caller, 'Dexterity', 'Attributes', 2)
                addsheet(caller, 'Wits', 'Attributes', 1)
                addsheet(caller, 'Presence', 'Attributes', 2)
                addsheet(caller, 'Influence', 'Skills', 1)
                addsheet(caller, 'Empathy', 'Skills', 1)
                addsheet(caller, 'Tech Redemption', 'Skills', 1)
                addsheet(caller, 'Physick', 'Skills', 1)
                addsheet(caller, 'Curious', 'Blessings', 0)
                addsheet(caller, 'Nosy', 'Blessings', 0)
                
            # Engineers
            elif house == 'Engineers':
                addsheet(caller, 'Dexterity', 'Attributes', 1)
                addsheet(caller, 'Wits', 'Attributes', 1)
                addsheet(caller, 'Tech', 'Attributes', 3)
                addsheet(caller, 'Investigation', 'Skills', 1)
                addsheet(caller, 'Tech Redemption', 'Skills', 3)
                addsheet(caller, 'Think Machine', 'Skills', 1)
                addsheet(caller, 'Urthtech', 'Languages', 0)
                addsheet(caller, 'Innovative', 'Blessings', 0)
                addsheet(caller, 'Unnerving', 'Blessings', 0)
                
            # Scravers
            elif house == 'Scravers':
                addsheet(caller, 'Strength', 'Attributes', 2)
                addsheet(caller, 'Perception', 'Attributes', 2)
                addsheet(caller, 'Will', 'Attributes', 1)
                addsheet(caller, 'Influence', 'Skills', 1)
                addsheet(caller, 'Vigor', 'Skills', 1)
                addsheet(caller, 'Sneak', 'Skills', 1)
                addsheet(caller, 'Gaming', 'Skills', 1)
                addsheet(caller, 'Investigation', 'Skills', 1)
                addsheet(caller, 'Scravers Cant', 'Languages', 0)
                addsheet(caller, 'The Man', 'Blessings', 0)
                addsheet(caller, 'Possessive', 'Blessings', 0)
                
            # Muster
            elif house == 'Muster':
                addsheet(caller, 'Strength', 'Attributes', 1)
                addsheet(caller, 'Dexterity', 'Attributes', 2)
                addsheet(caller, 'Tech', 'Attributes', 2)
                addsheet(caller, 'Influence', 'Skills', 1)
                addsheet(caller, 'Tech Redemption', 'Skills', 1)
                addsheet(caller, 'Physick', 'Skills', 1)
                addsheet(caller, 'Observe', 'Skills', 1)
                addsheet(caller, 'Bold', 'Blessings', 0)
                addsheet(caller, 'Callous', 'Blessings', 0)
                
            # Reeves
            elif house == 'Reeves':
                addsheet(caller, 'Wits', 'Attributes', 2)
                addsheet(caller, 'Perception', 'Attributes', 2)
                addsheet(caller, 'Will', 'Attributes', 1)
                addsheet(caller, 'Influence', 'Skills', 1)
                addsheet(caller, 'Observe', 'Skills', 1)
                addsheet(caller, 'Bureaucracy', 'Skills', 2)
                addsheet(caller, 'Etiquette', 'Skills', 1)
                addsheet(caller, 'Investigation', 'Skills', 2)
                addsheet(caller, 'Leadership', 'Skills', 1)
                addsheet(caller, 'Latin', 'Languages', 0)
                addsheet(caller, 'Shrewd', 'Blessings', 0)
                addsheet(caller, 'Mammon', 'Blessings', 0)
                
        # Streets
        elif what == 2:
            
            # Charioteers
            if house == 'Charioteers':
                addsheet(caller, 'Dexterity', 'Attributes', 2)
                addsheet(caller, 'Wits', 'Attributes', 1)
                addsheet(caller, 'Presence', 'Attributes', 2)
                addsheet(caller, 'Influence', 'Skills', 1)
                addsheet(caller, 'Tech Redemption', 'Skills', 1)
                addsheet(caller, 'Physick', 'Skills', 1)
                addsheet(caller, 'Latin', 'Languages', 0)
                addsheet(caller, 'Curious', 'Blessings', 0)
                addsheet(caller, 'Nosy', 'Blessings', 0)
                
            # Engineers
            elif house == 'Engineers':
                addsheet(caller, 'Dexterity', 'Attributes', 2)
                addsheet(caller, 'Wits', 'Attributes', 1)
                addsheet(caller, 'Tech', 'Attributes', 2)
                addsheet(caller, 'Investigation', 'Skills', 1)
                addsheet(caller, 'Tech Redemption', 'Skills', 2)
                addsheet(caller, 'Think Machine', 'Skills', 1)
                addsheet(caller, 'Urthtech', 'Languages', 0)
                addsheet(caller, 'Innovative', 'Blessings', 0)
                addsheet(caller, 'Unnerving', 'Blessings', 0)
                
            # Scravers
            elif house == 'Scravers':
                addsheet(caller, 'Strength', 'Attributes', 2)
                addsheet(caller, 'Dexterity', 'Attributes', 1)
                addsheet(caller, 'Perception', 'Attributes', 2)
                addsheet(caller, 'Influence', 'Skills', 1)
                addsheet(caller, 'Gaming', 'Skills', 1)
                addsheet(caller, 'Vigor', 'Skills', 1)
                addsheet(caller, 'Scravers Cant', 'Languages', 0)
                addsheet(caller, 'The Man', 'Blessings', 0)
                addsheet(caller, 'Possessive', 'Blessings', 0)
                
            # Muster
            elif house == 'Muster':
                addsheet(caller, 'Strength', 'Attributes', 2)
                addsheet(caller, 'Dexterity', 'Attributes', 2)
                addsheet(caller, 'Tech', 'Attributes', 1)
                addsheet(caller, 'Influence', 'Skills', 1)
                addsheet(caller, 'Physick', 'Skills', 1)
                addsheet(caller, 'Observe', 'Skills', 2)
                addsheet(caller, 'Survival', 'Skills', 1)
                addsheet(caller, 'Bold', 'Blessings', 0)
                addsheet(caller, 'Callous', 'Blessings', 0)
                
            # Reeves
            elif house == 'Reeves':
                addsheet(caller, 'Dexterity', 'Attributes', 1)
                addsheet(caller, 'Wits', 'Attributes', 2)
                addsheet(caller, 'Perception', 'Attributes', 2)
                addsheet(caller, 'Influence', 'Skills', 1)
                addsheet(caller, 'Observe', 'Skills', 1)
                addsheet(caller, 'Sneak', 'Skills', 1)
                addsheet(caller, 'Investigation', 'Skills', 1)
                addsheet(caller, 'Etiquette', 'Skills', 1)
                addsheet(caller, 'Bureaucracy', 'Skills', 2)
                addsheet(caller, 'Leadership', 'Skills', 1)
                addsheet(caller, 'Shrewd', 'Blessings', 0)
                addsheet(caller, 'Mammon', 'Blessings', 0)
                
    # Early Career
    elif which == 1:
        
        # Merchant
        if what == 0:
            addsheet(caller, 'Dexterity', 'Attributes', 1)
            addsheet(caller, 'Endurance', 'Attributes', 1)
            addsheet(caller, 'Wits', 'Attributes', 2)
            addsheet(caller, 'Perception', 'Attributes', 2)
            addsheet(caller, 'Presence', 'Attributes', 2)
            addsheet(caller, 'Will', 'Attributes', 2)
            addsheet(caller, 'Influence', 'Skills', 2)
            addsheet(caller, 'Observe', 'Skills', 2)
            addsheet(caller, 'Gaming', 'Skills', 1)
            addsheet(caller, 'Investigation', 'Skills', 2)
            addsheet(caller, 'Sneak', 'Skills', 1)
            caller.db.benefices['Rank'] = 'Associate'
            
        # Money-Lender
        elif what == 1:
            addsheet(caller, 'Dexterity', 'Attributes', 1)
            addsheet(caller, 'Endurance', 'Attributes', 1)
            addsheet(caller, 'Wits', 'Attributes', 2)
            addsheet(caller, 'Perception', 'Attributes', 2)
            addsheet(caller, 'Presence', 'Attributes', 2)
            addsheet(caller, 'Will', 'Attributes', 2)
            addsheet(caller, 'Bureaucracy', 'Skills', 2)
            addsheet(caller, 'Etiquette', 'Skills', 1)
            addsheet(caller, 'Influence', 'Skills', 2)
            addsheet(caller, 'Observe', 'Skills', 2)
            addsheet(caller, 'Gaming', 'Skills', 1)
            addsheet(caller, 'Investigation', 'Skills', 2)
            caller.db.benefices['Rank'] = 'Associate'
            
        # Pilot
        elif what == 2:
            addsheet(caller, 'Dexterity', 'Attributes', 2)
            addsheet(caller, 'Endurance', 'Attributes', 1)
            addsheet(caller, 'Wits', 'Attributes', 2)
            addsheet(caller, 'Perception', 'Attributes', 1)
            addsheet(caller, 'Tech', 'Attributes', 2)
            addsheet(caller, 'Will', 'Attributes', 2)
            addsheet(caller, 'Influence', 'Skills', 1)
            addsheet(caller, 'Spacecraft Operations', 'Skills', 2)
            addsheet(caller, 'Physick', 'Skills', 1)
            addsheet(caller, 'Tech Redemption', 'Skills', 2)
            addsheet(caller, 'Think Machine', 'Skills', 2)
            addsheet(caller, 'Warfare', 'Skills', 1)
            caller.db.benefices['Rank'] = 'Associate'
            
        # Engineer
        elif what == 3:
            addsheet(caller, 'Dexterity', 'Attributes', 2)
            addsheet(caller, 'Endurance', 'Attributes', 1)
            addsheet(caller, 'Wits', 'Attributes', 2)
            addsheet(caller, 'Perception', 'Attributes', 1)
            addsheet(caller, 'Tech', 'Attributes', 2)
            addsheet(caller, 'Will', 'Attributes', 2)
            addsheet(caller, 'Influence', 'Skills', 1)
            addsheet(caller, 'Spacecraft Operations', 'Skills', 1)
            addsheet(caller, 'Physick', 'Skills', 1)
            addsheet(caller, 'Tech Redemption', 'Skills', 3)
            addsheet(caller, 'Think Machine', 'Skills', 3)
            addsheet(caller, 'Warfare', 'Skills', 1)
            caller.db.benefices['Rank'] = 'Associate'
            
        # gunner
        elif what == 4:
            addsheet(caller, 'Dexterity', 'Attributes', 2)
            addsheet(caller, 'Endurance', 'Attributes', 1)
            addsheet(caller, 'Wits', 'Attributes', 2)
            addsheet(caller, 'Perception', 'Attributes', 1)
            addsheet(caller, 'Tech', 'Attributes', 2)
            addsheet(caller, 'Will', 'Attributes', 2)
            addsheet(caller, 'Gambling', 'Skills', 1)
            addsheet(caller, 'Gunnery', 'Skills', 2)
            addsheet(caller, 'Influence', 'Skills', 1)
            addsheet(caller, 'Spacecraft Operations', 'Skills', 1)
            addsheet(caller, 'Physick', 'Skills', 1)
            addsheet(caller, 'Tech Redemption', 'Skills', 2)
            addsheet(caller, 'Think Machine', 'Skills', 2)
            addsheet(caller, 'Warfare', 'Skills', 1)
            caller.db.benefices['Rank'] = 'Associate'
            
        # Soldier
        elif what == 5:
            addsheet(caller, 'Strength', 'Attributes', 2)
            addsheet(caller, 'Dexterity', 'Attributes', 3)
            addsheet(caller, 'Endurance', 'Attributes', 2)
            addsheet(caller, 'Tech', 'Attributes', 1)
            addsheet(caller, 'Will', 'Attributes', 2)
            addsheet(caller, 'Influence', 'Skills', 1)
            addsheet(caller, 'Vigor', 'Skills', 2)
            addsheet(caller, 'Tech Redemption', 'Skills', 1)
            addsheet(caller, 'Physick', 'Skills', 1)
            addsheet(caller, 'Survival', 'Skills', 2)
            caller.db.benefices['Rank'] = 'Associate'
            
        # Combat Engineer
        elif what == 6:
            addsheet(caller, 'Strength', 'Attributes', 1)
            addsheet(caller, 'Dexterity', 'Attributes', 2)
            addsheet(caller, 'Endurance', 'Attributes', 2)
            addsheet(caller, 'Wits', 'Attributes', 1)
            addsheet(caller, 'Perception', 'Attributes', 1)
            addsheet(caller, 'Tech', 'Attributes', 2)
            addsheet(caller, 'Will', 'Attributes', 1)
            addsheet(caller, 'Observe', 'Skills', 1)
            addsheet(caller, 'Physick', 'Skills', 1)
            addsheet(caller, 'Tech Redemption', 'Skills', 3)
            addsheet(caller, 'Science', 'Skills', 2)
            addsheet(caller, 'Warfare', 'Skills', 3)
            caller.db.benefices['Rank'] = 'Associate'
            
        # Scholar
        elif what == 7:
            addsheet(caller, 'Wits', 'Attributes', 2)
            addsheet(caller, 'Perception', 'Attributes', 2)
            addsheet(caller, 'Tech', 'Attributes', 1)
            addsheet(caller, 'Presence', 'Attributes', 2)
            addsheet(caller, 'Will', 'Attributes', 2)
            addsheet(caller, 'Faith', 'Attributes', 1)
            addsheet(caller, 'Influence', 'Skills', 1)
            addsheet(caller, 'Observe', 'Skills', 1)
            addsheet(caller, 'Investigation', 'Skills', 3)
            addsheet(caller, 'Etiquette', 'Skills', 1)
            addsheet(caller, 'Self Control', 'Skills', 2)
            addsheet(caller, 'Leadership', 'Skills', 1)
            addsheet(caller, 'Think Machine', 'Skills', 1)
            caller.db.benefices['Rank'] = 'Associate'
            
        # Scientist
        elif what == 8:
            addsheet(caller, 'Wits', 'Attributes', 3)
            addsheet(caller, 'Perception', 'Attributes', 2)
            addsheet(caller, 'Tech', 'Attributes', 2)
            addsheet(caller, 'Will', 'Attributes', 2)
            addsheet(caller, 'Presence', 'Attributes', 1)
            addsheet(caller, 'Influence', 'Skills', 1)
            addsheet(caller, 'Investigation', 'Skills', 2)
            addsheet(caller, 'Tech Redemption', 'Skills', 3)
            addsheet(caller, 'Think Machine', 'Skills', 3)
            addsheet(caller, 'Urthtech', 'Languages', 0)
            caller.db.benefices['Rank'] = 'Associate'
            
        # Thief
        elif what == 9:
            addsheet(caller, 'Strength', 'Attributes', 2)
            addsheet(caller, 'Dexterity', 'Attributes', 2)
            addsheet(caller, 'Endurance', 'Attributes', 2)
            addsheet(caller, 'Perception', 'Attributes', 2)
            addsheet(caller, 'Will', 'Attributes', 2)
            addsheet(caller, 'Influence', 'Skills', 1)
            addsheet(caller, 'Vigor', 'Skills', 1)
            addsheet(caller, 'Gaming', 'Skills', 1)
            addsheet(caller, 'Investigation', 'Skills', 1)
            addsheet(caller, 'Observe', 'Skills', 1)
            addsheet(caller, 'Sneak', 'Skills', 2)
            caller.db.benefices['Rank'] = 'Associate'
            
        # Spy
        elif what == 10:
            addsheet(caller, 'Strength', 'Attributes', 2)
            addsheet(caller, 'Dexterity', 'Attributes', 2)
            addsheet(caller, 'Endurance', 'Attributes', 2)
            addsheet(caller, 'Perception', 'Attributes', 2)
            addsheet(caller, 'Presence', 'Attributes', 2)
            addsheet(caller, 'Vigor', 'Skills', 1)
            addsheet(caller, 'Gaming', 'Skills', 1)
            addsheet(caller, 'Influence', 'Skills', 2)
            addsheet(caller, 'Investigation', 'Skills', 1)
            addsheet(caller, 'Observe', 'Skills', 2)
            addsheet(caller, 'Sneak', 'Skills', 1)
            caller.db.benefices['Rank'] = 'Associate'
            

def menunode_start(caller):
    text = "Beginning Fading Suns Character Generation. You will be able to execute other commands.\n"
    text += "You can exit early but will have to start over. Select your character's path."
    options = ({"desc": "Lifepath CG", "goto": "menunode_lifepath"}, {"desc": "Custom CG", "goto": "menunode_custom"})
    return text, options


def menunode_lifepath(caller):
    text = "Lifepath CG Beginning. This CG module uses the Lifepaths as described in FAS21901 the 2014 supplement to revised. It is free online.\n"
    text += "Please begin by selecting an archetype."
    options = ({"desc": "Nobles", "goto": "menunode_lpn1"}, {"desc": "Priests", "goto": "menunode_lpp1"},
               {"desc": "Merchants AKA Guild", "goto": "menunode_lpm1"})
    return text, options

#  Begin Noble Section
def menunode_lpn1(caller):
    caller.db.archetype = "Noble"
    caller.db.noble = 1
    caller.db.recbenefices = ('Nobility', 'Riches')
    text = "As nobility, your first step is picking a house. Please pick one.\n"
    text += "Please note that houses after al-Malik are book defined minor houses.\n"
    text += "If you are going to use minor house and not follow an existing house, use custom cg.\n"
    text += "If you want to name your own minor house, type that name here.\n"
    options = ({"key": "0", "desc": "Hawkwood", "goto": "menunode_lpn2"},
               {"key": "1", "desc": "Decados", "goto": "menunode_lpn2"},
               {"key": "2", "desc": "Hazat", "goto": "menunode_lpn2"},
               {"key": "3", "desc": "Li Halan", "goto": "menunode_lpn2"},
               {"key": "4", "desc": "al-Malik", "goto": "menunode_lpn2"},
               {"key": "5", "desc": "Alba", "goto": "menunode_lpn2"},
               {"key": "6", "desc": "Juandaastas", "goto": "menunode_lpn2"},
               {"key": "7", "desc": "Justinian", "goto": "menunode_lpn2"},
               {"key": "8", "desc": "Keddah", "goto": "menunode_lpn2"},
               {"key": "9", "desc": "Masseri", "goto": "menunode_lpn2"},
               {"key": "10", "desc": "Shelit", "goto": "menunode_lpn2"},
               {"key": "11", "desc": "Thana", "goto": "menunode_lpn2"},
               {"key": "12", "desc": "Torenson", "goto": "menunode_lpn2"},
               {"key": "13", "desc": "Trusnikron", "goto": "menunode_lpn2"},
               {"key": "14", "desc": "Van Gelder", "goto": "menunode_lpn2"},
               {"key": "15", "desc": "Xanthippe", "goto": "menunode_lpn2"},
               {"key": "16", "desc": "Questing Knight", "goto": "menunode_lpn2"},
               {"Key": "_default", "goto": "menunode_lpn2"})


def menunode_lpn2(caller, raw_input):
    if int(raw_input) == 16:
        caller.db.questing = 1
        text = "You selected questing knight. Please select your noble house.\n"
        text ++ "If you want to enter a custom minor house you can do that here too."
        options = ({"key": "0", "desc": "Hawkwood", "goto": "menunode_lpn2"},
               {"key": "1", "desc": "Decados", "goto": "menunode_lpnq"},
               {"key": "2", "desc": "Hazat", "goto": "menunode_lpnq"},
               {"key": "3", "desc": "Li Halan", "goto": "menunode_lpnq"},
               {"key": "4", "desc": "al-Malik", "goto": "menunode_lpnq"},
               {"key": "5", "desc": "Alba", "goto": "menunode_lpnq"},
               {"key": "6", "desc": "Juandaastas", "goto": "menunode_lpnq"},
               {"key": "7", "desc": "Justinian", "goto": "menunode_lpnq"},
               {"key": "8", "desc": "Keddah", "goto": "menunode_lpnq"},
               {"key": "9", "desc": "Masseri", "goto": "menunode_lpnq"},
               {"key": "10", "desc": "Shelit", "goto": "menunode_lpnq"},
               {"key": "11", "desc": "Thana", "goto": "menunode_lpnq"},
               {"key": "12", "desc": "Torenson", "goto": "menunode_lpnq"},
               {"key": "13", "desc": "Trusnikron", "goto": "menunode_lpnq"},
               {"key": "14", "desc": "Van Gelder", "goto": "menunode_lpnq"},
               {"key": "15", "desc": "Xanthippe", "goto": "menunode_lpnq"},
               {"Key": "_default", "goto": "menunode_lpnq"})
        return text, options
    elif 15 >= int(raw_input) >= 5 :
        caller.db.minor = 1
        caller.db.house = househelper[raw_input]
        addsheet(pc, 'Faction Lore: ' + househelper[raw_input], 'Skills', 3)
        text = "Which existing house are you mirroring?"
        options = ({"key": "0", "desc": "Hawkwood", "goto": "menunode_lpnmh"},
                   {"key": "1", "desc": "Decados", "goto": "menunode_lpnmh"},
                   {"key": "2", "desc": "Hazat", "goto": "menunode_lpnmh"},
                   {"key": "3", "desc": "Li Halan", "goto": "menunode_lpnmh"},
                   {"key": "4", "desc": "al-Malik", "goto": "menunode_lpnmh"},
                   {"key": "5", "desc": "Questing Knight", "goto": "menunode_lpnmh"})
        return text, options
    else not raw_input.isdigit():
        caller.db.minor = 1
        caller.db.house = raw_input
        addsheet(pc, 'Faction Lore: ' + raw_input, 'Skills', 3)
        text = "Which existing house are you mirroring?"
        options = ({"key": "0", "desc": "Hawkwood", "goto": "menunode_lpnmh"},
                   {"key": "1", "desc": "Decados", "goto": "menunode_lpnmh"},
                   {"key": "2", "desc": "Hazat", "goto": "menunode_lpnmh"},
                   {"key": "3", "desc": "Li Halan", "goto": "menunode_lpnmh"},
                   {"key": "4", "desc": "al-Malik", "goto": "menunode_lpnmh"},
                   {"key": "5", "desc": "Questing Knight", "goto": "menunode_lpnmh"})

    if int(raw_input) == 3:
        caller.db.recbenefices.append('Church Ally')
    elif int(raw_input) == 4:
        caller.db.recbenefices.append('Passage Contract')

    caller.db.house = househelper[raw_input]
    addsheet(pc, 'Faction Lore: ' + househelper[raw_input], 'Skills', 3)

    text = "At this point you select your upbringing. Depending on your house you will gain various bonuses."
    options = ({"key": "0", "desc": "High Court", "goto": "menunode_lpn3"},
               {"key": "1", "desc": "Rural Estate", "goto": "menunode_lpn3"},
               {"key": "2", "desc": "Landless", "goto": "menunode_lpn3"})
    return text, options


def menunode_lpnmh(caller, raw_input):
    if int(raw_input) == 5:
        caller.db.questing = 1
        text = "You selected questing knight. Please select the noble house you intend to mirror for bonuses."
        options = ({"key": "0", "desc": "Hawkwood", "goto": "menunode_lpnq"},
               {"key": "1", "desc": "Decados", "goto": "menunode_lpnq"},
               {"key": "2", "desc": "Hazat", "goto": "menunode_lpnq"},
               {"key": "3", "desc": "Li Halan", "goto": "menunode_lpnq"},
               {"key": "4", "desc": "al-Malik", "goto": "menunode_lpnq"})
        return text, options

    caller.db.mirrorhouse = househelper[raw_input]

    if int(raw_input) == 3:
        caller.db.recbenefices.append('Church Ally')
    elif int(raw_input) == 4:
        caller.db.recbenefices.append('Passage Contract')

    text = "At this point you select your upbringing. Depending on your house you will gain various bonuses."
    options = ({"key": "0", "desc": "High Court", "goto": "menunode_lpn3"},
               {"key": "1", "desc": "Rural Estate", "goto": "menunode_lpn3"},
               {"key": "2", "desc": "Landless", "goto": "menunode_lpn3"})
    return text, options


def menunode_lpnq(caller, raw_input):
    if caller.db.minor == 1:
        caller.db.mirrorhouse = househelper[raw_input]
    elif int(raw_input) <= 4:
        caller.db.house = househelper[raw_input]
        addsheet(pc, 'Faction Lore: ' + househelper[raw_input], 'Skills', 3)
    elif 15 >= int(raw_input) >= 5:
        caller.db.minor = 1
        caller.db.house = househelper[raw_input]
        addsheet(pc, 'Faction Lore: ' + househelper[raw_input], 'Skills', 3)
        text = "Which major house do you want to mirror?"
        options = ({"key": "0", "desc": "Hawkwood", "goto": "menunode_lpnqmh"},
               {"key": "1", "desc": "Decados", "goto": "menunode_lpnqmh"},
               {"key": "2", "desc": "Hazat", "goto": "menunode_lpnqmh"},
               {"key": "3", "desc": "Li Halan", "goto": "menunode_lpnqmh"},
               {"key": "4", "desc": "al-Malik", "goto": "menunode_lpnqmh"})
        return text, options
    elif not raw_input.isdigit():
        caller.db.minor = 1
        caller.db.house = raw_input
        addsheet(pc, 'Faction Lore: ' + raw_input, 'Skills', 3)
        text = "Which major house do you want to mirror?"
        options = ({"key": "0", "desc": "Hawkwood", "goto": "menunode_lpnqmh"},
               {"key": "1", "desc": "Decados", "goto": "menunode_lpnqmh"},
               {"key": "2", "desc": "Hazat", "goto": "menunode_lpnqmh"},
               {"key": "3", "desc": "Li Halan", "goto": "menunode_lpnqmh"},
               {"key": "4", "desc": "al-Malik", "goto": "menunode_lpnqmh"})
        return text, options
    

    if int(raw_input) == 3:
        caller.db.recbenefices.append('Church Ally')
    elif int(raw_input) == 4:
        caller.db.recbenefices.append('Passage Contract')

    text = "At this point you select your upbringing. Depending on your house you will gain various bonuses."
    options = ({"key": "0", "desc": "High Court", "goto": "menunode_lpnq4"},
               {"key": "1", "desc": "Rural Estate", "goto": "menunode_lpnq4"},
               {"key": "2", "desc": "Landless", "goto": "menunode_lpnq4"})
    return text, options
    
    
def menunode_lpnqmh(caller, raw_input):
    caller.db.mirrorhouse = househelper[raw_input]
    
     if int(raw_input) == 3:
        caller.db.recbenefices.append('Church Ally')
    elif int(raw_input) == 4:
        caller.db.recbenefices.append('Passage Contract')

    text = "At this point you select your upbringing. Depending on your house you will gain various bonuses."
    options = ({"key": "0", "desc": "High Court", "goto": "menunode_lpnq4"},
               {"key": "1", "desc": "Rural Estate", "goto": "menunode_lpnq4"},
               {"key": "2", "desc": "Landless", "goto": "menunode_lpnq4"})
    return text, options
    

def menunode_lpn3(caller, raw_input):

    if caller.db.minor:
        apply_path_noble(0, int(raw_input), caller.db.mirrorhouse, caller)
    else:
        apply_path_noble(0, int(raw_input), caller.db.house, caller)

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
               {"key": "1", "desc": "Starman", "goto": "menunode_lpn5"},
               {"key": "2", "desc": "Diplomacy and Intrigue", "goto": "menunode_lpn5"},
               {"key": "3", "desc": "Duelist", "goto": "menunode_lpn5"},
               {"key": "4", "desc": "Dandy", "goto": "menunode_lpn5"},
               {"key": "5", "desc": "Study", "goto": "menunode_lpn5"})
    return text, options


def menunode_lpnq4(caller, raw_input):

    if caller.db.minor:
        apply_path_noble(0, int(raw_input), caller.db.mirrorhouse, caller)
    else:
        apply_path_noble(0, int(raw_input), caller.db.house, caller)

    text = "Please select your noble apprenticeship."
    options = ({"key": "0", "desc": "Soldier", "goto": "menunode_lpnq5"},
               {"key": "1", "desc": "Starman", "goto": "menunode_lpnq5"},
               {"key": "2", "desc": "Diplomacy and Intrigue", "goto": "menunode_lpnq5"},
               {"key": "3", "desc": "Duelist", "goto": "menunode_lpnq5"},
               {"key": "4", "desc": "Dandy", "goto": "menunode_lpnq5"},
               {"key": "5", "desc": "Study", "goto": "menunode_lpnq5"})
    return text, options

def menunode_lpn5(caller, raw_input):

    apply_path_noble(1, int(raw_input), 'None', caller)

    if int(raw_input) == 0:
        text = "As a soldier you get 3 points for combat skills. First point."
        options = ({"key": "0", "desc": "Artifact Melee", "exec": addsheet(caller, 'Artifact Melee', 'Skills', 1), "goto": "menunode_lpn5sd2"},
                   {"key": "1", "desc": "Archery", "exec": addsheet(caller, 'Archer', 'Skills', 1), "goto": "menunode_lpn5sd2"},
                   {"key": "2", "desc": "Artillery", "exec": addsheet(caller, 'Artillery', 'Skills', 1), "goto": "menunode_lpn5sd2"},
                   {"key": "3", "desc": "Demolitions", "exec": addsheet(caller, 'Demolitions', 'Skills', 1), "goto": "menunode_lpn5sd2"},
                   {"key": "4", "desc": "Energy Guns", "exec": addsheet(caller, 'Energy Guns', 'Skills', 1), "goto": "menunode_lpn5sd2"},
                   {"key": "5", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 1), "goto": "menunode_lpn5sd2"},
                   {"key": "6", "desc": "Gunnery", "exec": addsheet(caller, 'Gunnery', 'Skills', 1), "goto": "menunode_lpn5sd2"},
                   {"key": "7", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 1), "goto": "menunode_lpn5sd2"},
                   {"key": "8", "desc": "Slug Guns", "exec": addsheet(caller, 'Slug Guns', 'Skills', 1), "goto": "menunode_lpn5sd2"},
                   {"key": "9", "desc": "Throwing", "exec": addsheet(caller, 'Throwing', 'Skills', 1), "goto": "menunode_lpn5sd2"})
        return text, options
    elif int(raw_input) == 2:
        text = "Please enter the specialty for your Arts +1 now."
        options = ({"key": "_default", "goto": "menunode_lpn5di2"})
        return text, options
    elif int(raw_input) == 3:
        text = "As a duelist you get a melee fighting style. Pick one now."
        options = ({"key": "0", "desc": "Florentine", "goto": "menunode_lpn5d2"},
                   {"key": "1", "desc": "Kraxi Knife", "goto": "menunode_lpn5d2"},
                   {"key": "2", "desc": "Serpentis", "goto": "menunode_lpn5d2"},
                   {"key": "3", "desc": "Torero", "goto": "menunode_lpn5d2"})
        return text, options
    elif int(raw_input) == 4:
        text = "As a dandy your first choice is 1 point into a combat skill. Pick one now."
        options = ({"key": "0", "desc": "Artifact Melee", "exec": addsheet(caller, 'Artifact Melee', 'Skills', 1), "goto": "menunode_lpn5dy2"},
                   {"key": "1", "desc": "Archery", "exec": addsheet(caller, 'Archer', 'Skills', 1), "goto": "menunode_lpn5dy2"},
                   {"key": "2", "desc": "Artillery", "exec": addsheet(caller, 'Artillery', 'Skills', 1), "goto": "menunode_lpn5dy2"},
                   {"key": "3", "desc": "Demolitions", "exec": addsheet(caller, 'Demolitions', 'Skills', 1), "goto": "menunode_lpn5dy2"},
                   {"key": "4", "desc": "Energy Guns", "exec": addsheet(caller, 'Energy Guns', 'Skills', 1), "goto": "menunode_lpn5dy2"},
                   {"key": "5", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 1), "goto": "menunode_lpn5dy2"},
                   {"key": "6", "desc": "Gunnery", "exec": addsheet(caller, 'Gunnery', 'Skills', 1), "goto": "menunode_lpn5dy2"},
                   {"key": "7", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 1), "goto": "menunode_lpn5dy2"},
                   {"key": "8", "desc": "Slug Guns", "exec": addsheet(caller, 'Slug Guns', 'Skills', 1), "goto": "menunode_lpn5dy2"},
                   {"key": "9", "desc": "Throwing", "exec": addsheet(caller, 'Throwing', 'Skills', 1), "goto": "menunode_lpn5dy2"})
        return text, options
    elif int(raw_input) == 5:
        text = "As a student you get a language of your choice. Enter it now."
        options = ({"key": "_default", "goto": "menunode_lpn5s2"})
        return text, options

    text = "Please select your noble's Early Career."
    options = ({"key": "0", "desc": "Soldier", "goto": "menunode_lpn6"},
               {"key": "1", "desc": "Starman", "goto": "menunode_lpn6"},
               {"key": "2", "desc": "Duelist", "goto": "menunode_lpn6"},
               {"key": "3", "desc": "Ambassador", "goto": "menunode_lpn6"})
    return text, options
    
    
def menunode_lpn5d2(caller, raw_input):
    if int(raw_input) == 0:
        caller.db.actions['Florentine'] = ['Woven Steel', 'Off-Hand Strike', 'Double strike', 'Wall of Steel']
    elif int(raw_input) == 1:
        caller.db.actions['Kraxi Knife'] = ['Focused Rage', 'Thrust', 'Rapid Strike', 'Slip of the Knife']
    elif int(raw_input) == 2:
        caller.db.actions['Serpentis'] = ['Weaving Fangs', 'Draw and Strike', 'Setup', 'Stop Thrust']
    else:
        caller.db.actions['Torero'] = ['Faena', 'Masking Strike', 'Disarming Cloak', 'Entangling Cloak']
        
    text = "Please select your noble's Early Career."
    options = ({"key": "0", "desc": "Soldier", "goto": "menunode_lpn6"},
               {"key": "1", "desc": "Starman", "goto": "menunode_lpn6"},
               {"key": "2", "desc": "Duelist", "goto": "menunode_lpn6"},
               {"key": "3", "desc": "Ambassador", "goto": "menunode_lpn6"})
    return text, options
    
def menunode_lpn5sd2(caller):
    text = "As a soldier you get 3 points for combat skills. Second point."
    options = ({"key": "0", "desc": "Artifact Melee", "exec": addsheet(caller, 'Artifact Melee', 'Skills', 1), "goto": "menunode_lpn5sd3"},
               {"key": "1", "desc": "Archery", "exec": addsheet(caller, 'Archer', 'Skills', 1), "goto": "menunode_lpn5sd3"},
               {"key": "2", "desc": "Artillery", "exec": addsheet(caller, 'Artillery', 'Skills', 1), "goto": "menunode_lpn5sd3"},
               {"key": "3", "desc": "Demolitions", "exec": addsheet(caller, 'Demolitions', 'Skills', 1), "goto": "menunode_lpn5sd3"},
               {"key": "4", "desc": "Energy Guns", "exec": addsheet(caller, 'Energy Guns', 'Skills', 1), "goto": "menunode_lpn5sd3"},
               {"key": "5", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 1), "goto": "menunode_lpn5sd3"},
               {"key": "6", "desc": "Gunnery", "exec": addsheet(caller, 'Gunnery', 'Skills', 1), "goto": "menunode_lpn5sd3"},
               {"key": "7", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 1), "goto": "menunode_lpn5sd3"},
               {"key": "8", "desc": "Slug Guns", "exec": addsheet(caller, 'Slug Guns', 'Skills', 1), "goto": "menunode_lpn5sd3"},
               {"key": "9", "desc": "Throwing", "exec": addsheet(caller, 'Throwing', 'Skills', 1), "goto": "menunode_lpn5sd3"})
    return text, options    
    
    
def menunode_lpn5sd3(caller):
    text = "As a soldier you get 3 points for combat skills. Second point."
    options = ({"key": "0", "desc": "Artifact Melee", "exec": addsheet(caller, 'Artifact Melee', 'Skills', 1), "goto": "menunode_lpn5sd4"},
               {"key": "1", "desc": "Archery", "exec": addsheet(caller, 'Archer', 'Skills', 1), "goto": "menunode_lpn5sd4"},
               {"key": "2", "desc": "Artillery", "exec": addsheet(caller, 'Artillery', 'Skills', 1), "goto": "menunode_lpn5sd4"},
               {"key": "3", "desc": "Demolitions", "exec": addsheet(caller, 'Demolitions', 'Skills', 1), "goto": "menunode_lpn5sd4"},
               {"key": "4", "desc": "Energy Guns", "exec": addsheet(caller, 'Energy Guns', 'Skills', 1), "goto": "menunode_lpn5sd4"},
               {"key": "5", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 1), "goto": "menunode_lpn5sd4"},
               {"key": "6", "desc": "Gunnery", "exec": addsheet(caller, 'Gunnery', 'Skills', 1), "goto": "menunode_lpn5sd4"},
               {"key": "7", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 1), "goto": "menunode_lpn5sd4"},
               {"key": "8", "desc": "Slug Guns", "exec": addsheet(caller, 'Slug Guns', 'Skills', 1), "goto": "menunode_lpn5sd4"},
               {"key": "9", "desc": "Throwing", "exec": addsheet(caller, 'Throwing', 'Skills', 1), "goto": "menunode_lpn5sd4"})
    return text, options
    
    
def menunode_lpn5sd4(caller):
    text = "Please select your noble's Early Career."
    options = ({"key": "0", "desc": "Soldier", "goto": "menunode_lpn6"},
               {"key": "1", "desc": "Starman", "goto": "menunode_lpn6"},
               {"key": "2", "desc": "Duelist", "goto": "menunode_lpn6"},
               {"key": "3", "desc": "Ambassador", "goto": "menunode_lpn6"})
    return text, options
    
    
def menunode_lpn5di2(caller, raw_input):
    addsheet(caller, 'Arts ' + raw_input, 'Skills', 1)
    text = "Do you want to take 2 points of Analytical or Malefaction skills?"
    options = ({"key": "0", "desc": "Analytical", "goto": "menunode_lpn5di2a"},
               {"key": "1", "desc": "Malefaction", "goto": "menunode_lpn5di2m"}}
    return text, options
    
    
def menunode_lpn5di2a(caller):
    text = "First point of Analytical."
    options = ({"key": "0", "desc": "Bureaucracy", "exec": addsheet(caller, 'Bureaucracy', 'Skills', 1), "goto": "menunode_lpn5di2a2"},
               {"key": "1", "desc": "Investigation", "exec": addsheet(caller, 'Investigation', 'Skills', 1), "goto": "menunode_lpn5di2a2"},
               {"key": "2", "desc": "Observe", "exec": addsheet(caller, 'Observe', 'Skills', 1), "goto": "menunode_lpn5di2a2"},
               {"key": "3", "desc": "Physick", "exec": addsheet(caller, 'Physick', 'Skills', 1), "goto": "menunode_lpn5di2a2"},
               {"key": "4", "desc": "Warfare", "exec": addsheet(caller, 'Warfare', 'Skills', 1), "goto": "menunode_lpn5di2a2"})
    return text, options
    

def menunode_lpn5di2a2(caller):
    text = "Second point of Analytical."
    options = ({"key": "0", "desc": "Bureaucracy", "exec": addsheet(caller, 'Bureaucracy', 'Skills', 1), "goto": "menunode_lpn5cc"},
               {"key": "1", "desc": "Investigation", "exec": addsheet(caller, 'Investigation', 'Skills', 1), "goto": "menunode_lpn5cc"},
               {"key": "2", "desc": "Observe", "exec": addsheet(caller, 'Observe', 'Skills', 1), "goto": "menunode_lpn5cc"},
               {"key": "3", "desc": "Physick", "exec": addsheet(caller, 'Physick', 'Skills', 1), "goto": "menunode_lpn5cc"},
               {"key": "4", "desc": "Warfare", "exec": addsheet(caller, 'Warfare', 'Skills', 1), "goto": "menunode_lpn5cc"})
    return text, options
    
    
def menunode_lpn5di2m(caller):
    text = "First point of Malefaction."
    options = ({"key": "0", "desc": "Lockpicking", "exec": addsheet(caller, 'Lockpicking', 'Skills', 1), "goto": "menunode_lpn5di2m2"},
               {"key": "1", "desc": "Sleight of Hand", "exec": addsheet(caller, 'Sleight of Hand', 'Skills', 1), "goto": "menunode_lpn5di2m2"},
               {"key": "2", "desc": "Sneak", "exec": addsheet(caller, 'Sneak', 'Skills', 1), "goto": "menunode_lpn5di2m2"},
               {"key": "3", "desc": "Streetwise", "exec": addsheet(caller, 'Streetwise', 'Skills', 1), "goto": "menunode_lpn5di2m2"},
               {"key": "4", "desc": "Torture", "exec": addsheet(caller, 'Torture', 'Skills', 1), "goto": "menunode_lpn5di2m2"})
    return text, options
    

def menunode_lpn5di2m2(caller):
    text = "Second point of Malefaction."
    options = ({"key": "0", "desc": "Lockpicking", "exec": addsheet(caller, 'Lockpicking', 'Skills', 1), "goto": "menunode_lpn5cc"},
               {"key": "1", "desc": "Sleight of Hand", "exec": addsheet(caller, 'Sleight of Hand', 'Skills', 1), "goto": "menunode_lpn5cc"},
               {"key": "2", "desc": "Sneak", "exec": addsheet(caller, 'Sneak', 'Skills', 1), "goto": "menunode_lpn5cc"},
               {"key": "3", "desc": "Streetwise", "exec": addsheet(caller, 'Streetwise', 'Skills', 1), "goto": "menunode_lpn5cc"},
               {"key": "4", "desc": "Torture", "exec": addsheet(caller, 'Torture', 'Skills', 1), "goto": "menunode_lpn5cc"})
    return text, options
    
    
def menunode_lpn5dy2(caller):
    text = "Enter your Arts specialty."
    options = ({"key": "_default", "goto": "menunode_lpn5dy3"})
    return text, options
    
    
def menunode_lpn5dy3(caller, raw_input):
    addsheet(caller, 'Arts ' + raw_input, 'Skills', 1)
    text = "You have one point to spend in the control group."
    options = ({"key": "0", "desc": "Aircraft", "exec": addsheet(caller, 'Aircraft', 'Skills', 1), "goto": "menunode_lpn5cc"},
               {"key": "1", "desc": "Beastcraft", "exec": addsheet(caller, 'Beastcraft', 'Skills', 1), "goto": "menunode_lpn5cc"},
               {"key": "2", "desc": "Landcraft", "exec": addsheet(caller, 'Landcraft', 'Skills', 1), "goto": "menunode_lpn5cc"},
               {"key": "3", "desc": "Watercraft", "exec": addsheet(caller, 'Watercraft', 'Skills', 1), "goto": "menunode_lpn5cc"},
               {"key": "4", "desc": "Ride", "exec": addsheet(caller, 'Ride', 'Skills', 1), "goto": "menunode_lpn5cc"})
               
               
def menunode_lpn5s2(caller, raw_input):
    addsheet(caller, raw_input, 'Languages', 0)
    text = "Do you want Creative or Science?"
    options = ({"key": "0", "desc": "Creative", "goto": "menunode_lpn5s2c"},
               {"key": "1", "desc": "Science", "goto": "menunode_lpn5s2s"})
    return text, options
    
    
def menunode_lpn5s2s(caller):
    addsheet(caller, 'Social Science', 'Skills', 3)
    text = "So you picked science. There are 5 skills in that group but since 4 of them are Guild only you get social science.\n"
    text += "This is just a notice that you just signed up for 3 points in Social Science!"
    options = ({"key": "0", "desc": "Oh...", "goto": "menunode_lpn5cc"})
    return text, options
    
    
def menunode_lpn5s2c(caller):
    text = "Creative has Arts, Craft, Gaming and Performance. Of these only gaming does not require a specialty.\n"
    text += "If you want gaming, just select it here. If you want one of the others, type that skill and then the specialty after it.\n"
    text += "Ex: Arts Painting or Craft Blacksmith.\n"
    text += "First Point."
    options = ({"key": "0", "desc": "Gaming", "exec": addsheet(caller, 'Gaming', 'Skills', 1), "goto": "menunode_lpn5s2c2"},
               {"key": "_default", "goto": "menunode_lpn5s2c2"})
    return text, options
    
    
def menunode_lpn5s2c2(caller, raw_input):
    if not raw_input.isdigit():
        addsheet(caller, raw_input, 'Skills', 1)
        
    text = "Creative has Arts, Craft, Gaming and Performance. Of these only gaming does not require a specialty.\n"
    text += "If you want gaming, just select it here. If you want one of the others, type that skill and then the specialty after it.\n"
    text += "Ex: Arts Painting or Craft Blacksmith.\n"
    text += "Second Point. If you want to add to an existing skill type it again. Case Sensitive."
    options = ({"key": "0", "desc": "Gaming", "exec": addsheet(caller, 'Gaming', 'Skills', 1), "goto": "menunode_lpn5s2c3"},
               {"key": "_default", "goto": "menunode_lpn5s2c3"})
    return text, options
    
    
def menunode_lpn5s2c3(caller, raw_input):
    if not raw_input.isdigit():
        addsheet(caller, raw_input, 'Skills', 1)
        
    text = "Creative has Arts, Craft, Gaming and Performance. Of these only gaming does not require a specialty.\n"
    text += "If you want gaming, just select it here. If you want one of the others, type that skill and then the specialty after it.\n"
    text += "Ex: Arts Painting or Craft Blacksmith.\n"
    text += "Second Point. If you want to add to an existing skill type it again. Case Sensitive."
    options = ({"key": "0", "desc": "Gaming", "exec": addsheet(caller, 'Gaming', 'Skills', 1), "goto": "menunode_lpn5cc"},
               {"key": "_default", "goto": "menunode_lpn5s2c4"})
    return text, options
    
    
def menunode_lpn5s2c4(caller, raw_input):
    addsheet(caller, raw_input, 'Skills', 1)
    text = "Please select your noble's Early Career."
    options = ({"key": "0", "desc": "Soldier", "goto": "menunode_lpn6"},
               {"key": "1", "desc": "Starman", "goto": "menunode_lpn6"},
               {"key": "2", "desc": "Duelist", "goto": "menunode_lpn6"},
               {"key": "3", "desc": "Ambassador", "goto": "menunode_lpn6"})
    return text, options
    
    
def menunode_lpn5cc(caller):
    text = "Please select your noble's Early Career."
    options = ({"key": "0", "desc": "Soldier", "goto": "menunode_lpn6"},
               {"key": "1", "desc": "Starman", "goto": "menunode_lpn6"},
               {"key": "2", "desc": "Duelist", "goto": "menunode_lpn6"},
               {"key": "3", "desc": "Ambassador", "goto": "menunode_lpn6"})
    return text, options


# QUESTING KNIGHTS
def menunode_lpnq5(caller, raw_input):
    # Questing knights are mostly the same, but they can't suddenly switch to other archetypes and their early career is set in stone.
    apply_path_noble(1, int(raw_input), 'None', caller)

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


def menunode_lpnq57(caller):
    text = "Now pick your second spirit attribute. It gets +1."
    options = ({"Key": "0", "desc": "Presence", "exec": addsheet(caller, 'Presence', 'Attributes', 1), "goto": "menunode_lpnq58"},
               {"Key": "1", "desc": "Will", "exec": addsheet(caller, 'Will', 'Attributes', 1), "goto": "menunode_lpnq58"},
               {"Key": "2", "desc": "Faith", "exec": addsheet(caller, 'Faith', 'Attributes', 1), "goto": "menunode_lpnq58"})

    return text, options


def menunode_lpnq58(caller):
    addsheet(caller, 'Influence', 'Skills', 1)

    text = "You get 3 points in combat skills. First point."
    options = ({"key": "0", "desc": "Artifact Melee", "exec": addsheet(caller, 'Artifact Melee', 'Skills', 1), "goto": "menunode_lpnq581"},
               {"key": "1", "desc": "Archery", "exec": addsheet(caller, 'Archer', 'Skills', 1), "goto": "menunode_lpnq581"},
               {"key": "2", "desc": "Artillery", "exec": addsheet(caller, 'Artillery', 'Skills', 1), "goto": "menunode_lpnq581"},
               {"key": "3", "desc": "Demolitions", "exec": addsheet(caller, 'Demolitions', 'Skills', 1), "goto": "menunode_lpnq581"},
               {"key": "4", "desc": "Energy Guns", "exec": addsheet(caller, 'Energy Guns', 'Skills', 1), "goto": "menunode_lpnq581"},
               {"key": "5", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 1), "goto": "menunode_lpnq581"},
               {"key": "6", "desc": "Gunnery", "exec": addsheet(caller, 'Gunnery', 'Skills', 1), "goto": "menunode_lpnq581"},
               {"key": "7", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 1), "goto": "menunode_lpnq581"},
               {"key": "8", "desc": "Slug Guns", "exec": addsheet(caller, 'Slug Guns', 'Skills', 1), "goto": "menunode_lpnq581"},
               {"key": "9", "desc": "Throwing", "exec": addsheet(caller, 'Throwing', 'Skills', 1), "goto": "menunode_lpnq581"})

    return text, options
    
    
def menunode_lpnq581(caller):
    text = "You get 3 points in combat skills. Second point."
    options = ({"key": "0", "desc": "Artifact Melee", "exec": addsheet(caller, 'Artifact Melee', 'Skills', 1), "goto": "menunode_lpnq582"},
               {"key": "1", "desc": "Archery", "exec": addsheet(caller, 'Archer', 'Skills', 1), "goto": "menunode_lpnq582"},
               {"key": "2", "desc": "Artillery", "exec": addsheet(caller, 'Artillery', 'Skills', 1), "goto": "menunode_lpnq582"},
               {"key": "3", "desc": "Demolitions", "exec": addsheet(caller, 'Demolitions', 'Skills', 1), "goto": "menunode_lpnq582"},
               {"key": "4", "desc": "Energy Guns", "exec": addsheet(caller, 'Energy Guns', 'Skills', 1), "goto": "menunode_lpnq582"},
               {"key": "5", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 1), "goto": "menunode_lpnq582"},
               {"key": "6", "desc": "Gunnery", "exec": addsheet(caller, 'Gunnery', 'Skills', 1), "goto": "menunode_lpnq582"},
               {"key": "7", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 1), "goto": "menunode_lpnq582"},
               {"key": "8", "desc": "Slug Guns", "exec": addsheet(caller, 'Slug Guns', 'Skills', 1), "goto": "menunode_lpnq582"},
               {"key": "9", "desc": "Throwing", "exec": addsheet(caller, 'Throwing', 'Skills', 1), "goto": "menunode_lpnq582"})

    return text, options
    
    
def menunode_lpnq582(caller):
    text = "You get 3 points in combat skills. Third point."
    options = ({"key": "0", "desc": "Artifact Melee", "exec": addsheet(caller, 'Artifact Melee', 'Skills', 1), "goto": "menunode_lpnq59"},
               {"key": "1", "desc": "Archery", "exec": addsheet(caller, 'Archer', 'Skills', 1), "goto": "menunode_lpnq59"},
               {"key": "2", "desc": "Artillery", "exec": addsheet(caller, 'Artillery', 'Skills', 1), "goto": "menunode_lpnq59"},
               {"key": "3", "desc": "Demolitions", "exec": addsheet(caller, 'Demolitions', 'Skills', 1), "goto": "menunode_lpnq59"},
               {"key": "4", "desc": "Energy Guns", "exec": addsheet(caller, 'Energy Guns', 'Skills', 1), "goto": "menunode_lpnq59"},
               {"key": "5", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 1), "goto": "menunode_lpnq59"},
               {"key": "6", "desc": "Gunnery", "exec": addsheet(caller, 'Gunnery', 'Skills', 1), "goto": "menunode_lpnq59"},
               {"key": "7", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 1), "goto": "menunode_lpnq59"},
               {"key": "8", "desc": "Slug Guns", "exec": addsheet(caller, 'Slug Guns', 'Skills', 1), "goto": "menunode_lpnq59"},
               {"key": "9", "desc": "Throwing", "exec": addsheet(caller, 'Throwing', 'Skills', 1), "goto": "menunode_lpnq59"})

    return text, options


def menunode_lpnq59(caller):
    addsheet(caller, 'Etiquette', 'Skills', 1)
    addsheet(caller, 'Observe', 'Skills', 1)
    addsheet(caller, 'Sneak', 'Skills', 1)
    addsheet(caller, 'Vigor', 'Skills', 2)
    addsheet(caller, 'Investigation', 'Skills', 1)
    addsheet(caller, 'Physick', 'Skills', 1)

    text = "Please pick a Malefaction skill."
    options = ({"key": "0", "desc": "Lockpicking", "exec": addsheet(caller, 'Lockpicking', 'Skills', 1), "goto": "menunode_lpnq591"},
               {"key": "1", "desc": "Sleight of Hand", "exec": addsheet(caller, 'Sleight of Hand', 'Skills', 1), "goto": "menunode_lpnq591"},
               {"key": "2", "desc": "Sneak", "exec": addsheet(caller, 'Sneak', 'Skills', 1), "goto": "menunode_lpnq591"},
               {"key": "3", "desc": "Streetwise", "exec": addsheet(caller, 'Streetwise', 'Skills', 1), "goto": "menunode_lpnq591"},
               {"key": "4", "desc": "Torture", "exec": addsheet(caller, 'Torture', 'Skills', 1), "goto": "menunode_lpnq591"})

    return text, options


def menunode_lpnq591(caller):
    text = "Please enter a dialect for your free language choice."
    options = {"key": "_default", "goto": "menunode_lpnq592"}

    return text, options


def menunode_lpnq592(caller, raw_input):
    addsheet(caller, raw_input, 'Languages', 0)
    caller.db.benefices['Rank'] = 'Knight'

    # Tour of Duty
# QUESTING KNIGHTS END


def menunode_lpn6(caller, raw_input):
    apply_path_noble(2, int(raw_input), 'None', caller)
 
    if int(raw_input) == 0: # Soldier
        text = "As a soldier you get 3 points in combat skills. First point."
        options = ({"key": "0", "desc": "Artifact Melee", "exec": addsheet(caller, 'Artifact Melee', 'Skills', 1), "goto": "menunode_lpn6sd2"},
                   {"key": "1", "desc": "Archery", "exec": addsheet(caller, 'Archer', 'Skills', 1), "goto": "menunode_lpn6sd2"},
                   {"key": "2", "desc": "Artillery", "exec": addsheet(caller, 'Artillery', 'Skills', 1), "goto": "menunode_lpn6sd2"},
                   {"key": "3", "desc": "Demolitions", "exec": addsheet(caller, 'Demolitions', 'Skills', 1), "goto": "menunode_lpn6sd2"},
                   {"key": "4", "desc": "Energy Guns", "exec": addsheet(caller, 'Energy Guns', 'Skills', 1), "goto": "menunode_lpn6sd2"},
                   {"key": "5", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 1), "goto": "menunode_lpn6sd2"},
                   {"key": "6", "desc": "Gunnery", "exec": addsheet(caller, 'Gunnery', 'Skills', 1), "goto": "menunode_lpn6sd2"},
                   {"key": "7", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 1), "goto": "menunode_lpn6sd2"},
                   {"key": "8", "desc": "Slug Guns", "exec": addsheet(caller, 'Slug Guns', 'Skills', 1), "goto": "menunode_lpn6sd2"},
                   {"key": "9", "desc": "Throwing", "exec": addsheet(caller, 'Throwing', 'Skills', 1), "goto": "menunode_lpn6sd2"})
        return text, options
    elif int(raw_input) == 1: # Starman
        text = "As a starman you get 2 points in combat skills. First point."
        options = ({"key": "0", "desc": "Artifact Melee", "exec": addsheet(caller, 'Artifact Melee', 'Skills', 1), "goto": "menunode_lpn6sm2"},
                   {"key": "1", "desc": "Archery", "exec": addsheet(caller, 'Archer', 'Skills', 1), "goto": "menunode_lpn6sm2"},
                   {"key": "2", "desc": "Artillery", "exec": addsheet(caller, 'Artillery', 'Skills', 1), "goto": "menunode_lpn6sm2"},
                   {"key": "3", "desc": "Demolitions", "exec": addsheet(caller, 'Demolitions', 'Skills', 1), "goto": "menunode_lpn6sm2"},
                   {"key": "4", "desc": "Energy Guns", "exec": addsheet(caller, 'Energy Guns', 'Skills', 1), "goto": "menunode_lpn6sm2"},
                   {"key": "5", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 1), "goto": "menunode_lpn6sm2"},
                   {"key": "6", "desc": "Gunnery", "exec": addsheet(caller, 'Gunnery', 'Skills', 1), "goto": "menunode_lpn6sm2"},
                   {"key": "7", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 1), "goto": "menunode_lpn6sm2"},
                   {"key": "8", "desc": "Slug Guns", "exec": addsheet(caller, 'Slug Guns', 'Skills', 1), "goto": "menunode_lpn6sm2"},
                   {"key": "9", "desc": "Throwing", "exec": addsheet(caller, 'Throwing', 'Skills', 1), "goto": "menunode_lpn6sm2"})
        return text, options
    elif int(raw_input) == 2: # Duelist
        text = "As a duelist you get a melee fighting style. Pick one now."
        options = ({"key": "0", "desc": "Florentine", "goto": "menunode_lpn6d2"},
                   {"key": "1", "desc": "Kraxi Knife", "goto": "menunode_lpn6d2"},
                   {"key": "2", "desc": "Serpentis", "goto": "menunode_lpn6d2"},
                   {"key": "3", "desc": "Torero", "goto": "menunode_lpn6d2"})
                   
        options = [x for x in options if x['desc'] not in caller.db.actions]
        
        return text, options
    elif int(raw_input) == 3: # ambassador
        text = "Enter the specialty for your arts."
        options = ({'key': '_default', 'goto': 'menunode_lpn6a2'})
        return text, options
        
        
def menunode_lpn6sd2(caller):
    text = "As a soldier you get 3 points in combat skills. Second point."
    options = ({"key": "0", "desc": "Artifact Melee", "exec": addsheet(caller, 'Artifact Melee', 'Skills', 1), "goto": "menunode_lpn6sd3"},
               {"key": "1", "desc": "Archery", "exec": addsheet(caller, 'Archer', 'Skills', 1), "goto": "menunode_lpn6sd3"},
               {"key": "2", "desc": "Artillery", "exec": addsheet(caller, 'Artillery', 'Skills', 1), "goto": "menunode_lpn6sd3"},
               {"key": "3", "desc": "Demolitions", "exec": addsheet(caller, 'Demolitions', 'Skills', 1), "goto": "menunode_lpn6sd3"},
               {"key": "4", "desc": "Energy Guns", "exec": addsheet(caller, 'Energy Guns', 'Skills', 1), "goto": "menunode_lpn6sd3"},
               {"key": "5", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 1), "goto": "menunode_lpn6sd3"},
               {"key": "6", "desc": "Gunnery", "exec": addsheet(caller, 'Gunnery', 'Skills', 1), "goto": "menunode_lpn6sd3"},
               {"key": "7", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 1), "goto": "menunode_lpn6sd3"},
               {"key": "8", "desc": "Slug Guns", "exec": addsheet(caller, 'Slug Guns', 'Skills', 1), "goto": "menunode_lpn6sd3"},
               {"key": "9", "desc": "Throwing", "exec": addsheet(caller, 'Throwing', 'Skills', 1), "goto": "menunode_lpn6sd3"})
    return text, options
    
def menunode_lpn6sd3(caller):
    text = "As a soldier you get 3 points in combat skills. Third point."
    options = ({"key": "0", "desc": "Artifact Melee", "exec": addsheet(caller, 'Artifact Melee', 'Skills', 1), "goto": "menunode_lpn6sd4"},
               {"key": "1", "desc": "Archery", "exec": addsheet(caller, 'Archer', 'Skills', 1), "goto": "menunode_lpn6sd4"},
               {"key": "2", "desc": "Artillery", "exec": addsheet(caller, 'Artillery', 'Skills', 1), "goto": "menunode_lpn6sd4"},
               {"key": "3", "desc": "Demolitions", "exec": addsheet(caller, 'Demolitions', 'Skills', 1), "goto": "menunode_lpn6sd4"},
               {"key": "4", "desc": "Energy Guns", "exec": addsheet(caller, 'Energy Guns', 'Skills', 1), "goto": "menunode_lpn6sd4"},
               {"key": "5", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 1), "goto": "menunode_lpn6sd4"},
               {"key": "6", "desc": "Gunnery", "exec": addsheet(caller, 'Gunnery', 'Skills', 1), "goto": "menunode_lpn6sd4"},
               {"key": "7", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 1), "goto": "menunode_lpn6sd4"},
               {"key": "8", "desc": "Slug Guns", "exec": addsheet(caller, 'Slug Guns', 'Skills', 1), "goto": "menunode_lpn6sd4"},
               {"key": "9", "desc": "Throwing", "exec": addsheet(caller, 'Throwing', 'Skills', 1), "goto": "menunode_lpn6sd4"})
    return text, options
    

def menunode_lpn6sd4(caller):
    text = "You now get 3 social points. First point."
    options = ({"key": "0", "desc": "Empathy", "exec": addsheet(caller, 'Empathy', 'Skills', 1), "goto": "menunode_lpn6sd5"},
               {"key": "1", "desc": "Etiquette", "exec": addsheet(caller, 'Etiquette', 'Skills', 1), "goto": "menunode_lpn6sd5"},
               {"key": "2", "desc": "Influence", "exec": addsheet(caller, 'Influence', 'Skills', 1), "goto": "menunode_lpn6sd5"},
               {"key": "3", "desc": "Knavery", "exec": addsheet(caller, 'Knavery', 'Skills', 1), "goto": "menunode_lpn6sd5"},
               {"key": "4", "desc": "Leadership", "exec": addsheet(caller, 'Leadership', 'Skills', 1), "goto": "menunode_lpn6sd5"})
    return text, options
    
    
def menunode_lpn6sd5(caller):
    text = "You now get 3 social points. Second point."
    options = ({"key": "0", "desc": "Empathy", "exec": addsheet(caller, 'Empathy', 'Skills', 1), "goto": "menunode_lpn6sd6"},
               {"key": "1", "desc": "Etiquette", "exec": addsheet(caller, 'Etiquette', 'Skills', 1), "goto": "menunode_lpn6sd6"},
               {"key": "2", "desc": "Influence", "exec": addsheet(caller, 'Influence', 'Skills', 1), "goto": "menunode_lpn6sd6"},
               {"key": "3", "desc": "Knavery", "exec": addsheet(caller, 'Knavery', 'Skills', 1), "goto": "menunode_lpn6sd6"},
               {"key": "4", "desc": "Leadership", "exec": addsheet(caller, 'Leadership', 'Skills', 1), "goto": "menunode_lpn6sd6"})
    return text, options
    
    
def menunode_lpn6sd6(caller):
    text = "You now get 3 social points. Third point."
    options = ({"key": "0", "desc": "Empathy", "exec": addsheet(caller, 'Empathy', 'Skills', 1), "goto": "menunode_lpn6cc"},
               {"key": "1", "desc": "Etiquette", "exec": addsheet(caller, 'Etiquette', 'Skills', 1), "goto": "menunode_lpn6cc"},
               {"key": "2", "desc": "Influence", "exec": addsheet(caller, 'Influence', 'Skills', 1), "goto": "menunode_lpn6cc"},
               {"key": "3", "desc": "Knavery", "exec": addsheet(caller, 'Knavery', 'Skills', 1), "goto": "menunode_lpn6cc"},
               {"key": "4", "desc": "Leadership", "exec": addsheet(caller, 'Leadership', 'Skills', 1), "goto": "menunode_lpn6cc"})
    return text, options
    
    
def menunode_lpn6sm2(caller):
    text = "As a starman you get 2 points in combat skills. Second Point.."
    options = ({"key": "0", "desc": "Artifact Melee", "exec": addsheet(caller, 'Artifact Melee', 'Skills', 1), "goto": "menunode_lpn6sm3"},
               {"key": "1", "desc": "Archery", "exec": addsheet(caller, 'Archer', 'Skills', 1), "goto": "menunode_lpn6sm3"},
               {"key": "2", "desc": "Artillery", "exec": addsheet(caller, 'Artillery', 'Skills', 1), "goto": "menunode_lpn6sm3"},
               {"key": "3", "desc": "Demolitions", "exec": addsheet(caller, 'Demolitions', 'Skills', 1), "goto": "menunode_lpn6sm3"},
               {"key": "4", "desc": "Energy Guns", "exec": addsheet(caller, 'Energy Guns', 'Skills', 1), "goto": "menunode_lpn6sm3"},
               {"key": "5", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 1), "goto": "menunode_lpn6sm3"},
               {"key": "6", "desc": "Gunnery", "exec": addsheet(caller, 'Gunnery', 'Skills', 1), "goto": "menunode_lpn6sm3"},
               {"key": "7", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 1), "goto": "menunode_lpn6sm3"},
               {"key": "8", "desc": "Slug Guns", "exec": addsheet(caller, 'Slug Guns', 'Skills', 1), "goto": "menunode_lpn6sm3"},
               {"key": "9", "desc": "Throwing", "exec": addsheet(caller, 'Throwing', 'Skills', 1), "goto": "menunode_lpn6sm3"})
    return text, options
    
    
def menunode_lpn6sm3(caller):
    text = "You now get 2 social points. First point."
    options = ({"key": "0", "desc": "Empathy", "exec": addsheet(caller, 'Empathy', 'Skills', 1), "goto": "menunode_lpn6sm4"},
               {"key": "1", "desc": "Etiquette", "exec": addsheet(caller, 'Etiquette', 'Skills', 1), "goto": "menunode_lpn6sm4"},
               {"key": "2", "desc": "Influence", "exec": addsheet(caller, 'Influence', 'Skills', 1), "goto": "menunode_lpn6sm4"},
               {"key": "3", "desc": "Knavery", "exec": addsheet(caller, 'Knavery', 'Skills', 1), "goto": "menunode_lpn6sm4"},
               {"key": "4", "desc": "Leadership", "exec": addsheet(caller, 'Leadership', 'Skills', 1), "goto": "menunode_lpn6sm4"})
    return text, options
    
    
def menunode_lpn6sm3(caller):
    text = "You now get 2 social points. Second point."
    options = ({"key": "0", "desc": "Empathy", "exec": addsheet(caller, 'Empathy', 'Skills', 1), "goto": "menunode_lpn6cc"},
               {"key": "1", "desc": "Etiquette", "exec": addsheet(caller, 'Etiquette', 'Skills', 1), "goto": "menunode_lpn6cc"},
               {"key": "2", "desc": "Influence", "exec": addsheet(caller, 'Influence', 'Skills', 1), "goto": "menunode_lpn6cc"},
               {"key": "3", "desc": "Knavery", "exec": addsheet(caller, 'Knavery', 'Skills', 1), "goto": "menunode_lpn6cc"},
               {"key": "4", "desc": "Leadership", "exec": addsheet(caller, 'Leadership', 'Skills', 1), "goto": "menunode_lpn6cc"})
    return text, options
    

def menunode_lpn6d2(caller, raw_input):
    if int(raw_input) == 0:
        caller.db.actions['Florentine'] = ['Woven Steel', 'Off-Hand Strike', 'Double strike', 'Wall of Steel']
    elif int(raw_input) == 1:
        caller.db.actions['Kraxi Knife'] = ['Focused Rage', 'Thrust', 'Rapid Strike', 'Slip of the Knife']
    elif int(raw_input) == 2:
        caller.db.actions['Serpentis'] = ['Weaving Fangs', 'Draw and Strike', 'Setup', 'Stop Thrust']
    else:
        caller.db.actions['Torero'] = ['Faena', 'Masking Strike', 'Disarming Cloak', 'Entangling Cloak']
        
    text = "You now get 3 social points. First point."
    options = ({"key": "0", "desc": "Empathy", "exec": addsheet(caller, 'Empathy', 'Skills', 1), "goto": "menunode_lpn6d3"},
               {"key": "1", "desc": "Etiquette", "exec": addsheet(caller, 'Etiquette', 'Skills', 1), "goto": "menunode_lpn6d3"},
               {"key": "2", "desc": "Influence", "exec": addsheet(caller, 'Influence', 'Skills', 1), "goto": "menunode_lpn6d3"},
               {"key": "3", "desc": "Knavery", "exec": addsheet(caller, 'Knavery', 'Skills', 1), "goto": "menunode_lpn6d3"},
               {"key": "4", "desc": "Leadership", "exec": addsheet(caller, 'Leadership', 'Skills', 1), "goto": "menunode_lpn6d3"})
    return text, options
    

def menunode_lpn6d3(caller):
    text = "You now get 3 social points. Second point."
    options = ({"key": "0", "desc": "Empathy", "exec": addsheet(caller, 'Empathy', 'Skills', 1), "goto": "menunode_lpn6d4"},
               {"key": "1", "desc": "Etiquette", "exec": addsheet(caller, 'Etiquette', 'Skills', 1), "goto": "menunode_lpn6d4"},
               {"key": "2", "desc": "Influence", "exec": addsheet(caller, 'Influence', 'Skills', 1), "goto": "menunode_lpn6d4"},
               {"key": "3", "desc": "Knavery", "exec": addsheet(caller, 'Knavery', 'Skills', 1), "goto": "menunode_lpn6d4"},
               {"key": "4", "desc": "Leadership", "exec": addsheet(caller, 'Leadership', 'Skills', 1), "goto": "menunode_lpn6d4"})
    return text, options
    

def menunode_lpn6d4(caller):
    text = "You now get 3 social points. Third point."
    options = ({"key": "0", "desc": "Empathy", "exec": addsheet(caller, 'Empathy', 'Skills', 1), "goto": "menunode_lpn6cc"},
               {"key": "1", "desc": "Etiquette", "exec": addsheet(caller, 'Etiquette', 'Skills', 1), "goto": "menunode_lpn6cc"},
               {"key": "2", "desc": "Influence", "exec": addsheet(caller, 'Influence', 'Skills', 1), "goto": "menunode_lpn6cc"},
               {"key": "3", "desc": "Knavery", "exec": addsheet(caller, 'Knavery', 'Skills', 1), "goto": "menunode_lpn6cc"},
               {"key": "4", "desc": "Leadership", "exec": addsheet(caller, 'Leadership', 'Skills', 1), "goto": "menunode_lpn6cc"})
    return text, options
    
    
def menunode_lpn6a2(caller, raw_input):
    addsheet(caller, 'Arts ' + raw_input, 'Skills', 1)
    
    text = "Do you want Investigation at +2 or to choose 2 points of skills from the Malefaction group?"
    options = ({"key": "0", "desc": "Investigation +2", "exec": addsheet(caller, 'Investigation', 'Skills', 2), "goto": "menunode_lpn6cc"},
               {"key": "1", "desc": "Malefaction", "goto": "menunode_lpn6a3"})
    return text, options
    

def menunode_lpn6a3(caller):
    text = "First point of Malefaction."
    options = ({"key": "0", "desc": "Lockpicking", "exec": addsheet(caller, 'Lockpicking', 'Skills', 1), "goto": "menunode_lpn6a4"},
               {"key": "1", "desc": "Sleight of Hand", "exec": addsheet(caller, 'Sleight of Hand', 'Skills', 1), "goto": "menunode_lpn6a4"},
               {"key": "2", "desc": "Sneak", "exec": addsheet(caller, 'Sneak', 'Skills', 1), "goto": "menunode_lpn6a4"},
               {"key": "3", "desc": "Streetwise", "exec": addsheet(caller, 'Streetwise', 'Skills', 1), "goto": "menunode_lpn6a4"},
               {"key": "4", "desc": "Torture", "exec": addsheet(caller, 'Torture', 'Skills', 1), "goto": "menunode_lpn6a4"})
    return text, options
    
    
def menunode_lpn6a4(caller):
    text = "Second point of Malefaction."
    options = ({"key": "0", "desc": "Lockpicking", "exec": addsheet(caller, 'Lockpicking', 'Skills', 1), "goto": "menunode_lpn6cc"},
               {"key": "1", "desc": "Sleight of Hand", "exec": addsheet(caller, 'Sleight of Hand', 'Skills', 1), "goto": "menunode_lpn6cc"},
               {"key": "2", "desc": "Sneak", "exec": addsheet(caller, 'Sneak', 'Skills', 1), "goto": "menunode_lpn6cc"},
               {"key": "3", "desc": "Streetwise", "exec": addsheet(caller, 'Streetwise', 'Skills', 1), "goto": "menunode_lpn6cc"},
               {"key": "4", "desc": "Torture", "exec": addsheet(caller, 'Torture', 'Skills', 1), "goto": "menunode_lpn6cc"})
    return text, options
    

def menunode_lpn6cc(caller):
    pass
    # TOUR OF DUTY
    
    # End Noble Section

    # Begin Priest Section
def menunode_lpp1(caller):
    caller.db.recbenefices.append('Ordained')
    caller.db.recbenefices.append('Vestments')
    caller.db.archetype = 'Priest'

    text = "If you intend to do Mendicants with a custom Order, please use custom cg. What order does your priest come from?"
    options = ({"key": "0", "desc": "Urth Orthodox", "goto": "menunode_lpp2"},
               {"key": "1", "desc": "Brother Battle", "goto": "menunode_lppbb"},
               {"key": "2", "desc": "Eskatonic Order", "goto": "menunode_lpp2"},
               {"key": "3", "desc": "Temple Avesti", "goto": "menunode_lpp2"},
               {"key": "4", "desc": "Sanctuary Aeon", "goto": "menunode_lpp2"},
               {"key": "5", "desc": "Mendicant Monks", "goto": "menunode_lppmm"})
    return text, options


def menunode_lppmm(caller, raw_input):
    caller.db.house = "Mendicant Monks"
    caller.db.minor = 1
    text = "Which order are you mirroring for bonuses?\n"
    options = ({"key": "0", "desc": "Urth Orthodox", "goto": "menunode_lppmm2"},
               {"key": "1", "desc": "Brother Battle", "goto": "menunode_lppbb"},
               {"key": "2", "desc": "Eskatonic Order", "goto": "menunode_lppmm2"},
               {"key": "3", "desc": "Temple Avesti", "goto": "menunode_lppmm2"},
               {"key": "4", "desc": "Sanctuary Aeon", "goto": "menunode_lppmm2"})
    return text, options


def menunode_lppmm2(caller, raw_input):
    caller.db.mirrorhouse = priesthelper[raw_input]

    if int(raw_input) == 0:
        caller.db.recbenefices.append('Noble Ally')
    elif int(raw_input) == 2:
        caller.db.recbenefices.append('Secrets')
        caller.db.recbenefices.append('Refuge')
    elif int(raw_input) == 4:
        caller.db.recbenefices.append('Ally')

    text = "Now choose your upbringing. Upbringing for a priest has 2 factors. First pick your Environment."
    options = ({"key": "0", "desc": "City", "exec": apply_path_uppm(caller, 0, 0), "goto": "menunode_lpp3"},
               {"key": "1", "desc": "Town", "exec": apply_path_uppm(caller, 0, 1), "goto": "menunode_lpp3"},
               {"key": "2", "desc": "Country", "exec": apply_path_uppm(caller, 0, 2), "goto": "menunode_lpp3"},
               {"key": "3", "desc": "Space Habitat", "exec": apply_path_uppm(caller, 0, 3), "goto": "menunode_lpp3"})
    return text, options


def menunode_lpp2(caller, raw_input):
    caller.db.house = priesthelper[raw_input]
    addsheet(caller, 'Faction Lore.' + priesthelper[raw_input], 'Skills', 3)

    if int(raw_input) == 0:
        caller.db.recbenefices.append('Noble Ally')
    elif int(raw_input) == 2:
        caller.db.recbenefices.append('Secrets')
        caller.db.recbenefices.append('Refuge')
    elif int(raw_input) == 4:
        caller.db.recbenefices.append('Ally')

    text = "Now choose your upbringing. Upbringing for a priest has 2 factors. First pick your Environment."
    options = ({"key": "0", "desc": "City", "exec": apply_path_uppm(caller, 0, 0), "goto": "menunode_lpp3"},
               {"key": "1", "desc": "Town", "exec": apply_path_uppm(caller, 0, 1), "goto": "menunode_lpp3"},
               {"key": "2", "desc": "Country", "exec": apply_path_uppm(caller, 0, 2), "goto": "menunode_lpp3"},
               {"key": "3", "desc": "Space Habitat", "exec": apply_path_uppm(caller, 0, 3), "goto": "menunode_lpp3"})
    return text, options

def menunode_lpp3(caller):
    text = "The next thing you need to pick is your Class."
    options = ({"key": "0", "desc": "Wealthy", "exec": apply_path_uppm(caller, 1, 0), "goto": "menunode_lpp31"},
               {"key": "1", "desc": "Middle", "exec": apply_path_uppm(caller, 1, 1), "goto": "menunode_lpp32"},
               {"key": "2", "desc": "Poor", "exec": apply_path_uppm(caller, 1, 2), "goto": "menunode_lpp33"})
    return text, options
               
               
def menunode_lpp31(caller):
    text = "You get 1 point in the social group."
    options = ({"key": "0", "desc": "Empathy", "exec": addsheet(caller, 'Empathy', 'Skills', 1), "goto": "menunode_lpp4"},
               {"key": "1", "desc": "Etiquette", "exec": addsheet(caller, 'Etiquette', 'Skills', 1), "goto": "menunode_lpp4"},
               {"key": "2", "desc": "Influence", "exec": addsheet(caller, 'Influence', 'Skills', 1), "goto": "menunode_lpp4"},
               {"key": "3", "desc": "Knavery", "exec": addsheet(caller, 'Knavery', 'Skills', 1), "goto": "menunode_lpp4"},
               {"key": "4", "desc": "Leadership", "exec": addsheet(caller, 'Leadership', 'Skills', 1), "goto": "menunode_lpp4"})
    return text, options
    
    
def menunode_lpp32(caller):
    text = "Enter your craft specialty."
    options = ({"key": "_default", "goto": "menunode_lpp322"})
    return text, options
    
    
def menunode_lpp322(caller, raw_input):
    addsheet(caller, 'Craft ' + raw_input, 'Skills', 1)
    
    text = "At this point you choose your apprenticeship."
    options = ({"key": "0", "desc": "Cathedral", "goto": "menunode_lpp5"},
               {"key": "1", "desc": "Parish", "goto": "menunode_lpp5"},
               {"key": "2", "desc": "Monastery", "goto": "menunode_lpp5"})
    return text, options
    
    
def menunode_lpp33(caller):
    text = "You get 1 point in the malefaction group."
    options = ({"key": "0", "desc": "Lockpicking", "exec": addsheet(caller, 'Lockpicking', 'Skills', 1), "goto": "menunode_lpp4"},
               {"key": "1", "desc": "Sleight of Hand", "exec": addsheet(caller, 'Sleight of Hand', 'Skills', 1), "goto": "menunode_lpp4"},
               {"key": "2", "desc": "Sneak", "exec": addsheet(caller, 'Sneak', 'Skills', 1), "goto": "menunode_lpp4"},
               {"key": "3", "desc": "Streetwise", "exec": addsheet(caller, 'Streetwise', 'Skills', 1), "goto": "menunode_lpp4"},
               {"key": "4", "desc": "Torture", "exec": addsheet(caller, 'Torture', 'Skills', 1), "goto": "menunode_lpp4"})
    return text, options
    
    
def menunode_lpp4(caller):
    text = "At this point you choose your apprenticeship."
    options = ({"key": "0", "desc": "Cathedral", "goto": "menunode_lpp5"},
               {"key": "1", "desc": "Parish", "goto": "menunode_lpp5"},
               {"key": "2", "desc": "Monastery", "goto": "menunode_lpp5"})
    return text, options
    
    
def menunode_lpp5(caller, raw_input):
    if caller.db.minor:
        apply_path_priest(caller, 0, int(raw_input), caller.db.mirrorhouse)
    else:
        apply_path_priest(caller, 0, int(raw_input), caller.db.house)
    
    # cathdral    
    if int(raw_input) == 0:
        if caller.db.house == "Temple Avesti" or caller.db.mirrorhouse == "Temple Avesti":
            text = "You get 1 point in the combat group."
            options = ({"key": "0", "desc": "Artifact Melee", "exec": addsheet(caller, 'Artifact Melee', 'Skills', 1), "goto": "menunode_lpp5ta2"},
                       {"key": "1", "desc": "Archery", "exec": addsheet(caller, 'Archer', 'Skills', 1), "goto": "menunode_lpp5ta2"},
                       {"key": "2", "desc": "Artillery", "exec": addsheet(caller, 'Artillery', 'Skills', 1), "goto": "menunode_lpp5ta2"},
                       {"key": "3", "desc": "Demolitions", "exec": addsheet(caller, 'Demolitions', 'Skills', 1), "goto": "menunode_lpp5ta2"},
                       {"key": "4", "desc": "Energy Guns", "exec": addsheet(caller, 'Energy Guns', 'Skills', 1), "goto": "menunode_lpp5ta2"},
                       {"key": "5", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 1), "goto": "menunode_lpp5ta2"},
                       {"key": "6", "desc": "Gunnery", "exec": addsheet(caller, 'Gunnery', 'Skills', 1), "goto": "menunode_lpp5ta2"},
                       {"key": "7", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 1), "goto": "menunode_lpp5ta2"},
                       {"key": "8", "desc": "Slug Guns", "exec": addsheet(caller, 'Slug Guns', 'Skills', 1), "goto": "menunode_lpp5ta2"},
                       {"key": "9", "desc": "Throwing", "exec": addsheet(caller, 'Throwing', 'Skills', 1), "goto": "menunode_lpp5ta2"})
            return text, options
        elif caller.db.house == "Sanctuary Aeon" or caller.db.mirrorhouse == "Sanctuary Aeon":
            text = "What is your arts specialty?"
            options = ({"key": "_default", "goto": "menunode_lpp5sa"})
            return text, options
    # Parish
    elif int(raw_input) == 1:
        if caller.db.house == "Temple Avesti" or caller.db.mirrorhouse == "Temple Avesti":
            text = "You get 1 point in the combat group."
            options = ({"key": "0", "desc": "Artifact Melee", "exec": addsheet(caller, 'Artifact Melee', 'Skills', 1), "goto": "menunode_lpp5ta2"},
                       {"key": "1", "desc": "Archery", "exec": addsheet(caller, 'Archer', 'Skills', 1), "goto": "menunode_lpp5ta2"},
                       {"key": "2", "desc": "Artillery", "exec": addsheet(caller, 'Artillery', 'Skills', 1), "goto": "menunode_lpp5ta2"},
                       {"key": "3", "desc": "Demolitions", "exec": addsheet(caller, 'Demolitions', 'Skills', 1), "goto": "menunode_lpp5ta2"},
                       {"key": "4", "desc": "Energy Guns", "exec": addsheet(caller, 'Energy Guns', 'Skills', 1), "goto": "menunode_lpp5ta2"},
                       {"key": "5", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 1), "goto": "menunode_lpp5ta2"},
                       {"key": "6", "desc": "Gunnery", "exec": addsheet(caller, 'Gunnery', 'Skills', 1), "goto": "menunode_lpp5ta2"},
                       {"key": "7", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 1), "goto": "menunode_lpp5ta2"},
                       {"key": "8", "desc": "Slug Guns", "exec": addsheet(caller, 'Slug Guns', 'Skills', 1), "goto": "menunode_lpp5ta2"},
                       {"key": "9", "desc": "Throwing", "exec": addsheet(caller, 'Throwing', 'Skills', 1), "goto": "menunode_lpp5ta2"})
            return text, options
        elif caller.db.house == "Eskatonic Order" or caller.db.mirrorhouse == "Eskatonic Order":
            text = "You get 3 points in the Analytical group."
            options = ({"key": "0", "desc": "Bureaucracy", "exec": addsheet(caller, 'Bureaucracy', 'Skills', 1), "goto": "menunode_lpp5eo02"},
                       {"key": "1", "desc": "Investigation", "exec": addsheet(caller, 'Investigation', 'Skills', 1), "goto": "menunode_lpp5eo02"},
                       {"key": "2", "desc": "Observe", "exec": addsheet(caller, 'Observe', 'Skills', 1), "goto": "menunode_lpp5eo02"},
                       {"key": "3", "desc": "Physick", "exec": addsheet(caller, 'Physick', 'Skills', 1), "goto": "menunode_lpp5eo02"},
                       {"key": "4", "desc": "Warfare", "exec": addsheet(caller, 'Warfare', 'Skills', 1), "goto": "menunode_lpp5eo02"})
            return text, options
    # Monastery
    elif int(raw_input) == 2:
        if caller.db.house == "Temple Avesti" or caller.db.mirrorhouse == "Temple Avesti":
            text = "You get 1 point in the combat group."
            options = ({"key": "0", "desc": "Artifact Melee", "exec": addsheet(caller, 'Artifact Melee', 'Skills', 1), "goto": "menunode_lpp5ta2"},
                       {"key": "1", "desc": "Archery", "exec": addsheet(caller, 'Archer', 'Skills', 1), "goto": "menunode_lpp5ta2"},
                       {"key": "2", "desc": "Artillery", "exec": addsheet(caller, 'Artillery', 'Skills', 1), "goto": "menunode_lpp5ta2"},
                       {"key": "3", "desc": "Demolitions", "exec": addsheet(caller, 'Demolitions', 'Skills', 1), "goto": "menunode_lpp5ta2"},
                       {"key": "4", "desc": "Energy Guns", "exec": addsheet(caller, 'Energy Guns', 'Skills', 1), "goto": "menunode_lpp5ta2"},
                       {"key": "5", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 1), "goto": "menunode_lpp5ta2"},
                       {"key": "6", "desc": "Gunnery", "exec": addsheet(caller, 'Gunnery', 'Skills', 1), "goto": "menunode_lpp5ta2"},
                       {"key": "7", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 1), "goto": "menunode_lpp5ta2"},
                       {"key": "8", "desc": "Slug Guns", "exec": addsheet(caller, 'Slug Guns', 'Skills', 1), "goto": "menunode_lpp5ta2"},
                       {"key": "9", "desc": "Throwing", "exec": addsheet(caller, 'Throwing', 'Skills', 1), "goto": "menunode_lpp5ta2"})
            return text, options
        elif caller.db.house == "Eskatonic Order" or caller.db.mirrorhouse == "Eskatonic Order":
            text = "You get 2 points in the Analytical group."
            options = ({"key": "0", "desc": "Bureaucracy", "exec": addsheet(caller, 'Bureaucracy', 'Skills', 1), "goto": "menunode_lpp5eo12"},
                       {"key": "1", "desc": "Investigation", "exec": addsheet(caller, 'Investigation', 'Skills', 1), "goto": "menunode_lpp5eo12"},
                       {"key": "2", "desc": "Observe", "exec": addsheet(caller, 'Observe', 'Skills', 1), "goto": "menunode_lpp5eo12"},
                       {"key": "3", "desc": "Physick", "exec": addsheet(caller, 'Physick', 'Skills', 1), "goto": "menunode_lpp5eo12"},
                       {"key": "4", "desc": "Warfare", "exec": addsheet(caller, 'Warfare', 'Skills', 1), "goto": "menunode_lpp5eo12"})
            return text, options
            
    text = "Please select your early career."
    options = ({"key": "0", "desc": "Preacher/Pastor", "goto":"menunode_lpp6"},
               {"key": "1", "desc": "Monk", "goto":"menunode_lpp6"},
               {"key": "2", "desc": "Missionary", "goto":"menunode_lpp6"},
               {"key": "3", "desc": "Healer", "goto":"menunode_lpp6"},
               {"key": "4", "desc": "Inquisitor", "goto":"menunode_lpp6"})
    return text, options

def menunode_lpp5sa(caller, raw_input):
    addsheet(caller, 'Arts ' + raw_input, 'Skills', 1)
    text = "Please select your early career."
    options = ({"key": "0", "desc": "Preacher/Pastor", "goto":"menunode_lpp6"},
               {"key": "1", "desc": "Monk", "goto":"menunode_lpp6"},
               {"key": "2", "desc": "Missionary", "goto":"menunode_lpp6"},
               {"key": "3", "desc": "Healer", "goto":"menunode_lpp6"},
               {"key": "4", "desc": "Inquisitor", "goto":"menunode_lpp6"})
    return text, options
    

def menunode_lpp5ta2(caller):
    text = "You get 2 points in the social group."
    options = ({"key": "0", "desc": "Empathy", "exec": addsheet(caller, 'Empathy', 'Skills', 1), "goto": "menunode_lpp5ta3"},
               {"key": "1", "desc": "Etiquette", "exec": addsheet(caller, 'Etiquette', 'Skills', 1), "goto": "menunode_lpp5ta3"},
               {"key": "2", "desc": "Influence", "exec": addsheet(caller, 'Influence', 'Skills', 1), "goto": "menunode_lpp5ta3"},
               {"key": "3", "desc": "Knavery", "exec": addsheet(caller, 'Knavery', 'Skills', 1), "goto": "menunode_lpp5ta3"},
               {"key": "4", "desc": "Leadership", "exec": addsheet(caller, 'Leadership', 'Skills', 1), "goto": "menunode_lpp5ta3"})
    return text, options
    
    
def menunode_lpp5ta3(caller):
    text = "You get 2 points in the social group. Second Point."
    options = ({"key": "0", "desc": "Empathy", "exec": addsheet(caller, 'Empathy', 'Skills', 1), "goto": "menunode_lpp5ta4"},
               {"key": "1", "desc": "Etiquette", "exec": addsheet(caller, 'Etiquette', 'Skills', 1), "goto": "menunode_lpp5ta4"},
               {"key": "2", "desc": "Influence", "exec": addsheet(caller, 'Influence', 'Skills', 1), "goto": "menunode_lpp5ta4"},
               {"key": "3", "desc": "Knavery", "exec": addsheet(caller, 'Knavery', 'Skills', 1), "goto": "menunode_lpp5ta4"},
               {"key": "4", "desc": "Leadership", "exec": addsheet(caller, 'Leadership', 'Skills', 1), "goto": "menunode_lpp5ta4"})
    return text, options
    
    
def menunode_lpp5ta4(caller):
    text = "You get 2 points in the malefaction group."
    options = ({"key": "0", "desc": "Lockpicking", "exec": addsheet(caller, 'Lockpicking', 'Skills', 1), "goto": "menunode_lpp5ta5"},
               {"key": "1", "desc": "Sleight of Hand", "exec": addsheet(caller, 'Sleight of Hand', 'Skills', 1), "goto": "menunode_lpp5ta5"},
               {"key": "2", "desc": "Sneak", "exec": addsheet(caller, 'Sneak', 'Skills', 1), "goto": "menunode_lpp5ta5"},
               {"key": "3", "desc": "Streetwise", "exec": addsheet(caller, 'Streetwise', 'Skills', 1), "goto": "menunode_lpp5ta5"},
               {"key": "4", "desc": "Torture", "exec": addsheet(caller, 'Torture', 'Skills', 1), "goto": "menunode_lpp5ta5"})
    return text, options
    
    
def menunode_lpp5ta5(caller):
    text = "You get 2 points in the malefaction group. Second Point."
    options = ({"key": "0", "desc": "Lockpicking", "exec": addsheet(caller, 'Lockpicking', 'Skills', 1), "goto": "menunode_lpp5cc"},
               {"key": "1", "desc": "Sleight of Hand", "exec": addsheet(caller, 'Sleight of Hand', 'Skills', 1), "goto": "menunode_lpp5cc"},
               {"key": "2", "desc": "Sneak", "exec": addsheet(caller, 'Sneak', 'Skills', 1), "goto": "menunode_lpp5cc"},
               {"key": "3", "desc": "Streetwise", "exec": addsheet(caller, 'Streetwise', 'Skills', 1), "goto": "menunode_lpp5cc"},
               {"key": "4", "desc": "Torture", "exec": addsheet(caller, 'Torture', 'Skills', 1), "goto": "menunode_lpp5cc"})
    return text, options
    
    
def menunode_lpp5eo02(caller):
    text = "You get 3 points in the Analytical group. Second Point."
    options = ({"key": "0", "desc": "Bureaucracy", "exec": addsheet(caller, 'Bureaucracy', 'Skills', 1), "goto": "menunode_lpp5eo03"},
               {"key": "1", "desc": "Investigation", "exec": addsheet(caller, 'Investigation', 'Skills', 1), "goto": "menunode_lpp5eo03"},
               {"key": "2", "desc": "Observe", "exec": addsheet(caller, 'Observe', 'Skills', 1), "goto": "menunode_lpp5eo03"},
               {"key": "3", "desc": "Physick", "exec": addsheet(caller, 'Physick', 'Skills', 1), "goto": "menunode_lpp5eo03"},
               {"key": "4", "desc": "Warfare", "exec": addsheet(caller, 'Warfare', 'Skills', 1), "goto": "menunode_lpp5eo03"})
    return text, options
    

def menunode_lpp5eo03(caller):
    text = "You get 3 points in the Analytical group. Third Point."
    options = ({"key": "0", "desc": "Bureaucracy", "exec": addsheet(caller, 'Bureaucracy', 'Skills', 1), "goto": "menunode_lpp5cc"},
               {"key": "1", "desc": "Investigation", "exec": addsheet(caller, 'Investigation', 'Skills', 1), "goto": "menunode_lpp5cc"},
               {"key": "2", "desc": "Observe", "exec": addsheet(caller, 'Observe', 'Skills', 1), "goto": "menunode_lpp5cc"},
               {"key": "3", "desc": "Physick", "exec": addsheet(caller, 'Physick', 'Skills', 1), "goto": "menunode_lpp5cc"},
               {"key": "4", "desc": "Warfare", "exec": addsheet(caller, 'Warfare', 'Skills', 1), "goto": "menunode_lpp5cc"})
    return text, options
    
    
def menunode_lpp5eo12(caller):
    text = "You get 2 points in the Analytical group. Second Point."
    options = ({"key": "0", "desc": "Bureaucracy", "exec": addsheet(caller, 'Bureaucracy', 'Skills', 1), "goto": "menunode_lpp5cc"},
               {"key": "1", "desc": "Investigation", "exec": addsheet(caller, 'Investigation', 'Skills', 1), "goto": "menunode_lpp5cc"},
               {"key": "2", "desc": "Observe", "exec": addsheet(caller, 'Observe', 'Skills', 1), "goto": "menunode_lpp5cc"},
               {"key": "3", "desc": "Physick", "exec": addsheet(caller, 'Physick', 'Skills', 1), "goto": "menunode_lpp5cc"},
               {"key": "4", "desc": "Warfare", "exec": addsheet(caller, 'Warfare', 'Skills', 1), "goto": "menunode_lpp5cc"})
    return text, options
    
    
def menunode_lpp5cc(caller):
    text = "Please select your early career."
    options = ({"key": "0", "desc": "Preacher/Pastor", "goto":"menunode_lpp6"},
               {"key": "1", "desc": "Monk", "goto":"menunode_lpp6"},
               {"key": "2", "desc": "Missionary", "goto":"menunode_lpp6"},
               {"key": "3", "desc": "Healer", "goto":"menunode_lpp6"},
               {"key": "4", "desc": "Inquisitor", "goto":"menunode_lpp6"})
    return text, options
    
    
def menunode_lpp6(caller, raw_input):
    apply_path_priest(caller, 1, int(raw_input), 'None')
    
    # Monk
    if int(raw_input) == 1:
        text = "What is your craft specialty?"
        options = ({"key": "_default", "goto": "menunode_lpp6m2"})
        return text, options
    # Missionary
    elif int(raw_input) == 2:
        text = "You have one point to spend in the control group."
        options = ({"key": "0", "desc": "Aircraft", "exec": addsheet(caller, 'Aircraft', 'Skills', 1), "goto": "menunode_lpp6cc"},
                   {"key": "1", "desc": "Beastcraft", "exec": addsheet(caller, 'Beastcraft', 'Skills', 1), "goto": "menunode_lpp6cc"},
                   {"key": "2", "desc": "Landcraft", "exec": addsheet(caller, 'Landcraft', 'Skills', 1), "goto": "menunode_lpp6cc"},
                   {"key": "3", "desc": "Watercraft", "exec": addsheet(caller, 'Watercraft', 'Skills', 1), "goto": "menunode_lpp6cc"},
                   {"key": "4", "desc": "Ride", "exec": addsheet(caller, 'Ride', 'Skills', 1), "goto": "menunode_lpp6cc"})
        return text, options
    # Inquisitor
    elif int(raw_input) == 4:
        text = "You get 2 points in the combat group."
        options = ({"key": "0", "desc": "Artifact Melee", "exec": addsheet(caller, 'Artifact Melee', 'Skills', 1), "goto": "menunode_lpp6i2"},
                   {"key": "1", "desc": "Archery", "exec": addsheet(caller, 'Archer', 'Skills', 1), "goto": "menunode_lpp6i2"},
                   {"key": "2", "desc": "Artillery", "exec": addsheet(caller, 'Artillery', 'Skills', 1), "goto": "menunode_lpp6i2"},
                   {"key": "3", "desc": "Demolitions", "exec": addsheet(caller, 'Demolitions', 'Skills', 1), "goto": "menunode_lpp6i2"},
                   {"key": "4", "desc": "Energy Guns", "exec": addsheet(caller, 'Energy Guns', 'Skills', 1), "goto": "menunode_lpp6i2"},
                   {"key": "5", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 1), "goto": "menunode_lpp6i2"},
                   {"key": "6", "desc": "Gunnery", "exec": addsheet(caller, 'Gunnery', 'Skills', 1), "goto": "menunode_lpp6i2"},
                   {"key": "7", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 1), "goto": "menunode_lpp6i2"},
                   {"key": "8", "desc": "Slug Guns", "exec": addsheet(caller, 'Slug Guns', 'Skills', 1), "goto": "menunode_lpp6i2"},
                   {"key": "9", "desc": "Throwing", "exec": addsheet(caller, 'Throwing', 'Skills', 1), "goto": "menunode_lpp6i2"})
        return text, options
        
    # TOUR OF DUTY
    
    
def menunode_lpp6m2(caller, raw_input):
    addsheet(caller, 'Craft ' + raw_input, 'Skills', 2)
    # TOUR OF DUTY
    
def menunode_lpp6i2(caller):
    text = "You get 2 points in the combat group. Second Point"
    options = ({"key": "0", "desc": "Artifact Melee", "exec": addsheet(caller, 'Artifact Melee', 'Skills', 1), "goto": "menunode_lpp6i3"},
               {"key": "1", "desc": "Archery", "exec": addsheet(caller, 'Archer', 'Skills', 1), "goto": "menunode_lpp6i3"},
               {"key": "2", "desc": "Artillery", "exec": addsheet(caller, 'Artillery', 'Skills', 1), "goto": "menunode_lpp6i3"},
               {"key": "3", "desc": "Demolitions", "exec": addsheet(caller, 'Demolitions', 'Skills', 1), "goto": "menunode_lpp6i3"},
               {"key": "4", "desc": "Energy Guns", "exec": addsheet(caller, 'Energy Guns', 'Skills', 1), "goto": "menunode_lpp6i3"},
               {"key": "5", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 1), "goto": "menunode_lpp6i3"},
               {"key": "6", "desc": "Gunnery", "exec": addsheet(caller, 'Gunnery', 'Skills', 1), "goto": "menunode_lpp6i3"},
               {"key": "7", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 1), "goto": "menunode_lpp6i3"},
               {"key": "8", "desc": "Slug Guns", "exec": addsheet(caller, 'Slug Guns', 'Skills', 1), "goto": "menunode_lpp6i3"},
               {"key": "9", "desc": "Throwing", "exec": addsheet(caller, 'Throwing', 'Skills', 1), "goto": "menunode_lpp6i3"})
    return text, options


def menunode_lpp6i3(caller):
    text = "You get 2 points in the malefaction group."
    options = ({"key": "0", "desc": "Lockpicking", "exec": addsheet(caller, 'Lockpicking', 'Skills', 1), "goto": "menunode_lpp6i4"},
               {"key": "1", "desc": "Sleight of Hand", "exec": addsheet(caller, 'Sleight of Hand', 'Skills', 1), "goto": "menunode_lpp6i4"},
               {"key": "2", "desc": "Sneak", "exec": addsheet(caller, 'Sneak', 'Skills', 1), "goto": "menunode_lpp6i4"},
               {"key": "3", "desc": "Streetwise", "exec": addsheet(caller, 'Streetwise', 'Skills', 1), "goto": "menunode_lpp6i4"},
               {"key": "4", "desc": "Torture", "exec": addsheet(caller, 'Torture', 'Skills', 1), "goto": "menunode_lpp6i4"})
    return text, options
    
def menunode_lpp6i4(caller):
    text = "You get 2 points in the malefaction group. Second Point."
    options = ({"key": "0", "desc": "Lockpicking", "exec": addsheet(caller, 'Lockpicking', 'Skills', 1), "goto": "menunode_lpp6cc"},
               {"key": "1", "desc": "Sleight of Hand", "exec": addsheet(caller, 'Sleight of Hand', 'Skills', 1), "goto": "menunode_lpp6cc"},
               {"key": "2", "desc": "Sneak", "exec": addsheet(caller, 'Sneak', 'Skills', 1), "goto": "menunode_lpp6cc"},
               {"key": "3", "desc": "Streetwise", "exec": addsheet(caller, 'Streetwise', 'Skills', 1), "goto": "menunode_lpp6cc"},
               {"key": "4", "desc": "Torture", "exec": addsheet(caller, 'Torture', 'Skills', 1), "goto": "menunode_lpp6cc"})
    return text, options
    
def menunode_lppbb(caller):
    addsheet(caller, 'Strength', 'Attributes', 5)
    addsheet(caller, 'Dexterity', 'Attributes', 5)
    addsheet(caller, 'Endurance', 'Attributes', 5)
    addsheet(caller, 'Will', 'Attributes', 1)
    addsheet(caller, 'Faith', 'Attributes', 4)
    addsheet(caller, 'Vigor', 'Skills', 3)
    addsheet(caller, 'Physick', 'Skills', 3)
    addsheet(caller, 'Self Control', 'Skills', 4)
    addsheet(caller, 'Survival', 'Skills', 1)
    addsheet(caller, 'Warfare', 'Skills', 1)
    addsheet(caller, 'Fight', 'Skills', 1)
    addsheet(caller, 'Melee', 'Skills', 1)
    caller.db.actions['Mantok'] = ["Soldier's Stance", 'Close Palm, Reach the Heart', 'Cross Arms, Don the Robe', 'Stretch Spine, Speak the Word']
    
    text = "You have 2 points to spend in the combat group."
    options = ({"key": "0", "desc": "Artifact Melee", "exec": addsheet(caller, 'Artifact Melee', 'Skills', 1), "goto": "menunode_lppbb2"},
               {"key": "1", "desc": "Archery", "exec": addsheet(caller, 'Archer', 'Skills', 1), "goto": "menunode_lppbb2"},
               {"key": "2", "desc": "Artillery", "exec": addsheet(caller, 'Artillery', 'Skills', 1), "goto": "menunode_lppbb2"},
               {"key": "3", "desc": "Demolitions", "exec": addsheet(caller, 'Demolitions', 'Skills', 1), "goto": "menunode_lppbb2"},
               {"key": "4", "desc": "Energy Guns", "exec": addsheet(caller, 'Energy Guns', 'Skills', 1), "goto": "menunode_lppbb2"},
               {"key": "5", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 1), "goto": "menunode_lppbb2"},
               {"key": "6", "desc": "Gunnery", "exec": addsheet(caller, 'Gunnery', 'Skills', 1), "goto": "menunode_lppbb2"},
               {"key": "7", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 1), "goto": "menunode_lppbb2"},
               {"key": "8", "desc": "Slug Guns", "exec": addsheet(caller, 'Slug Guns', 'Skills', 1), "goto": "menunode_lppbb2"},
               {"key": "9", "desc": "Throwing", "exec": addsheet(caller, 'Throwing', 'Skills', 1), "goto": "menunode_lppbb2"})
    return text, options
    
    
def menunode_lppbb2(caller):
    text = "You have 2 points to spend in the combat group. Second Point."
    options = ({"key": "0", "desc": "Artifact Melee", "exec": addsheet(caller, 'Artifact Melee', 'Skills', 1), "goto": "menunode_lppbb3"},
               {"key": "1", "desc": "Archery", "exec": addsheet(caller, 'Archer', 'Skills', 1), "goto": "menunode_lppbb3"},
               {"key": "2", "desc": "Artillery", "exec": addsheet(caller, 'Artillery', 'Skills', 1), "goto": "menunode_lppbb3"},
               {"key": "3", "desc": "Demolitions", "exec": addsheet(caller, 'Demolitions', 'Skills', 1), "goto": "menunode_lppbb3"},
               {"key": "4", "desc": "Energy Guns", "exec": addsheet(caller, 'Energy Guns', 'Skills', 1), "goto": "menunode_lppbb3"},
               {"key": "5", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 1), "goto": "menunode_lppbb3"},
               {"key": "6", "desc": "Gunnery", "exec": addsheet(caller, 'Gunnery', 'Skills', 1), "goto": "menunode_lppbb3"},
               {"key": "7", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 1), "goto": "menunode_lppbb3"},
               {"key": "8", "desc": "Slug Guns", "exec": addsheet(caller, 'Slug Guns', 'Skills', 1), "goto": "menunode_lppbb3"},
               {"key": "9", "desc": "Throwing", "exec": addsheet(caller, 'Throwing', 'Skills', 1), "goto": "menunode_lppbb3"})
    return text, options
    

def menunode_lppbb3(caller):
    text = "Do you want Fight or Melee +2?"
    options = ({"key": "0", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 2), "goto": "menunode_lppbb4"},
               {"key": "0", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 2), "goto": "menunode_lppbb4"})
    return text, options
    
    
def menunode_lppbb4(caller):
    text = "Pick a single combat skill to get +3."
    options = ({"key": "0", "desc": "Artifact Melee", "exec": addsheet(caller, 'Artifact Melee', 'Skills', 3), "goto": "menunode_lppbb5"},
               {"key": "1", "desc": "Archery", "exec": addsheet(caller, 'Archer', 'Skills', 3), "goto": "menunode_lppbb5"},
               {"key": "2", "desc": "Artillery", "exec": addsheet(caller, 'Artillery', 'Skills', 3), "goto": "menunode_lppbb5"},
               {"key": "3", "desc": "Demolitions", "exec": addsheet(caller, 'Demolitions', 'Skills', 3), "goto": "menunode_lppbb5"},
               {"key": "4", "desc": "Energy Guns", "exec": addsheet(caller, 'Energy Guns', 'Skills', 3), "goto": "menunode_lppbb5"},
               {"key": "5", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 3), "goto": "menunode_lppbb5"},
               {"key": "6", "desc": "Gunnery", "exec": addsheet(caller, 'Gunnery', 'Skills', 3), "goto": "menunode_lppbb5"},
               {"key": "7", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 3), "goto": "menunode_lppbb5"},
               {"key": "8", "desc": "Slug Guns", "exec": addsheet(caller, 'Slug Guns', 'Skills', 3), "goto": "menunode_lppbb5"},
               {"key": "9", "desc": "Throwing", "exec": addsheet(caller, 'Throwing', 'Skills', 3), "goto": "menunode_lppbb5"})
    return text, options
    

def menunode_lppbb5(caller):
    text = "Pick another fighting style to get."
    options = ({"key": "0", "desc": "Jox Kai Von", "goto": "menunode_lppbb6"},
               {"key": "1", "desc": "Koto", "goto": "menunode_lppbb6"},
               {"key": "2", "desc": "Iron Heel", "goto": "menunode_lppbb6"},
               {"key": "3", "desc": "Shaidan", "goto": "menunode_lppbb6"},
               {"key": "4", "desc": "Florentine", "goto": "menunode_lppbb6"},
               {"key": "5", "desc": "Kraxi Knife", "goto": "menunode_lppbb6"},
               {"key": "6", "desc": "Serpentis", "goto": "menunode_lppbb6"},
               {"key": "7", "desc": "Torero", "goto": "menunode_lppbb6"},
               {"key": "8", "desc": "Phoenix Rifle Corps Training", "goto": "menunode_lppbb6"},
               {"key": "9", "desc": "Pistola", "goto": "menunode_lppbb6"})
    return text, options
    
    
def menunode_lppbb6(caller, raw_input):
    if int(raw_input) == 0:
        caller.db.actions['Jox Kai Von'] = ['Jox Stance', 'Jab', 'Pound', 'Mantis Strike']
    elif int(raw_input) == 1:
        caller.db.actions['Koto'] = ['Koto Stance', 'Step to Sky', 'Jolo Bird Squawks', 'Old Lady Falls and Gets Up']
    elif int(raw_input) == 2:
        caller.db.actions['Iron Heel'] = ['Beatdown Stance', 'Chain of Destruction', 'Head-Butt', 'Choke Hold']
    elif int(raw_input) == 3:
        caller.db.actions['Shaidan'] = ['Balanced Stance', 'Royal Palm', 'Astride the Throne', 'Imperial Dance']
    elif int(raw_input) == 4:
        caller.db.actions['Florentine'] = ['Woven Steel', 'Off-Hand Strike', 'Double Strike', 'Wall of Steel']
    elif int(raw_input) == 5:
        caller.db.actions['Kraxi Knife'] = ['Focused Rage', 'Thrust', 'Rapid Strike', 'Slip of the Knife']
    elif int(raw_input) == 6:
        caller.db.actions['Serpentis'] = ['Weaving Fangs', 'Draw and Strike', 'Setup', 'Stop Thrust']
    elif int(raw_input) == 7:
        caller.db.actions['Torero'] = ['Faena', 'Masking Strike', 'Disarming Cloak', 'Entangling Cloak']
    elif int(raw_input) == 8:
        caller.db.actions['Phoenix Rifle Corps'] = ['Heads Down Stance', 'Practiced Shooting', 'Stock Slam', 'Instinct Shot']
    elif int(raw_input) == 9:
        caller.db.actions['Pistola'] = ['Criticorum Reload', 'Snap Shot', 'Roll and Shoot', 'Run and Gun']
        
    # TOUR OF DUTY
    
    
def menunode_lpp6cc(caller):
    pass

# END PRIEST SECTION

# BEGIN GUILD SECTION

def menunode_lpm1(caller):
    caller.db.archetype = "Merchant"
    caller.db.guild = 1
    
    text = "You have chosen to be a guild member or perhaps a yeoman. Please pick your guild below.\n"
    text += "If you want to be a yeoman but not mirror another guild please use custom cg."
    options = ({"key": "0", "desc": "Charioteers", "goto": "menunode_lpm2"},
               {"key": "1", "desc": "Engineers", "goto": "menunode_lpm2"},
               {"key": "2", "desc": "Scravers", "goto": "menunode_lpm2"},
               {"key": "3", "desc": "The Muster", "goto": "menunode_lpm2"},
               {"key": "4", "desc": "The Reeves", "goto": "menunode_lpm2"},
               {"key": "5", "desc": "Yeoman", "goto": "menunode_lpm12"})
    return text, options
    
    
def menunode_lpm12(caller):
    caller.db.house = "Yeoman"
    caller.db.minor = 1
    
    text = "Please select the guild you will mirror for lifepath selections."
    options = ({"key": "0", "desc": "Charioteers", "goto": "menunode_lpm2"},
               {"key": "1", "desc": "Engineers", "goto": "menunode_lpm2"},
               {"key": "2", "desc": "Scravers", "goto": "menunode_lpm2"},
               {"key": "3", "desc": "The Muster", "goto": "menunode_lpm2"},
               {"key": "4", "desc": "The Reeves", "goto": "menunode_lpm2"})
    return text, options
    
    
def menunode_lpm2(caller, raw_input):
    if caller.db.minor:
        caller.db.mirrorhouse = guildhelper[raw_input]
    else:
        caller.db.house = guildhelper[raw_input]
        addsheet(caller, 'Faction Lore.' + caller.db.house, 'Skills', 3)
        
    text = "Now you select an upbringing. Merchants have 2 factors to select. An environment and Class.\n"
    text += "Pick an environment."
    options = ({"key": "0", "desc": "City", "exec": apply_path_uppm(caller, 0, 0), "goto": "menunode_lpm3"},
               {"key": "1", "desc": "Town", "exec": apply_path_uppm(caller, 0, 1), "goto": "menunode_lpm3"},
               {"key": "2", "desc": "Country", "exec": apply_path_uppm(caller, 0, 2), "goto": "menunode_lpm3"},
               {"key": "3", "desc": "Space Habitat", "exec": apply_path_uppm(caller, 0, 3), "goto": "menunode_lpm3"})
    return text, options
    
    
def menunode_lpm3(caller):
    text = "The second part of your upbringing is a class. Pick one now."
    options = ({"key": "0", "desc": "Wealthy", "exec": apply_path_uppm(caller, 1, 0), "goto": "menunode_lpm31"},
               {"key": "1", "desc": "Middle", "exec": apply_path_uppm(caller, 1, 1), "goto": "menunode_lpm32"},
               {"key": "2", "desc": "Poor", "exec": apply_path_uppm(caller, 1, 2), "goto": "menunode_lpm33"})
    return text, options
    
    
def menunode_lpm31(caller):
    text = "You get 1 point in the social group."
    options = ({"key": "0", "desc": "Empathy", "exec": addsheet(caller, 'Empathy', 'Skills', 1), "goto": "menunode_lpm4"},
               {"key": "1", "desc": "Etiquette", "exec": addsheet(caller, 'Etiquette', 'Skills', 1), "goto": "menunode_lpm4"},
               {"key": "2", "desc": "Influence", "exec": addsheet(caller, 'Influence', 'Skills', 1), "goto": "menunode_lpm4"},
               {"key": "3", "desc": "Knavery", "exec": addsheet(caller, 'Knavery', 'Skills', 1), "goto": "menunode_lpm4"},
               {"key": "4", "desc": "Leadership", "exec": addsheet(caller, 'Leadership', 'Skills', 1), "goto": "menunode_lpm4"})
    return text, options
    
def menunode_lpm32(caller):
    text = "Pick your craft specialty."
    options = ({"key": "_default", "goto": "menunode_lpm322"})
    return text, options
    
    
def menunode_lpm322(caller, raw_input):
    addsheet(caller, 'Craft ' + raw_input, 'Skills', 1)
    # APPRENTICESHIP
    
    
def menunode_lpm33(caller):
    text = "You get 1 pointi n the malefaction group."
    options = ({"key": "0", "desc": "Lockpicking", "exec": addsheet(caller, 'Lockpicking', 'Skills', 1), "goto": "menunode_lpm4"},
               {"key": "1", "desc": "Sleight of Hand", "exec": addsheet(caller, 'Sleight of Hand', 'Skills', 1), "goto": "menunode_lpm4"},
               {"key": "2", "desc": "Sneak", "exec": addsheet(caller, 'Sneak', 'Skills', 1), "goto": "menunode_lpm4"},
               {"key": "3", "desc": "Streetwise", "exec": addsheet(caller, 'Streetwise', 'Skills', 1), "goto": "menunode_lpm4"},
               {"key": "4", "desc": "Torture", "exec": addsheet(caller, 'Torture', 'Skills', 1), "goto": "menunode_lpm4"})
    return text, options
    
    
def menunode_lpm4(caller):
    text = "Now you will pick an apprenticeship."
    options = ({"key": "0", "desc": "Academy", "goto": "menunode_lpm5"},
               {"key": "1", "desc": "Guild Hall", "goto": "menunode_lpm5"},
               {"key": "2", "desc": "The Streets", "goto": "menunode_lpm5"})
               
    if caller.db.minor: # no academy for yeoman
        options = [x for x in options if x['key'] != '0']
        
    return text, options
    
    
def menunode_lpm5(caller, raw_input):
    if caller.db.minor:
        apply_path_guild(caller, 0, int(raw_input), caller.db.mirrorhouse)
    else:
        apply_path_guild(caller, 0, int(raw_input), caller.db.house)
        
    if int(raw_input) == 0:  # Academy
        
        if caller.db.house == "Charioteers" or caller.db.mirrorhouse == "Charioteers":
            text = "You get 3 points in the control group."
            options = ({"key": "0", "desc": "Aircraft", "exec": addsheet(caller, 'Aircraft', 'Skills', 1), "goto": "menunode_lpm5c02"},
                       {"key": "1", "desc": "Beastcraft", "exec": addsheet(caller, 'Beastcraft', 'Skills', 1), "goto": "menunode_lpm5c02"},
                       {"key": "2", "desc": "Landcraft", "exec": addsheet(caller, 'Landcraft', 'Skills', 1), "goto": "menunode_lpm5c02"},
                       {"key": "3", "desc": "Watercraft", "exec": addsheet(caller, 'Watercraft', 'Skills', 1), "goto": "menunode_lpm5c02"},
                       {"key": "4", "desc": "Ride", "exec": addsheet(caller, 'Ride', 'Skills', 1), "goto": "menunode_lpm5c02"})
            return text, options
        elif caller.db.house == "Engineers" or caller.db.mirrorhouse == "Engineers":
            text = "You get 2 points in the science group."
            options = ({"key": "0", "desc": "Applied Science", "exec": addsheet(caller, 'Applied Science', 'Skills', 1), "goto": "menunode_lpm5e02"},
                       {"key": "1", "desc": "Life Science", "exec": addsheet(caller, 'Life Science', 'Skills', 1), "goto": "menunode_lpm5e02"},
                       {"key": "2", "desc": "Social Science", "exec": addsheet(caller, 'Social Science', 'Skills', 1), "goto": "menunode_lpm5e02"},
                       {"key": "3", "desc": "Physical Science", "exec": addsheet(caller, 'Physical Science', 'Skills', 1), "goto": "menunode_lpm5e02"},
                       {"key": "4", "desc": "Terraforming", "exec": addsheet(caller, 'Terraforming', 'Skills', 1), "goto": "menunode_lpm5e02"})
            return text, options
        elif caller.db.house == "Scravers" or caller.db.mirrorhouse == "Scravers":
            text = "You get 1 point in the combat group."
            options = ({"key": "0", "desc": "Artifact Melee", "exec": addsheet(caller, 'Artifact Melee', 'Skills', 1), "goto": "menunode_lpm5s02"},
                       {"key": "1", "desc": "Archery", "exec": addsheet(caller, 'Archer', 'Skills', 1), "goto": "menunode_lpm5s02"},
                       {"key": "2", "desc": "Artillery", "exec": addsheet(caller, 'Artillery', 'Skills', 1), "goto": "menunode_lpm5s02"},
                       {"key": "3", "desc": "Demolitions", "exec": addsheet(caller, 'Demolitions', 'Skills', 1), "goto": "menunode_lpm5s02"},
                       {"key": "4", "desc": "Energy Guns", "exec": addsheet(caller, 'Energy Guns', 'Skills', 1), "goto": "menunode_lpm5s02"},
                       {"key": "5", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 1), "goto": "menunode_lpm5s02"},
                       {"key": "6", "desc": "Gunnery", "exec": addsheet(caller, 'Gunnery', 'Skills', 1), "goto": "menunode_lpm5s02"},
                       {"key": "7", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 1), "goto": "menunode_lpm5s02"},
                       {"key": "8", "desc": "Slug Guns", "exec": addsheet(caller, 'Slug Guns', 'Skills', 1), "goto": "menunode_lpm5s02"},
                       {"key": "9", "desc": "Throwing", "exec": addsheet(caller, 'Throwing', 'Skills', 1), "goto": "menunode_lpm5s02"})
            return text, options
        elif caller.db.house == "Muster" or caller.db.mirrorhouse == "Muster":
            text = "You get 3 points in the combat group."
            options = ({"key": "0", "desc": "Artifact Melee", "exec": addsheet(caller, 'Artifact Melee', 'Skills', 1), "goto": "menunode_lpm5m02"},
                       {"key": "1", "desc": "Archery", "exec": addsheet(caller, 'Archer', 'Skills', 1), "goto": "menunode_lpm5m02"},
                       {"key": "2", "desc": "Artillery", "exec": addsheet(caller, 'Artillery', 'Skills', 1), "goto": "menunode_lpm5m02"},
                       {"key": "3", "desc": "Demolitions", "exec": addsheet(caller, 'Demolitions', 'Skills', 1), "goto": "menunode_lpm5m02"},
                       {"key": "4", "desc": "Energy Guns", "exec": addsheet(caller, 'Energy Guns', 'Skills', 1), "goto": "menunode_lpm5m02"},
                       {"key": "5", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 1), "goto": "menunode_lpm5m02"},
                       {"key": "6", "desc": "Gunnery", "exec": addsheet(caller, 'Gunnery', 'Skills', 1), "goto": "menunode_lpm5m02"},
                       {"key": "7", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 1), "goto": "menunode_lpm5m02"},
                       {"key": "8", "desc": "Slug Guns", "exec": addsheet(caller, 'Slug Guns', 'Skills', 1), "goto": "menunode_lpm5m02"},
                       {"key": "9", "desc": "Throwing", "exec": addsheet(caller, 'Throwing', 'Skills', 1), "goto": "menunode_lpm5m02"})
            return text, options
        
    elif int(raw_input) == 1: # Guild Hall
        
        if caller.db.house == "Charioteers" or caller.db.mirrorhouse == "Charioteers":
            text = "You get 3 points in the control group."
            options = ({"key": "0", "desc": "Aircraft", "exec": addsheet(caller, 'Aircraft', 'Skills', 1), "goto": "menunode_lpm5c12"},
                       {"key": "1", "desc": "Beastcraft", "exec": addsheet(caller, 'Beastcraft', 'Skills', 1), "goto": "menunode_lpm5c12"},
                       {"key": "2", "desc": "Landcraft", "exec": addsheet(caller, 'Landcraft', 'Skills', 1), "goto": "menunode_lpm5c12"},
                       {"key": "3", "desc": "Watercraft", "exec": addsheet(caller, 'Watercraft', 'Skills', 1), "goto": "menunode_lpm5c12"},
                       {"key": "4", "desc": "Ride", "exec": addsheet(caller, 'Ride', 'Skills', 1), "goto": "menunode_lpm5c12"})
            return text, options
        elif caller.db.house == "Engineers" or caller.db.mirrorhouse == "Engineers":
            text = "You get 1 point in the combat group."
            options = ({"key": "0", "desc": "Artifact Melee", "exec": addsheet(caller, 'Artifact Melee', 'Skills', 1), "goto": "menunode_lpm5e12"},
                       {"key": "1", "desc": "Archery", "exec": addsheet(caller, 'Archer', 'Skills', 1), "goto": "menunode_lpm5e12"},
                       {"key": "2", "desc": "Artillery", "exec": addsheet(caller, 'Artillery', 'Skills', 1), "goto": "menunode_lpm5e12"},
                       {"key": "3", "desc": "Demolitions", "exec": addsheet(caller, 'Demolitions', 'Skills', 1), "goto": "menunode_lpm5e12"},
                       {"key": "4", "desc": "Energy Guns", "exec": addsheet(caller, 'Energy Guns', 'Skills', 1), "goto": "menunode_lpm5e12"},
                       {"key": "5", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 1), "goto": "menunode_lpm5e12"},
                       {"key": "6", "desc": "Gunnery", "exec": addsheet(caller, 'Gunnery', 'Skills', 1), "goto": "menunode_lpm5e12"},
                       {"key": "7", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 1), "goto": "menunode_lpm5e12"},
                       {"key": "8", "desc": "Slug Guns", "exec": addsheet(caller, 'Slug Guns', 'Skills', 1), "goto": "menunode_lpm5e12"},
                       {"key": "9", "desc": "Throwing", "exec": addsheet(caller, 'Throwing', 'Skills', 1), "goto": "menunode_lpm5e12"})
            return text, options
        elif caller.db.house == "Scravers" or caller.db.mirrorhouse == "Scravers":
            text = "You get 1 point in the combat group."
            options = ({"key": "0", "desc": "Artifact Melee", "exec": addsheet(caller, 'Artifact Melee', 'Skills', 1), "goto": "menunode_lpm5s12"},
                       {"key": "1", "desc": "Archery", "exec": addsheet(caller, 'Archer', 'Skills', 1), "goto": "menunode_lpm5s12"},
                       {"key": "2", "desc": "Artillery", "exec": addsheet(caller, 'Artillery', 'Skills', 1), "goto": "menunode_lpm5s12"},
                       {"key": "3", "desc": "Demolitions", "exec": addsheet(caller, 'Demolitions', 'Skills', 1), "goto": "menunode_lpm5s12"},
                       {"key": "4", "desc": "Energy Guns", "exec": addsheet(caller, 'Energy Guns', 'Skills', 1), "goto": "menunode_lpm5s12"},
                       {"key": "5", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 1), "goto": "menunode_lpm5s12"},
                       {"key": "6", "desc": "Gunnery", "exec": addsheet(caller, 'Gunnery', 'Skills', 1), "goto": "menunode_lpm5s12"},
                       {"key": "7", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 1), "goto": "menunode_lpm5s12"},
                       {"key": "8", "desc": "Slug Guns", "exec": addsheet(caller, 'Slug Guns', 'Skills', 1), "goto": "menunode_lpm5s12"},
                       {"key": "9", "desc": "Throwing", "exec": addsheet(caller, 'Throwing', 'Skills', 1), "goto": "menunode_lpm5s12"})
            return text, options
        elif caller.db.house == "Muster" or caller.db.mirrorhouse == "Muster":
            text = "You get 2 points in the combat group."
            options = ({"key": "0", "desc": "Artifact Melee", "exec": addsheet(caller, 'Artifact Melee', 'Skills', 1), "goto": "menunode_lpm5m12"},
                       {"key": "1", "desc": "Archery", "exec": addsheet(caller, 'Archer', 'Skills', 1), "goto": "menunode_lpm5m12"},
                       {"key": "2", "desc": "Artillery", "exec": addsheet(caller, 'Artillery', 'Skills', 1), "goto": "menunode_lpm5m12"},
                       {"key": "3", "desc": "Demolitions", "exec": addsheet(caller, 'Demolitions', 'Skills', 1), "goto": "menunode_lpm5m12"},
                       {"key": "4", "desc": "Energy Guns", "exec": addsheet(caller, 'Energy Guns', 'Skills', 1), "goto": "menunode_lpm5m12"},
                       {"key": "5", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 1), "goto": "menunode_lpm5m12"},
                       {"key": "6", "desc": "Gunnery", "exec": addsheet(caller, 'Gunnery', 'Skills', 1), "goto": "menunode_lpm5m12"},
                       {"key": "7", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 1), "goto": "menunode_lpm5m12"},
                       {"key": "8", "desc": "Slug Guns", "exec": addsheet(caller, 'Slug Guns', 'Skills', 1), "goto": "menunode_lpm5m12"},
                       {"key": "9", "desc": "Throwing", "exec": addsheet(caller, 'Throwing', 'Skills', 1), "goto": "menunode_lpm5m12"})
            return text, options
        
    elif int(raw_input) == 2: # streets
        
        if caller.db.house == "Charioteers" or caller.db.mirrorhouse == "Charioteers":
            text = "You get 2 points in the control group."
            options = ({"key": "0", "desc": "Aircraft", "exec": addsheet(caller, 'Aircraft', 'Skills', 1), "goto": "menunode_lpm5c22"},
                       {"key": "1", "desc": "Beastcraft", "exec": addsheet(caller, 'Beastcraft', 'Skills', 1), "goto": "menunode_lpm5c22"},
                       {"key": "2", "desc": "Landcraft", "exec": addsheet(caller, 'Landcraft', 'Skills', 1), "goto": "menunode_lpm5c22"},
                       {"key": "3", "desc": "Watercraft", "exec": addsheet(caller, 'Watercraft', 'Skills', 1), "goto": "menunode_lpm5c22"},
                       {"key": "4", "desc": "Ride", "exec": addsheet(caller, 'Ride', 'Skills', 1), "goto": "menunode_lpm5c22"})
            return text, options
        elif caller.db.house == "Engineers" or caller.db.mirrorhouse == "Engineers":
            text = "You get 2 points in the science group.."
            options = ({"key": "0", "desc": "Applied Science", "exec": addsheet(caller, 'Applied Science', 'Skills', 1), "goto": "menunode_lpm5e22"},
                       {"key": "1", "desc": "Life Science", "exec": addsheet(caller, 'Life Science', 'Skills', 1), "goto": "menunode_lpm5e22"},
                       {"key": "2", "desc": "Social Science", "exec": addsheet(caller, 'Social Science', 'Skills', 1), "goto": "menunode_lpm5e22"},
                       {"key": "3", "desc": "Physical Science", "exec": addsheet(caller, 'Physical Science', 'Skills', 1), "goto": "menunode_lpm5e22"},
                       {"key": "4", "desc": "Terraforming", "exec": addsheet(caller, 'Terraforming', 'Skills', 1), "goto": "menunode_lpm5e22"})
            return text, options
        elif caller.db.house == "Scravers" or caller.db.mirrorhouse == "Scravers":
            text = "You get 3 points in the malefaction group."
            options = ({"key": "0", "desc": "Lockpicking", "exec": addsheet(caller, 'Lockpicking', 'Skills', 1), "goto": "menunode_lpm5s22"},
                       {"key": "1", "desc": "Sleight of Hand", "exec": addsheet(caller, 'Sleight of Hand', 'Skills', 1), "goto": "menunode_lpm5s22"},
                       {"key": "2", "desc": "Sneak", "exec": addsheet(caller, 'Sneak', 'Skills', 1), "goto": "menunode_lpm5s22"},
                       {"key": "3", "desc": "Streetwise", "exec": addsheet(caller, 'Streetwise', 'Skills', 1), "goto": "menunode_lpm5s22"},
                       {"key": "4", "desc": "Torture", "exec": addsheet(caller, 'Torture', 'Skills', 1), "goto": "menunode_lpm5s22"})
            return text, options
        elif caller.db.house == "Muster" or caller.db.mirrorhouse == "Muster":
            text = "You get 2 points in the combat group."
            options = ({"key": "0", "desc": "Artifact Melee", "exec": addsheet(caller, 'Artifact Melee', 'Skills', 1), "goto": "menunode_lpm5m22"},
                       {"key": "1", "desc": "Archery", "exec": addsheet(caller, 'Archer', 'Skills', 1), "goto": "menunode_lpm5m22"},
                       {"key": "2", "desc": "Artillery", "exec": addsheet(caller, 'Artillery', 'Skills', 1), "goto": "menunode_lpm5m22"},
                       {"key": "3", "desc": "Demolitions", "exec": addsheet(caller, 'Demolitions', 'Skills', 1), "goto": "menunode_lpm5m22"},
                       {"key": "4", "desc": "Energy Guns", "exec": addsheet(caller, 'Energy Guns', 'Skills', 1), "goto": "menunode_lpm5m22"},
                       {"key": "5", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 1), "goto": "menunode_lpm5m22"},
                       {"key": "6", "desc": "Gunnery", "exec": addsheet(caller, 'Gunnery', 'Skills', 1), "goto": "menunode_lpm5m22"},
                       {"key": "7", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 1), "goto": "menunode_lpm5m22"},
                       {"key": "8", "desc": "Slug Guns", "exec": addsheet(caller, 'Slug Guns', 'Skills', 1), "goto": "menunode_lpm5m22"},
                       {"key": "9", "desc": "Throwing", "exec": addsheet(caller, 'Throwing', 'Skills', 1), "goto": "menunode_lpm5m22"})
            return text, options
        elif caller.db.house == "Reeves" or caller.db.mirrorhouse == "Reeves":
            text = "You get 1 point in the combat group."
            options = ({"key": "0", "desc": "Artifact Melee", "exec": addsheet(caller, 'Artifact Melee', 'Skills', 1), "goto": "menunode_lpm5r22"},
                       {"key": "1", "desc": "Archery", "exec": addsheet(caller, 'Archer', 'Skills', 1), "goto": "menunode_lpm5r22"},
                       {"key": "2", "desc": "Artillery", "exec": addsheet(caller, 'Artillery', 'Skills', 1), "goto": "menunode_lpm5r22"},
                       {"key": "3", "desc": "Demolitions", "exec": addsheet(caller, 'Demolitions', 'Skills', 1), "goto": "menunode_lpm5r22"},
                       {"key": "4", "desc": "Energy Guns", "exec": addsheet(caller, 'Energy Guns', 'Skills', 1), "goto": "menunode_lpm5r22"},
                       {"key": "5", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 1), "goto": "menunode_lpm5r22"},
                       {"key": "6", "desc": "Gunnery", "exec": addsheet(caller, 'Gunnery', 'Skills', 1), "goto": "menunode_lpm5r22"},
                       {"key": "7", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 1), "goto": "menunode_lpm5r22"},
                       {"key": "8", "desc": "Slug Guns", "exec": addsheet(caller, 'Slug Guns', 'Skills', 1), "goto": "menunode_lpm5r22"},
                       {"key": "9", "desc": "Throwing", "exec": addsheet(caller, 'Throwing', 'Skills', 1), "goto": "menunode_lpm5r22"})
            return text, options
            
    text = "Select your early career."
    options = ({"key": "0", "desc": "Merchant", "goto": "menunode_lpm6"},
               {"key": "1", "desc": "Money-Lender", "goto": "menunode_lpm6"},
               {"key": "2", "desc": "Pilot", "goto": "menunode_lpm6"},
               {"key": "3", "desc": "Engineer", "goto": "menunode_lpm6"},
               {"key": "4", "desc": "Gunner", "goto": "menunode_lpm6"},
               {"key": "5", "desc": "Soldier", "goto": "menunode_lpm6"},
               {"key": "6", "desc": "Combat Engineer", "goto": "menunode_lpm6"},
               {"key": "7", "desc": "Scholar", "goto": "menunode_lpm6"},
               {"key": "8", "desc": "Scientist", "goto": "menunode_lpm6"},
               {"key": "9", "desc": "Thief", "goto": "menunode_lpm6"},
               {"key": "10", "desc": "Spy", "goto": "menunode_lpm6"})
    return text, options
    
    
def menunode_lpm5c02(caller):
    text = "Second point in control group."
    options = ({"key": "0", "desc": "Aircraft", "exec": addsheet(caller, 'Aircraft', 'Skills', 1), "goto": "menunode_lpm5c03"},
               {"key": "1", "desc": "Beastcraft", "exec": addsheet(caller, 'Beastcraft', 'Skills', 1), "goto": "menunode_lpm5c03"},
               {"key": "2", "desc": "Landcraft", "exec": addsheet(caller, 'Landcraft', 'Skills', 1), "goto": "menunode_lpm5c03"},
               {"key": "3", "desc": "Watercraft", "exec": addsheet(caller, 'Watercraft', 'Skills', 1), "goto": "menunode_lpm5c03"},
               {"key": "4", "desc": "Ride", "exec": addsheet(caller, 'Ride', 'Skills', 1), "goto": "menunode_lpm5c03"})
    return text, options

    
def menunode_lpm5c03(caller):
    text = "Third point in control group."
    options = ({"key": "0", "desc": "Aircraft", "exec": addsheet(caller, 'Aircraft', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "1", "desc": "Beastcraft", "exec": addsheet(caller, 'Beastcraft', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "2", "desc": "Landcraft", "exec": addsheet(caller, 'Landcraft', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "3", "desc": "Watercraft", "exec": addsheet(caller, 'Watercraft', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "4", "desc": "Ride", "exec": addsheet(caller, 'Ride', 'Skills', 1), "goto": "menunode_lpm5cc"})
    return text, options
    
    
def menunode_lpm5e02(caller):
    text = "You get 2 points in the science group. Second Point."
    options = ({"key": "0", "desc": "Applied Science", "exec": addsheet(caller, 'Applied Science', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "1", "desc": "Life Science", "exec": addsheet(caller, 'Life Science', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "2", "desc": "Social Science", "exec": addsheet(caller, 'Social Science', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "3", "desc": "Physical Science", "exec": addsheet(caller, 'Physical Science', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "4", "desc": "Terraforming", "exec": addsheet(caller, 'Terraforming', 'Skills', 1), "goto": "menunode_lpm5cc"})
    return text, options
    

def menunode_lpm5s02(caller):
    text = "You now get 3 points in the malefaction group."
    options = ({"key": "0", "desc": "Lockpicking", "exec": addsheet(caller, 'Lockpicking', 'Skills', 1), "goto": "menunode_lpm5s03"},
               {"key": "1", "desc": "Sleight of Hand", "exec": addsheet(caller, 'Sleight of Hand', 'Skills', 1), "goto": "menunode_lpm5s03"},
               {"key": "2", "desc": "Sneak", "exec": addsheet(caller, 'Sneak', 'Skills', 1), "goto": "menunode_lpm5s03"},
               {"key": "3", "desc": "Streetwise", "exec": addsheet(caller, 'Streetwise', 'Skills', 1), "goto": "menunode_lpm5s03"},
               {"key": "4", "desc": "Torture", "exec": addsheet(caller, 'Torture', 'Skills', 1), "goto": "menunode_lpm5s03"})
    return text, options
    
    
def menunode_lpm5s03(caller):
    text = "You now get 3 points in the malefaction group. Second Point."
    options = ({"key": "0", "desc": "Lockpicking", "exec": addsheet(caller, 'Lockpicking', 'Skills', 1), "goto": "menunode_lpm5s04"},
               {"key": "1", "desc": "Sleight of Hand", "exec": addsheet(caller, 'Sleight of Hand', 'Skills', 1), "goto": "menunode_lpm5s04"},
               {"key": "2", "desc": "Sneak", "exec": addsheet(caller, 'Sneak', 'Skills', 1), "goto": "menunode_lpm5s04"},
               {"key": "3", "desc": "Streetwise", "exec": addsheet(caller, 'Streetwise', 'Skills', 1), "goto": "menunode_lpm5s04"},
               {"key": "4", "desc": "Torture", "exec": addsheet(caller, 'Torture', 'Skills', 1), "goto": "menunode_lpm5s04"})
    return text, options
    
    
def menunode_lpm5s04(caller):
    text = "You now get 3 points in the malefaction group. Third Point."
    options = ({"key": "0", "desc": "Lockpicking", "exec": addsheet(caller, 'Lockpicking', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "1", "desc": "Sleight of Hand", "exec": addsheet(caller, 'Sleight of Hand', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "2", "desc": "Sneak", "exec": addsheet(caller, 'Sneak', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "3", "desc": "Streetwise", "exec": addsheet(caller, 'Streetwise', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "4", "desc": "Torture", "exec": addsheet(caller, 'Torture', 'Skills', 1), "goto": "menunode_lpm5cc"})
    return text, options
    
    
def menunode_lpm5m02(caller):
    text = "Combat point 2."
    options = ({"key": "0", "desc": "Artifact Melee", "exec": addsheet(caller, 'Artifact Melee', 'Skills', 1), "goto": "menunode_lpm5m03"},
               {"key": "1", "desc": "Archery", "exec": addsheet(caller, 'Archer', 'Skills', 1), "goto": "menunode_lpm5m03"},
               {"key": "2", "desc": "Artillery", "exec": addsheet(caller, 'Artillery', 'Skills', 1), "goto": "menunode_lpm5m03"},
               {"key": "3", "desc": "Demolitions", "exec": addsheet(caller, 'Demolitions', 'Skills', 1), "goto": "menunode_lpm5m03"},
               {"key": "4", "desc": "Energy Guns", "exec": addsheet(caller, 'Energy Guns', 'Skills', 1), "goto": "menunode_lpm5m03"},
               {"key": "5", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 1), "goto": "menunode_lpm5m03"},
               {"key": "6", "desc": "Gunnery", "exec": addsheet(caller, 'Gunnery', 'Skills', 1), "goto": "menunode_lpm5m03"},
               {"key": "7", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 1), "goto": "menunode_lpm5m03"},
               {"key": "8", "desc": "Slug Guns", "exec": addsheet(caller, 'Slug Guns', 'Skills', 1), "goto": "menunode_lpm5m03"},
               {"key": "9", "desc": "Throwing", "exec": addsheet(caller, 'Throwing', 'Skills', 1), "goto": "menunode_lpm5m03"})
    return text, options
    
    
def menunode_lpm5m03(caller):
    text = "Combat point 3."
    options = ({"key": "0", "desc": "Artifact Melee", "exec": addsheet(caller, 'Artifact Melee', 'Skills', 1), "goto": "menunode_lpm5m04"},
               {"key": "1", "desc": "Archery", "exec": addsheet(caller, 'Archer', 'Skills', 1), "goto": "menunode_lpm5m04"},
               {"key": "2", "desc": "Artillery", "exec": addsheet(caller, 'Artillery', 'Skills', 1), "goto": "menunode_lpm5m04"},
               {"key": "3", "desc": "Demolitions", "exec": addsheet(caller, 'Demolitions', 'Skills', 1), "goto": "menunode_lpm5m04"},
               {"key": "4", "desc": "Energy Guns", "exec": addsheet(caller, 'Energy Guns', 'Skills', 1), "goto": "menunode_lpm5m04"},
               {"key": "5", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 1), "goto": "menunode_lpm5m04"},
               {"key": "6", "desc": "Gunnery", "exec": addsheet(caller, 'Gunnery', 'Skills', 1), "goto": "menunode_lpm5m04"},
               {"key": "7", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 1), "goto": "menunode_lpm5m04"},
               {"key": "8", "desc": "Slug Guns", "exec": addsheet(caller, 'Slug Guns', 'Skills', 1), "goto": "menunode_lpm5m04"},
               {"key": "9", "desc": "Throwing", "exec": addsheet(caller, 'Throwing', 'Skills', 1), "goto": "menunode_lpm5m04"})
    return text, options
    
    
def menunode_lpm5m04(caller):
    text = "You get 2 points in the control group."
    options = ({"key": "0", "desc": "Aircraft", "exec": addsheet(caller, 'Aircraft', 'Skills', 1), "goto": "menunode_lpm5m05"},
               {"key": "1", "desc": "Beastcraft", "exec": addsheet(caller, 'Beastcraft', 'Skills', 1), "goto": "menunode_lpm5m05"},
               {"key": "2", "desc": "Landcraft", "exec": addsheet(caller, 'Landcraft', 'Skills', 1), "goto": "menunode_lpm5m05"},
               {"key": "3", "desc": "Watercraft", "exec": addsheet(caller, 'Watercraft', 'Skills', 1), "goto": "menunode_lpm5m05"},
               {"key": "4", "desc": "Ride", "exec": addsheet(caller, 'Ride', 'Skills', 1), "goto": "menunode_lpm5m05"})
    return text, options
    
    
def menunode_lpm5m05(caller):
    text = "Second control point."
    options = ({"key": "0", "desc": "Aircraft", "exec": addsheet(caller, 'Aircraft', 'Skills', 1), "goto": "menunode_lpm5m06"},
               {"key": "1", "desc": "Beastcraft", "exec": addsheet(caller, 'Beastcraft', 'Skills', 1), "goto": "menunode_lpm5m06"},
               {"key": "2", "desc": "Landcraft", "exec": addsheet(caller, 'Landcraft', 'Skills', 1), "goto": "menunode_lpm5m06"},
               {"key": "3", "desc": "Watercraft", "exec": addsheet(caller, 'Watercraft', 'Skills', 1), "goto": "menunode_lpm5m06"},
               {"key": "4", "desc": "Ride", "exec": addsheet(caller, 'Ride', 'Skills', 1), "goto": "menunode_lpm5m06"})
    return text, options
    

def menunode_lpm5m06(caller):
    text = "You now get 1 point in the malefaction group."
    options = ({"key": "0", "desc": "Lockpicking", "exec": addsheet(caller, 'Lockpicking', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "1", "desc": "Sleight of Hand", "exec": addsheet(caller, 'Sleight of Hand', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "2", "desc": "Sneak", "exec": addsheet(caller, 'Sneak', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "3", "desc": "Streetwise", "exec": addsheet(caller, 'Streetwise', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "4", "desc": "Torture", "exec": addsheet(caller, 'Torture', 'Skills', 1), "goto": "menunode_lpm5cc"})
    return text, options
    
def menunode_lpm5c12(caller):
    text = "Second Control Point."
    options = ({"key": "0", "desc": "Aircraft", "exec": addsheet(caller, 'Aircraft', 'Skills', 1), "goto": "menunode_lpm5c13"},
               {"key": "1", "desc": "Beastcraft", "exec": addsheet(caller, 'Beastcraft', 'Skills', 1), "goto": "menunode_lpm5c13"},
               {"key": "2", "desc": "Landcraft", "exec": addsheet(caller, 'Landcraft', 'Skills', 1), "goto": "menunode_lpm5c13"},
               {"key": "3", "desc": "Watercraft", "exec": addsheet(caller, 'Watercraft', 'Skills', 1), "goto": "menunode_lpm5c13"},
               {"key": "4", "desc": "Ride", "exec": addsheet(caller, 'Ride', 'Skills', 1), "goto": "menunode_lpm5c13"})
    return text, options
    
def menunode_lpm5c13(caller):
    text = "Third Control Point."
    options = ({"key": "0", "desc": "Aircraft", "exec": addsheet(caller, 'Aircraft', 'Skills', 1), "goto": "menunode_lpm5c14"},
               {"key": "1", "desc": "Beastcraft", "exec": addsheet(caller, 'Beastcraft', 'Skills', 1), "goto": "menunode_lpm5c14"},
               {"key": "2", "desc": "Landcraft", "exec": addsheet(caller, 'Landcraft', 'Skills', 1), "goto": "menunode_lpm5c14"},
               {"key": "3", "desc": "Watercraft", "exec": addsheet(caller, 'Watercraft', 'Skills', 1), "goto": "menunode_lpm5c14"},
               {"key": "4", "desc": "Ride", "exec": addsheet(caller, 'Ride', 'Skills', 1), "goto": "menunode_lpm5c14"})
    return text, options
    

def menunode_lpm5c14(caller):
    text = "You get 1 point in the social group."
    options = ({"key": "0", "desc": "Empathy", "exec": addsheet(caller, 'Empathy', 'Skills', 1), "goto": "menunode_lpm5c15"},
               {"key": "1", "desc": "Etiquette", "exec": addsheet(caller, 'Etiquette', 'Skills', 1), "goto": "menunode_lpm5c15"},
               {"key": "2", "desc": "Influence", "exec": addsheet(caller, 'Influence', 'Skills', 1), "goto": "menunode_lpm5c15"},
               {"key": "3", "desc": "Knavery", "exec": addsheet(caller, 'Knavery', 'Skills', 1), "goto": "menunode_lpm5c15"},
               {"key": "4", "desc": "Leadership", "exec": addsheet(caller, 'Leadership', 'Skills', 1), "goto": "menunode_lpm5c15"})
    return text, options
    
def menunode_lpm5c15(caller):
    text = "Enter your free language."
    options = ({"key": "_default", "goto": "menunode_lpm5c16"})
    return text, options
    

def menunode_lpm5c16(caller, raw_input):
    addsheet(caller, raw_input, 'Languages', 0)
    text = "Select your early career."
    options = ({"key": "0", "desc": "Merchant", "goto": "menunode_lpm6"},
               {"key": "1", "desc": "Money-Lender", "goto": "menunode_lpm6"},
               {"key": "2", "desc": "Pilot", "goto": "menunode_lpm6"},
               {"key": "3", "desc": "Engineer", "goto": "menunode_lpm6"},
               {"key": "4", "desc": "Gunner", "goto": "menunode_lpm6"},
               {"key": "5", "desc": "Soldier", "goto": "menunode_lpm6"},
               {"key": "6", "desc": "Combat Engineer", "goto": "menunode_lpm6"},
               {"key": "7", "desc": "Scholar", "goto": "menunode_lpm6"},
               {"key": "8", "desc": "Scientist", "goto": "menunode_lpm6"},
               {"key": "9", "desc": "Thief", "goto": "menunode_lpm6"},
               {"key": "10", "desc": "Spy", "goto": "menunode_lpm6"})
    return text, options
    

def menunode_lpm5e12(caller):
    text = "You get 2 points in the science group."
    options = ({"key": "0", "desc": "Applied Science", "exec": addsheet(caller, 'Applied Science', 'Skills', 1), "goto": "menunode_lpm5e13"},
               {"key": "1", "desc": "Life Science", "exec": addsheet(caller, 'Life Science', 'Skills', 1), "goto": "menunode_lpm5e13"},
               {"key": "2", "desc": "Social Science", "exec": addsheet(caller, 'Social Science', 'Skills', 1), "goto": "menunode_lpm5e13"},
               {"key": "3", "desc": "Physical Science", "exec": addsheet(caller, 'Physical Science', 'Skills', 1), "goto": "menunode_lpm5e13"},
               {"key": "4", "desc": "Terraforming", "exec": addsheet(caller, 'Terraforming', 'Skills', 1), "goto": "menunode_lpm5e13"})
    return text, options
    

def menunode_lpm5e13(caller):
    text = "You get 2 points in the science group. Second Point."
    options = ({"key": "0", "desc": "Applied Science", "exec": addsheet(caller, 'Applied Science', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "1", "desc": "Life Science", "exec": addsheet(caller, 'Life Science', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "2", "desc": "Social Science", "exec": addsheet(caller, 'Social Science', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "3", "desc": "Physical Science", "exec": addsheet(caller, 'Physical Science', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "4", "desc": "Terraforming", "exec": addsheet(caller, 'Terraforming', 'Skills', 1), "goto": "menunode_lpm5cc"})
    return text, options
    

def menunode_lpm5s12(caller):
    text = "You now get 2 points in the malefaction group."
    options = ({"key": "0", "desc": "Lockpicking", "exec": addsheet(caller, 'Lockpicking', 'Skills', 1), "goto": "menunode_lpm5s13"},
               {"key": "1", "desc": "Sleight of Hand", "exec": addsheet(caller, 'Sleight of Hand', 'Skills', 1), "goto": "menunode_lpm5s13"},
               {"key": "2", "desc": "Sneak", "exec": addsheet(caller, 'Sneak', 'Skills', 1), "goto": "menunode_lpm5s13"},
               {"key": "3", "desc": "Streetwise", "exec": addsheet(caller, 'Streetwise', 'Skills', 1), "goto": "menunode_lpm5s13"},
               {"key": "4", "desc": "Torture", "exec": addsheet(caller, 'Torture', 'Skills', 1), "goto": "menunode_lpm5s13"})
    return text, options
    

def menunode_lpm5s13(caller):
    text = "You now get 2 points in the malefaction group. Second Point."
    options = ({"key": "0", "desc": "Lockpicking", "exec": addsheet(caller, 'Lockpicking', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "1", "desc": "Sleight of Hand", "exec": addsheet(caller, 'Sleight of Hand', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "2", "desc": "Sneak", "exec": addsheet(caller, 'Sneak', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "3", "desc": "Streetwise", "exec": addsheet(caller, 'Streetwise', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "4", "desc": "Torture", "exec": addsheet(caller, 'Torture', 'Skills', 1), "goto": "menunode_lpm5cc"})
    return text, options
    
    
def menunode_lpm5m12(caller):
    text = "Second Combat Point."
    options = ({"key": "0", "desc": "Artifact Melee", "exec": addsheet(caller, 'Artifact Melee', 'Skills', 1), "goto": "menunode_lpm5m13"},
               {"key": "1", "desc": "Archery", "exec": addsheet(caller, 'Archer', 'Skills', 1), "goto": "menunode_lpm5m13"},
               {"key": "2", "desc": "Artillery", "exec": addsheet(caller, 'Artillery', 'Skills', 1), "goto": "menunode_lpm5m13"},
               {"key": "3", "desc": "Demolitions", "exec": addsheet(caller, 'Demolitions', 'Skills', 1), "goto": "menunode_lpm5m13"},
               {"key": "4", "desc": "Energy Guns", "exec": addsheet(caller, 'Energy Guns', 'Skills', 1), "goto": "menunode_lpm5m13"},
               {"key": "5", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 1), "goto": "menunode_lpm5m13"},
               {"key": "6", "desc": "Gunnery", "exec": addsheet(caller, 'Gunnery', 'Skills', 1), "goto": "menunode_lpm5m13"},
               {"key": "7", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 1), "goto": "menunode_lpm5m13"},
               {"key": "8", "desc": "Slug Guns", "exec": addsheet(caller, 'Slug Guns', 'Skills', 1), "goto": "menunode_lpm5m13"},
               {"key": "9", "desc": "Throwing", "exec": addsheet(caller, 'Throwing', 'Skills', 1), "goto": "menunode_lpm5m13"})
    return text, options
    

def menunode_lpm5m13(caller):
    text = "You get 1 point in the control group."
    options = ({"key": "0", "desc": "Aircraft", "exec": addsheet(caller, 'Aircraft', 'Skills', 1), "goto": "menunode_lpm5m14"},
               {"key": "1", "desc": "Beastcraft", "exec": addsheet(caller, 'Beastcraft', 'Skills', 1), "goto": "menunode_lpm5m14"},
               {"key": "2", "desc": "Landcraft", "exec": addsheet(caller, 'Landcraft', 'Skills', 1), "goto": "menunode_lpm5m14"},
               {"key": "3", "desc": "Watercraft", "exec": addsheet(caller, 'Watercraft', 'Skills', 1), "goto": "menunode_lpm5m14"},
               {"key": "4", "desc": "Ride", "exec": addsheet(caller, 'Ride', 'Skills', 1), "goto": "menunode_lpm5m14"})
    return text, options
    

def menunode_lpm5m14(caller):
    text = "You now get 3 points in the malefaction group."
    options = ({"key": "0", "desc": "Lockpicking", "exec": addsheet(caller, 'Lockpicking', 'Skills', 1), "goto": "menunode_lpm5m15"},
               {"key": "1", "desc": "Sleight of Hand", "exec": addsheet(caller, 'Sleight of Hand', 'Skills', 1), "goto": "menunode_lpm5m15"},
               {"key": "2", "desc": "Sneak", "exec": addsheet(caller, 'Sneak', 'Skills', 1), "goto": "menunode_lpm5m15"},
               {"key": "3", "desc": "Streetwise", "exec": addsheet(caller, 'Streetwise', 'Skills', 1), "goto": "menunode_lpm5m15"},
               {"key": "4", "desc": "Torture", "exec": addsheet(caller, 'Torture', 'Skills', 1), "goto": "menunode_lpm5m15"})
    return text, options
    
    
def menunode_lpm5m15(caller):
    text = "You now get 3 points in the malefaction group. Second Point."
    options = ({"key": "0", "desc": "Lockpicking", "exec": addsheet(caller, 'Lockpicking', 'Skills', 1), "goto": "menunode_lpm5m16"},
               {"key": "1", "desc": "Sleight of Hand", "exec": addsheet(caller, 'Sleight of Hand', 'Skills', 1), "goto": "menunode_lpm5m16"},
               {"key": "2", "desc": "Sneak", "exec": addsheet(caller, 'Sneak', 'Skills', 1), "goto": "menunode_lpm5m16"},
               {"key": "3", "desc": "Streetwise", "exec": addsheet(caller, 'Streetwise', 'Skills', 1), "goto": "menunode_lpm5m16"},
               {"key": "4", "desc": "Torture", "exec": addsheet(caller, 'Torture', 'Skills', 1), "goto": "menunode_lpm5m16"})
    return text, options
    

def menunode_lpm5m16(caller):
    text = "You now get 3 points in the malefaction group. Third Point."
    options = ({"key": "0", "desc": "Lockpicking", "exec": addsheet(caller, 'Lockpicking', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "1", "desc": "Sleight of Hand", "exec": addsheet(caller, 'Sleight of Hand', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "2", "desc": "Sneak", "exec": addsheet(caller, 'Sneak', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "3", "desc": "Streetwise", "exec": addsheet(caller, 'Streetwise', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "4", "desc": "Torture", "exec": addsheet(caller, 'Torture', 'Skills', 1), "goto": "menunode_lpm5cc"})
    return text, options
    
    
def menunode_lpm5c22(caller):
    text = "Second Control Point."
    options = ({"key": "0", "desc": "Aircraft", "exec": addsheet(caller, 'Aircraft', 'Skills', 1), "goto": "menunode_lpm5c23"},
               {"key": "1", "desc": "Beastcraft", "exec": addsheet(caller, 'Beastcraft', 'Skills', 1), "goto": "menunode_lpm5c23"},
               {"key": "2", "desc": "Landcraft", "exec": addsheet(caller, 'Landcraft', 'Skills', 1), "goto": "menunode_lpm5c23"},
               {"key": "3", "desc": "Watercraft", "exec": addsheet(caller, 'Watercraft', 'Skills', 1), "goto": "menunode_lpm5c23"},
               {"key": "4", "desc": "Ride", "exec": addsheet(caller, 'Ride', 'Skills', 1), "goto": "menunode_lpm5c23"})
    return text, options
    
    
def menunode_lpm5c23(caller):
    text = "You get one point in the combat group."
    options = ({"key": "0", "desc": "Artifact Melee", "exec": addsheet(caller, 'Artifact Melee', 'Skills', 1), "goto": "menunode_lpm5c24"},
               {"key": "1", "desc": "Archery", "exec": addsheet(caller, 'Archer', 'Skills', 1), "goto": "menunode_lpm5c24"},
               {"key": "2", "desc": "Artillery", "exec": addsheet(caller, 'Artillery', 'Skills', 1), "goto": "menunode_lpm5c24"},
               {"key": "3", "desc": "Demolitions", "exec": addsheet(caller, 'Demolitions', 'Skills', 1), "goto": "menunode_lpm5c24"},
               {"key": "4", "desc": "Energy Guns", "exec": addsheet(caller, 'Energy Guns', 'Skills', 1), "goto": "menunode_lpm5c24"},
               {"key": "5", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 1), "goto": "menunode_lpm5c24"},
               {"key": "6", "desc": "Gunnery", "exec": addsheet(caller, 'Gunnery', 'Skills', 1), "goto": "menunode_lpm5c24"},
               {"key": "7", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 1), "goto": "menunode_lpm5c24"},
               {"key": "8", "desc": "Slug Guns", "exec": addsheet(caller, 'Slug Guns', 'Skills', 1), "goto": "menunode_lpm5c24"},
               {"key": "9", "desc": "Throwing", "exec": addsheet(caller, 'Throwing', 'Skills', 1), "goto": "menunode_lpm5c24"})
    return text, options
    
    
def menunode_lpm5c24(caller):
    text = "You now get 2 points in the malefaction group."
    options = ({"key": "0", "desc": "Lockpicking", "exec": addsheet(caller, 'Lockpicking', 'Skills', 1), "goto": "menunode_lpm5c25"},
               {"key": "1", "desc": "Sleight of Hand", "exec": addsheet(caller, 'Sleight of Hand', 'Skills', 1), "goto": "menunode_lpm5c25"},
               {"key": "2", "desc": "Sneak", "exec": addsheet(caller, 'Sneak', 'Skills', 1), "goto": "menunode_lpm5c25"},
               {"key": "3", "desc": "Streetwise", "exec": addsheet(caller, 'Streetwise', 'Skills', 1), "goto": "menunode_lpm5c25"},
               {"key": "4", "desc": "Torture", "exec": addsheet(caller, 'Torture', 'Skills', 1), "goto": "menunode_lpm5c25"})
    return text, options
    
    
def menunode_lpm5c25(caller):
    text = "You now get 2 points in the malefaction group. Second Point."
    options = ({"key": "0", "desc": "Lockpicking", "exec": addsheet(caller, 'Lockpicking', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "1", "desc": "Sleight of Hand", "exec": addsheet(caller, 'Sleight of Hand', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "2", "desc": "Sneak", "exec": addsheet(caller, 'Sneak', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "3", "desc": "Streetwise", "exec": addsheet(caller, 'Streetwise', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "4", "desc": "Torture", "exec": addsheet(caller, 'Torture', 'Skills', 1), "goto": "menunode_lpm5cc"})
    return text, options
    

def menunode_lpm5e22(caller):
    text = "You get 2 points in the science group. Second Point."
    options = ({"key": "0", "desc": "Applied Science", "exec": addsheet(caller, 'Applied Science', 'Skills', 1), "goto": "menunode_lpm5e23"},
               {"key": "1", "desc": "Life Science", "exec": addsheet(caller, 'Life Science', 'Skills', 1), "goto": "menunode_lpm5e23"},
               {"key": "2", "desc": "Social Science", "exec": addsheet(caller, 'Social Science', 'Skills', 1), "goto": "menunode_lpm5e23"},
               {"key": "3", "desc": "Physical Science", "exec": addsheet(caller, 'Physical Science', 'Skills', 1), "goto": "menunode_lpm5e23"},
               {"key": "4", "desc": "Terraforming", "exec": addsheet(caller, 'Terraforming', 'Skills', 1), "goto": "menunode_lpm5e23"})
    return text, options
    
    
def menunode_lpm5e23(caller):
    text = "You now get 1 point in the malefaction group."
    options = ({"key": "0", "desc": "Lockpicking", "exec": addsheet(caller, 'Lockpicking', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "1", "desc": "Sleight of Hand", "exec": addsheet(caller, 'Sleight of Hand', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "2", "desc": "Sneak", "exec": addsheet(caller, 'Sneak', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "3", "desc": "Streetwise", "exec": addsheet(caller, 'Streetwise', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "4", "desc": "Torture", "exec": addsheet(caller, 'Torture', 'Skills', 1), "goto": "menunode_lpm5cc"})
    return text, options
    
    
def menunode_lpm5s22(caller):
    text = "Second Malefaction Point."
    options = ({"key": "0", "desc": "Lockpicking", "exec": addsheet(caller, 'Lockpicking', 'Skills', 1), "goto": "menunode_lpm5s23"},
               {"key": "1", "desc": "Sleight of Hand", "exec": addsheet(caller, 'Sleight of Hand', 'Skills', 1), "goto": "menunode_lpm5s23"},
               {"key": "2", "desc": "Sneak", "exec": addsheet(caller, 'Sneak', 'Skills', 1), "goto": "menunode_lpm5s23"},
               {"key": "3", "desc": "Streetwise", "exec": addsheet(caller, 'Streetwise', 'Skills', 1), "goto": "menunode_lpm5s23"},
               {"key": "4", "desc": "Torture", "exec": addsheet(caller, 'Torture', 'Skills', 1), "goto": "menunode_lpm5s23"})
    return text, options
    
    
def menunode_lpm5s23(caller):
    text = "Third Malefaction Point."
    options = ({"key": "0", "desc": "Lockpicking", "exec": addsheet(caller, 'Lockpicking', 'Skills', 1), "goto": "menunode_lpm5s24"},
               {"key": "1", "desc": "Sleight of Hand", "exec": addsheet(caller, 'Sleight of Hand', 'Skills', 1), "goto": "menunode_lpm5s24"},
               {"key": "2", "desc": "Sneak", "exec": addsheet(caller, 'Sneak', 'Skills', 1), "goto": "menunode_lpm5s24"},
               {"key": "3", "desc": "Streetwise", "exec": addsheet(caller, 'Streetwise', 'Skills', 1), "goto": "menunode_lpm5s24"},
               {"key": "4", "desc": "Torture", "exec": addsheet(caller, 'Torture', 'Skills', 1), "goto": "menunode_lpm5s24"})
    return text, options
    

def menunode_lpm5s24(caller):
    text = "You get 2 points in the combat group."
    options = ({"key": "0", "desc": "Artifact Melee", "exec": addsheet(caller, 'Artifact Melee', 'Skills', 1), "goto": "menunode_lpm5s25"},
               {"key": "1", "desc": "Archery", "exec": addsheet(caller, 'Archer', 'Skills', 1), "goto": "menunode_lpm5s25"},
               {"key": "2", "desc": "Artillery", "exec": addsheet(caller, 'Artillery', 'Skills', 1), "goto": "menunode_lpm5s25"},
               {"key": "3", "desc": "Demolitions", "exec": addsheet(caller, 'Demolitions', 'Skills', 1), "goto": "menunode_lpm5s25"},
               {"key": "4", "desc": "Energy Guns", "exec": addsheet(caller, 'Energy Guns', 'Skills', 1), "goto": "menunode_lpm5s25"},
               {"key": "5", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 1), "goto": "menunode_lpm5s25"},
               {"key": "6", "desc": "Gunnery", "exec": addsheet(caller, 'Gunnery', 'Skills', 1), "goto": "menunode_lpm5s25"},
               {"key": "7", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 1), "goto": "menunode_lpm5s25"},
               {"key": "8", "desc": "Slug Guns", "exec": addsheet(caller, 'Slug Guns', 'Skills', 1), "goto": "menunode_lpm5s25"},
               {"key": "9", "desc": "Throwing", "exec": addsheet(caller, 'Throwing', 'Skills', 1), "goto": "menunode_lpm5s25"})
    return text, options
    
def menunode_lpm5s25(caller):
    text = "Second Combat Point."
    options = ({"key": "0", "desc": "Artifact Melee", "exec": addsheet(caller, 'Artifact Melee', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "1", "desc": "Archery", "exec": addsheet(caller, 'Archer', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "2", "desc": "Artillery", "exec": addsheet(caller, 'Artillery', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "3", "desc": "Demolitions", "exec": addsheet(caller, 'Demolitions', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "4", "desc": "Energy Guns", "exec": addsheet(caller, 'Energy Guns', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "5", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "6", "desc": "Gunnery", "exec": addsheet(caller, 'Gunnery', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "7", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "8", "desc": "Slug Guns", "exec": addsheet(caller, 'Slug Guns', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "9", "desc": "Throwing", "exec": addsheet(caller, 'Throwing', 'Skills', 1), "goto": "menunode_lpm5cc"})
    return text, options
    
    
def menunode_lpm5m22(caller):
    text = "Second Combat Point."
    options = ({"key": "0", "desc": "Artifact Melee", "exec": addsheet(caller, 'Artifact Melee', 'Skills', 1), "goto": "menunode_lpm5m23"},
               {"key": "1", "desc": "Archery", "exec": addsheet(caller, 'Archer', 'Skills', 1), "goto": "menunode_lpm5m23"},
               {"key": "2", "desc": "Artillery", "exec": addsheet(caller, 'Artillery', 'Skills', 1), "goto": "menunode_lpm5m23"},
               {"key": "3", "desc": "Demolitions", "exec": addsheet(caller, 'Demolitions', 'Skills', 1), "goto": "menunode_lpm5m23"},
               {"key": "4", "desc": "Energy Guns", "exec": addsheet(caller, 'Energy Guns', 'Skills', 1), "goto": "menunode_lpm5m23"},
               {"key": "5", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 1), "goto": "menunode_lpm5m23"},
               {"key": "6", "desc": "Gunnery", "exec": addsheet(caller, 'Gunnery', 'Skills', 1), "goto": "menunode_lpm5m23"},
               {"key": "7", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 1), "goto": "menunode_lpm5m23"},
               {"key": "8", "desc": "Slug Guns", "exec": addsheet(caller, 'Slug Guns', 'Skills', 1), "goto": "menunode_lpm5m23"},
               {"key": "9", "desc": "Throwing", "exec": addsheet(caller, 'Throwing', 'Skills', 1), "goto": "menunode_lpm5m23"})
    return text, options
    

def menunode_lpm5m23(caller):
    text = "You get one point in the control group."
    options = ({"key": "0", "desc": "Aircraft", "exec": addsheet(caller, 'Aircraft', 'Skills', 1), "goto": "menunode_lpm5m24"},
               {"key": "1", "desc": "Beastcraft", "exec": addsheet(caller, 'Beastcraft', 'Skills', 1), "goto": "menunode_lpm5m24"},
               {"key": "2", "desc": "Landcraft", "exec": addsheet(caller, 'Landcraft', 'Skills', 1), "goto": "menunode_lpm5m24"},
               {"key": "3", "desc": "Watercraft", "exec": addsheet(caller, 'Watercraft', 'Skills', 1), "goto": "menunode_lpm5m24"},
               {"key": "4", "desc": "Ride", "exec": addsheet(caller, 'Ride', 'Skills', 1), "goto": "menunode_lpm5m24"})
    return text, options
    
    
def menunode_lpm5m24(caller):
    text = "You get 2 points in the malefaction group."
    options = ({"key": "0", "desc": "Lockpicking", "exec": addsheet(caller, 'Lockpicking', 'Skills', 1), "goto": "menunode_lpm5m25"},
               {"key": "1", "desc": "Sleight of Hand", "exec": addsheet(caller, 'Sleight of Hand', 'Skills', 1), "goto": "menunode_lpm5m25"},
               {"key": "2", "desc": "Sneak", "exec": addsheet(caller, 'Sneak', 'Skills', 1), "goto": "menunode_lpm5m25"},
               {"key": "3", "desc": "Streetwise", "exec": addsheet(caller, 'Streetwise', 'Skills', 1), "goto": "menunode_lpm5m25"},
               {"key": "4", "desc": "Torture", "exec": addsheet(caller, 'Torture', 'Skills', 1), "goto": "menunode_lpm5m25"})
    return text, options
    
    
def menunode_lpm5m25(caller):
    text = "You get 2 points in the malefaction group."
    options = ({"key": "0", "desc": "Lockpicking", "exec": addsheet(caller, 'Lockpicking', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "1", "desc": "Sleight of Hand", "exec": addsheet(caller, 'Sleight of Hand', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "2", "desc": "Sneak", "exec": addsheet(caller, 'Sneak', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "3", "desc": "Streetwise", "exec": addsheet(caller, 'Streetwise', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "4", "desc": "Torture", "exec": addsheet(caller, 'Torture', 'Skills', 1), "goto": "menunode_lpm5cc"})
    return text, options
    
    
def menunode_lpm5r22(caller):
    text = "You get one point in the malefaction group."
    options = ({"key": "0", "desc": "Lockpicking", "exec": addsheet(caller, 'Lockpicking', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "1", "desc": "Sleight of Hand", "exec": addsheet(caller, 'Sleight of Hand', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "2", "desc": "Sneak", "exec": addsheet(caller, 'Sneak', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "3", "desc": "Streetwise", "exec": addsheet(caller, 'Streetwise', 'Skills', 1), "goto": "menunode_lpm5cc"},
               {"key": "4", "desc": "Torture", "exec": addsheet(caller, 'Torture', 'Skills', 1), "goto": "menunode_lpm5cc"})
    return text, options
    
    
def menunode_lpm5cc(caller):
    text = "Select your early career."
    options = ({"key": "0", "desc": "Merchant", "goto": "menunode_lpm6"},
               {"key": "1", "desc": "Money-Lender", "goto": "menunode_lpm6"},
               {"key": "2", "desc": "Pilot", "goto": "menunode_lpm6"},
               {"key": "3", "desc": "Engineer", "goto": "menunode_lpm6"},
               {"key": "4", "desc": "Gunner", "goto": "menunode_lpm6"},
               {"key": "5", "desc": "Soldier", "goto": "menunode_lpm6"},
               {"key": "6", "desc": "Combat Engineer", "goto": "menunode_lpm6"},
               {"key": "7", "desc": "Scholar", "goto": "menunode_lpm6"},
               {"key": "8", "desc": "Scientist", "goto": "menunode_lpm6"},
               {"key": "9", "desc": "Thief", "goto": "menunode_lpm6"},
               {"key": "10", "desc": "Spy", "goto": "menunode_lpm6"})
    return text, options
    
    
def menunode_lpm6(caller, raw_input):
    apply_path_guild(caller, 1, int(raw_input), 'None')
    
    if int(raw_input) == 0:  # Merchant
        text = "You get one point in the combat group."
        options = ({"key": "0", "desc": "Artifact Melee", "exec": addsheet(caller, 'Artifact Melee', 'Skills', 1), "goto": "menunode_lpm6m01"},
                   {"key": "1", "desc": "Archery", "exec": addsheet(caller, 'Archer', 'Skills', 1), "goto": "menunode_lpm6m01"},
                   {"key": "2", "desc": "Artillery", "exec": addsheet(caller, 'Artillery', 'Skills', 1), "goto": "menunode_lpm6m01"},
                   {"key": "3", "desc": "Demolitions", "exec": addsheet(caller, 'Demolitions', 'Skills', 1), "goto": "menunode_lpm6m01"},
                   {"key": "4", "desc": "Energy Guns", "exec": addsheet(caller, 'Energy Guns', 'Skills', 1), "goto": "menunode_lpm6m01"},
                   {"key": "5", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 1), "goto": "menunode_lpm6m01"},
                   {"key": "6", "desc": "Gunnery", "exec": addsheet(caller, 'Gunnery', 'Skills', 1), "goto": "menunode_lpm6m01"},
                   {"key": "7", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 1), "goto": "menunode_lpm6m01"},
                   {"key": "8", "desc": "Slug Guns", "exec": addsheet(caller, 'Slug Guns', 'Skills', 1), "goto": "menunode_lpm6m01"},
                   {"key": "9", "desc": "Throwing", "exec": addsheet(caller, 'Throwing', 'Skills', 1), "goto": "menunode_lpm6m01"})
        return text, options
    elif int(raw_input) == 1:  # Money Lender
        text = "You get one point in the combat group."
        options = ({"key": "0", "desc": "Artifact Melee", "exec": addsheet(caller, 'Artifact Melee', 'Skills', 1), "goto": "menunode_lpm6ml01"},
                   {"key": "1", "desc": "Archery", "exec": addsheet(caller, 'Archer', 'Skills', 1), "goto": "menunode_lpm6ml01"},
                   {"key": "2", "desc": "Artillery", "exec": addsheet(caller, 'Artillery', 'Skills', 1), "goto": "menunode_lpm6ml01"},
                   {"key": "3", "desc": "Demolitions", "exec": addsheet(caller, 'Demolitions', 'Skills', 1), "goto": "menunode_lpm6ml01"},
                   {"key": "4", "desc": "Energy Guns", "exec": addsheet(caller, 'Energy Guns', 'Skills', 1), "goto": "menunode_lpm6ml01"},
                   {"key": "5", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 1), "goto": "menunode_lpm6ml01"},
                   {"key": "6", "desc": "Gunnery", "exec": addsheet(caller, 'Gunnery', 'Skills', 1), "goto": "menunode_lpm6ml01"},
                   {"key": "7", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 1), "goto": "menunode_lpm6ml01"},
                   {"key": "8", "desc": "Slug Guns", "exec": addsheet(caller, 'Slug Guns', 'Skills', 1), "goto": "menunode_lpm6ml01"},
                   {"key": "9", "desc": "Throwing", "exec": addsheet(caller, 'Throwing', 'Skills', 1), "goto": "menunode_lpm6ml01"})
        return text, options
    elif int(raw_input) == 2:  # Pilot 
        text = "You get 2 points in the combat group."
        options = ({"key": "0", "desc": "Artifact Melee", "exec": addsheet(caller, 'Artifact Melee', 'Skills', 1), "goto": "menunode_lpm6p01"},
                   {"key": "1", "desc": "Archery", "exec": addsheet(caller, 'Archer', 'Skills', 1), "goto": "menunode_lpm6p01"},
                   {"key": "2", "desc": "Artillery", "exec": addsheet(caller, 'Artillery', 'Skills', 1), "goto": "menunode_lpm6p01"},
                   {"key": "3", "desc": "Demolitions", "exec": addsheet(caller, 'Demolitions', 'Skills', 1), "goto": "menunode_lpm6p01"},
                   {"key": "4", "desc": "Energy Guns", "exec": addsheet(caller, 'Energy Guns', 'Skills', 1), "goto": "menunode_lpm6p01"},
                   {"key": "5", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 1), "goto": "menunode_lpm6p01"},
                   {"key": "6", "desc": "Gunnery", "exec": addsheet(caller, 'Gunnery', 'Skills', 1), "goto": "menunode_lpm6p01"},
                   {"key": "7", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 1), "goto": "menunode_lpm6p01"},
                   {"key": "8", "desc": "Slug Guns", "exec": addsheet(caller, 'Slug Guns', 'Skills', 1), "goto": "menunode_lpm6p01"},
                   {"key": "9", "desc": "Throwing", "exec": addsheet(caller, 'Throwing', 'Skills', 1), "goto": "menunode_lpm6p01"})
        return text, options
    elif int(raw_input) == 3:  # Engineer
        text = "You get 2 points in the combat group."
        options = ({"key": "0", "desc": "Artifact Melee", "exec": addsheet(caller, 'Artifact Melee', 'Skills', 1), "goto": "menunode_lpm6e01"},
                   {"key": "1", "desc": "Archery", "exec": addsheet(caller, 'Archer', 'Skills', 1), "goto": "menunode_lpm6e01"},
                   {"key": "2", "desc": "Artillery", "exec": addsheet(caller, 'Artillery', 'Skills', 1), "goto": "menunode_lpm6e01"},
                   {"key": "3", "desc": "Demolitions", "exec": addsheet(caller, 'Demolitions', 'Skills', 1), "goto": "menunode_lpm6e01"},
                   {"key": "4", "desc": "Energy Guns", "exec": addsheet(caller, 'Energy Guns', 'Skills', 1), "goto": "menunode_lpm6e01"},
                   {"key": "5", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 1), "goto": "menunode_lpm6e01"},
                   {"key": "6", "desc": "Gunnery", "exec": addsheet(caller, 'Gunnery', 'Skills', 1), "goto": "menunode_lpm6e01"},
                   {"key": "7", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 1), "goto": "menunode_lpm6e01"},
                   {"key": "8", "desc": "Slug Guns", "exec": addsheet(caller, 'Slug Guns', 'Skills', 1), "goto": "menunode_lpm6e01"},
                   {"key": "9", "desc": "Throwing", "exec": addsheet(caller, 'Throwing', 'Skills', 1), "goto": "menunode_lpm6e01"})
        return text, options
    elif int(raw_input) == 4:  # Gunner
        text = "You get 2 points in the combat group."
        options = ({"key": "0", "desc": "Artifact Melee", "exec": addsheet(caller, 'Artifact Melee', 'Skills', 1), "goto": "menunode_lpm6g01"},
                   {"key": "1", "desc": "Archery", "exec": addsheet(caller, 'Archer', 'Skills', 1), "goto": "menunode_lpm6g01"},
                   {"key": "2", "desc": "Artillery", "exec": addsheet(caller, 'Artillery', 'Skills', 1), "goto": "menunode_lpm6g01"},
                   {"key": "3", "desc": "Demolitions", "exec": addsheet(caller, 'Demolitions', 'Skills', 1), "goto": "menunode_lpm6g01"},
                   {"key": "4", "desc": "Energy Guns", "exec": addsheet(caller, 'Energy Guns', 'Skills', 1), "goto": "menunode_lpm6g01"},
                   {"key": "5", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 1), "goto": "menunode_lpm6g01"},
                   {"key": "6", "desc": "Gunnery", "exec": addsheet(caller, 'Gunnery', 'Skills', 1), "goto": "menunode_lpm6g01"},
                   {"key": "7", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 1), "goto": "menunode_lpm6g01"},
                   {"key": "8", "desc": "Slug Guns", "exec": addsheet(caller, 'Slug Guns', 'Skills', 1), "goto": "menunode_lpm6g01"},
                   {"key": "9", "desc": "Throwing", "exec": addsheet(caller, 'Throwing', 'Skills', 1), "goto": "menunode_lpm6g01"})
        return text, options
    elif int(raw_input) == 5:  # Soldier
        text = "You get 7 points in the combat group."
        options = ({"key": "0", "desc": "Artifact Melee", "exec": addsheet(caller, 'Artifact Melee', 'Skills', 1), "goto": "menunode_lpm6s01"},
                   {"key": "1", "desc": "Archery", "exec": addsheet(caller, 'Archer', 'Skills', 1), "goto": "menunode_lpm6s01"},
                   {"key": "2", "desc": "Artillery", "exec": addsheet(caller, 'Artillery', 'Skills', 1), "goto": "menunode_lpm6s01"},
                   {"key": "3", "desc": "Demolitions", "exec": addsheet(caller, 'Demolitions', 'Skills', 1), "goto": "menunode_lpm6s01"},
                   {"key": "4", "desc": "Energy Guns", "exec": addsheet(caller, 'Energy Guns', 'Skills', 1), "goto": "menunode_lpm6s01"},
                   {"key": "5", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 1), "goto": "menunode_lpm6s01"},
                   {"key": "6", "desc": "Gunnery", "exec": addsheet(caller, 'Gunnery', 'Skills', 1), "goto": "menunode_lpm6s01"},
                   {"key": "7", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 1), "goto": "menunode_lpm6s01"},
                   {"key": "8", "desc": "Slug Guns", "exec": addsheet(caller, 'Slug Guns', 'Skills', 1), "goto": "menunode_lpm6s01"},
                   {"key": "9", "desc": "Throwing", "exec": addsheet(caller, 'Throwing', 'Skills', 1), "goto": "menunode_lpm6s01"})
        return text, options
    elif int(raw_input) == 6:  # Combat Engineer
        text = "You get 3 points in the combat group."
        options = ({"key": "0", "desc": "Artifact Melee", "exec": addsheet(caller, 'Artifact Melee', 'Skills', 1), "goto": "menunode_lpm6ce01"},
                   {"key": "1", "desc": "Archery", "exec": addsheet(caller, 'Archer', 'Skills', 1), "goto": "menunode_lpm6ce01"},
                   {"key": "2", "desc": "Artillery", "exec": addsheet(caller, 'Artillery', 'Skills', 1), "goto": "menunode_lpm6ce01"},
                   {"key": "3", "desc": "Demolitions", "exec": addsheet(caller, 'Demolitions', 'Skills', 1), "goto": "menunode_lpm6ce01"},
                   {"key": "4", "desc": "Energy Guns", "exec": addsheet(caller, 'Energy Guns', 'Skills', 1), "goto": "menunode_lpm6ce01"},
                   {"key": "5", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 1), "goto": "menunode_lpm6ce01"},
                   {"key": "6", "desc": "Gunnery", "exec": addsheet(caller, 'Gunnery', 'Skills', 1), "goto": "menunode_lpm6ce01"},
                   {"key": "7", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 1), "goto": "menunode_lpm6ce01"},
                   {"key": "8", "desc": "Slug Guns", "exec": addsheet(caller, 'Slug Guns', 'Skills', 1), "goto": "menunode_lpm6ce01"},
                   {"key": "9", "desc": "Throwing", "exec": addsheet(caller, 'Throwing', 'Skills', 1), "goto": "menunode_lpm6ce01"})
        return text, options
    elif int(raw_input) == 7 or int(raw_input) == 8:  # Scholar and Scientist. They both pick 5 points of science, nothing more.
        text = "You get 5 points in the science group."
        options = ({"key": "0", "desc": "Applied Science", "exec": addsheet(caller, 'Applied Science', 'Skills', 1), "goto": "menunode_lpm6schi01"},
                   {"key": "1", "desc": "Life Science", "exec": addsheet(caller, 'Life Science', 'Skills', 1), "goto": "menunode_lpm6schi01"},
                   {"key": "2", "desc": "Social Science", "exec": addsheet(caller, 'Social Science', 'Skills', 1), "goto": "menunode_lpm6schi01"},
                   {"key": "3", "desc": "Physical Science", "exec": addsheet(caller, 'Physical Science', 'Skills', 1), "goto": "menunode_lpm6schi01"},
                   {"key": "4", "desc": "Terraforming", "exec": addsheet(caller, 'Terraforming', 'Skills', 1), "goto": "menunode_lpm6schi01"})
        return text, options
    elif int(raw_input) == 9:  # Thief
        text = "You get 2 points in the combat group."
        options = ({"key": "0", "desc": "Artifact Melee", "exec": addsheet(caller, 'Artifact Melee', 'Skills', 1), "goto": "menunode_lpm6t01"},
                   {"key": "1", "desc": "Archery", "exec": addsheet(caller, 'Archer', 'Skills', 1), "goto": "menunode_lpm6t01"},
                   {"key": "2", "desc": "Artillery", "exec": addsheet(caller, 'Artillery', 'Skills', 1), "goto": "menunode_lpm6t01"},
                   {"key": "3", "desc": "Demolitions", "exec": addsheet(caller, 'Demolitions', 'Skills', 1), "goto": "menunode_lpm6t01"},
                   {"key": "4", "desc": "Energy Guns", "exec": addsheet(caller, 'Energy Guns', 'Skills', 1), "goto": "menunode_lpm6t01"},
                   {"key": "5", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 1), "goto": "menunode_lpm6t01"},
                   {"key": "6", "desc": "Gunnery", "exec": addsheet(caller, 'Gunnery', 'Skills', 1), "goto": "menunode_lpm6t01"},
                   {"key": "7", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 1), "goto": "menunode_lpm6t01"},
                   {"key": "8", "desc": "Slug Guns", "exec": addsheet(caller, 'Slug Guns', 'Skills', 1), "goto": "menunode_lpm6t01"},
                   {"key": "9", "desc": "Throwing", "exec": addsheet(caller, 'Throwing', 'Skills', 1), "goto": "menunode_lpm6t01"})
        return text, options
    elif int(raw_input) == 10: # Spy
        text = "You get 2 points in the combat group."
        options = ({"key": "0", "desc": "Artifact Melee", "exec": addsheet(caller, 'Artifact Melee', 'Skills', 1), "goto": "menunode_lpm6spy01"},
                   {"key": "1", "desc": "Archery", "exec": addsheet(caller, 'Archer', 'Skills', 1), "goto": "menunode_lpm6spy01"},
                   {"key": "2", "desc": "Artillery", "exec": addsheet(caller, 'Artillery', 'Skills', 1), "goto": "menunode_lpm6spy01"},
                   {"key": "3", "desc": "Demolitions", "exec": addsheet(caller, 'Demolitions', 'Skills', 1), "goto": "menunode_lpm6spy01"},
                   {"key": "4", "desc": "Energy Guns", "exec": addsheet(caller, 'Energy Guns', 'Skills', 1), "goto": "menunode_lpm6spy01"},
                   {"key": "5", "desc": "Fight", "exec": addsheet(caller, 'Fight', 'Skills', 1), "goto": "menunode_lpm6spy01"},
                   {"key": "6", "desc": "Gunnery", "exec": addsheet(caller, 'Gunnery', 'Skills', 1), "goto": "menunode_lpm6spy01"},
                   {"key": "7", "desc": "Melee", "exec": addsheet(caller, 'Melee', 'Skills', 1), "goto": "menunode_lpm6spy01"},
                   {"key": "8", "desc": "Slug Guns", "exec": addsheet(caller, 'Slug Guns', 'Skills', 1), "goto": "menunode_lpm6spy01"},
                   {"key": "9", "desc": "Throwing", "exec": addsheet(caller, 'Throwing', 'Skills', 1), "goto": "menunode_lpm6spy01"})
        return text, options