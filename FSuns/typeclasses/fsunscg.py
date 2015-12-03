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
            addsheet(caller, 'Inquiry', 'Skills', 1)
            addsheet(caller, 'Streetwise', 'Skills', 1)

        # Town
        elif what == 1:
            addsheet(caller, 'Wits', 'Attributes', 1)
            addsheet(caller, 'Perception', 'Attributes', 1)
            addsheet(caller, 'Extrovert', 'Attributes', 2)
            addsheet(caller, 'Charm', 'Skills', 1)
            addsheet(caller, 'Vigor', 'Skills', 1)
            addsheet(caller, 'Inquiry', 'Skills', 1)

        # Country
        elif what == 2:
            addsheet(caller, 'Strength', 'Attributes', 1)
            addsheet(caller, 'Endurance', 'Attributes', 2)
            addsheet(caller, 'Faith', 'Attributes', 1)
            addsheet(caller, 'Vigor', 'Skills', 1)
            addsheet(caller, 'Lore Regional', 'Skills', 1)

    # Class
    elif which == 1:
        # Wealthy
        if what == 0:
            addsheet(caller, 'Extrovert', 'Attributes', 1)
            addsheet(caller, 'Read Urthish', 'Languages', 0)

        # Average would be here, but it's all choices

        # poor
        elif what == 2:
            addsheet(caller, 'Knavery', 'Skills', 1)
            

def apply_path_priest(caller, which, what):
    # Apprenticeship
    if which == 0:
        
        # Cathedral
        if what == 0:
            
            # Urth Orthodox
            if caller.db.house == "Urth Orthodox":
                addsheet(caller, 'Wits', 'Attributes', 1)
                addsheet(caller, 'Extrovert', 'Attributes', 1)
                addsheet(caller, 'Calm', 'Attributes', 1)
                addsheet(caller, 'Faith', 'Attributes', 2)
                addsheet(caller, 'Academia', 'Skills', 1)
                addsheet(caller, 'Focus', 'Skills', 1)
                addsheet(caller, 'Lore Theology', 'Skills', 1)
                addsheet(caller, 'Physick', 'Skills', 1)
                addsheet(caller, 'Social Oratory', 'Skills', 1)
                addsheet(caller, 'Read Latin', 'Languages', 0)
                addsheet(caller, 'Remedy', 'Skills', 1)
                addsheet(caller, 'Pious', 'Blessings', 0)
                addsheet(caller, 'Austere', 'Curses', 0)
                
            # Eskatonic
            elif caller.db.house == "Eskatonic Order":
                addsheet(caller, 'Wits', 'Attributes', 1)
                addsheet(caller, 'Introvert', 'Attributes', 2)
                addsheet(caller, 'Faith', 'Attributes', 2)
                addsheet(caller, 'Observe', 'Skills', 1)
                addsheet(caller, 'Academia', 'Skills', 1)
                addsheet(caller, 'Alchemy', 'Skills', 1)
                addsheet(caller, 'Focus', 'Skills', 3)
                addsheet(caller, 'Lore Occult', 'Skills', 1)
                addsheet(caller, 'Stoic Mind', 'Skills', 1)
                addsheet(caller, 'Read Latin', 'Languages', 0)
                addsheet(caller, 'Curious', 'Blessings', 0)
                addsheet(caller, 'Subtle', 'Curses', 0)
                
            # Temple Avesti
            elif caller.db.house == "Temple Avesti":
                
                
            # Sanctuary Aeon
            elif caller.db.house == "Sanctuary Aeon":
            
        # Parish
        elif what == 1:
            
            # Urth Orthodox
            if caller.db.house == "Urth Orthodox":
                
            # Eskatonic
            elif caller.db.house == "Eskatonic Order":
                
            # Temple Avesti
            elif caller.db.house == "Temple Avesti":
                
            # Sanctuary Aeon
            elif caller.db.house == "Sanctuary Aeon":
            
        # Monastery
        elif what == 2:
            
            # Urth Orthodox
            if caller.db.house == "Urth Orthodox":
                
            # Eskatonic
            elif caller.db.house == "Eskatonic Order":
                
            # Temple Avesti
            elif caller.db.house == "Temple Avesti":
                
            # Sanctuary Aeon
            elif caller.db.house == "Sanctuary Aeon":
            
    # Early Career
    elif which == 1:
        
        # Preacher Pastor
        if what == 0:
            
            # Urth Orthodox
            if caller.db.house == "Urth Orthodox":
                
            # Eskatonic
            elif caller.db.house == "Eskatonic Order":
                
            # Temple Avesti
            elif caller.db.house == "Temple Avesti":
                
            # Sanctuary Aeon
            elif caller.db.house == "Sanctuary Aeon":
            
        # Monk
        elif what == 1:
            
            # Urth Orthodox
            if caller.db.house == "Urth Orthodox":
                
            # Eskatonic
            elif caller.db.house == "Eskatonic Order":
                
            # Temple Avesti
            elif caller.db.house == "Temple Avesti":
                
            # Sanctuary Aeon
            elif caller.db.house == "Sanctuary Aeon":
            
        # Missionary
        elif what == 2:
            
            # Urth Orthodox
            if caller.db.house == "Urth Orthodox":
                
            # Eskatonic
            elif caller.db.house == "Eskatonic Order":
                
            # Temple Avesti
            elif caller.db.house == "Temple Avesti":
                
            # Sanctuary Aeon
            elif caller.db.house == "Sanctuary Aeon":
            
        # Healer
        elif what == 3:
            
            # Urth Orthodox
            if caller.db.house == "Urth Orthodox":
                
            # Eskatonic
            elif caller.db.house == "Eskatonic Order":
                
            # Temple Avesti
            elif caller.db.house == "Temple Avesti":
                
            # Sanctuary Aeon
            elif caller.db.house == "Sanctuary Aeon":
            
        # Inquisitor
        elif what == 4:
            
            # Urth Orthodox
            if caller.db.house == "Urth Orthodox":
                
            # Eskatonic
            elif caller.db.house == "Eskatonic Order":
                
            # Temple Avesti
            elif caller.db.house == "Temple Avesti":
                
            # Sanctuary Aeon
            elif caller.db.house == "Sanctuary Aeon":


def menunode_start(caller):
    text = "Beginning Fading Suns Character Generation. You will be able to execute other commands.\n"
    text += "You can exit early but will have to start over. Select your character's path."
    options = ({"desc": "Lifepath CG", "goto": "menunode_lifepath"}, {"desc": "Custom CG", "goto": "menunode_custom"})
    return text, options


def menunode_lifepath(caller):
    text = "Lifepath CG Beginning. This CG module uses the Lifepaths as described in FAS21901 the 2014 supplement to revised. It is free online.\n"
    text += "Please begin by selecting an archetype."
    options = ({"desc": "Nobles", "goto": "menunode_lpn1"}, {"desc": "Priests", "goto": "menunode_lpp1"},
               {"desc": "Merchants", "goto": "menunode_lpm1"}, {"desc": "Aliens", "goto": "menunode_lpa1"})
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
    if raw_input == 16:
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
    elif 15 >= raw_input >= 5 :
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

    if raw_input == 3:
        caller.db.recbenefices.append('Church Ally')
    elif raw_input == 4:
        caller.db.recbenefices.append('Passage Contract')

    caller.db.house = househelper[raw_input]
    addsheet(pc, 'Faction Lore: ' + househelper[raw_input], 'Skills', 3)

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
               {"key": "1", "desc": "Decados", "goto": "menunode_lpnq"},
               {"key": "2", "desc": "Hazat", "goto": "menunode_lpnq"},
               {"key": "3", "desc": "Li Halan", "goto": "menunode_lpnq"},
               {"key": "4", "desc": "al-Malik", "goto": "menunode_lpnq"})
        return text, options

    caller.db.mirrorhouse = househelper[raw_input]

    if raw_input == 3:
        caller.db.recbenefices.append('Church Ally')
    elif raw_input == 4:
        caller.db.recbenefices.append('Passage Contract')

    text = "At this point you select your upbringing. Depending on your house you will gain various bonuses."
    options = ({"key": "0", "desc": "High Court", "goto": "menunode_lpn3"},
               {"key": "1", "desc": "Rural Estate", "goto": "menunode_lpn3"},
               {"key": "2", "desc": "Landless", "goto": "menunode_lpn3"})
    return text, options


def menunode_lpnq(caller, raw_input):
    if caller.db.minor == 1:
        caller.db.mirrorhouse = househelper[raw_input]
    elif raw_input <= 4:
        caller.db.house = househelper[raw_input]
        addsheet(pc, 'Faction Lore: ' + househelper[raw_input], 'Skills', 3)
    elif 15 >= raw_input >= 5:
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
    

    if raw_input == 3:
        caller.db.recbenefices.append('Church Ally')
    elif raw_input == 4:
        caller.db.recbenefices.append('Passage Contract')

    text = "At this point you select your upbringing. Depending on your house you will gain various bonuses."
    options = ({"key": "0", "desc": "High Court", "goto": "menunode_lpnq4"},
               {"key": "1", "desc": "Rural Estate", "goto": "menunode_lpnq4"},
               {"key": "2", "desc": "Landless", "goto": "menunode_lpnq4"})
    return text, options
    
    
def menunode_lpnqmh(caller, raw_input):
    caller.db.mirrorhouse = househelper[raw_input]
    
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

    if caller.db.minor:
        apply_path_noble(0, raw_input, caller.db.mirrorhouse, caller)
    else:
        apply_path_noble(0, raw_input, caller.db.house, caller)

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
        apply_path_noble(0, raw_input, caller.db.mirrorhouse, caller)
    else:
        apply_path_noble(0, raw_input, caller.db.house, caller)

    text = "Please select your noble apprenticeship."
    options = ({"key": "0", "desc": "Soldier", "goto": "menunode_lpnq5"},
               {"key": "1", "desc": "Starman", "goto": "menunode_lpnq5"},
               {"key": "2", "desc": "Diplomacy and Intrigue", "goto": "menunode_lpnq5"},
               {"key": "3", "desc": "Duelist", "goto": "menunode_lpnq5"},
               {"key": "4", "desc": "Dandy", "goto": "menunode_lpnq5"},
               {"key": "5", "desc": "Study", "goto": "menunode_lpnq5"})
    return text, options

#TODO: Fix choices to match up with newer lifepaths.
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


def menunode_lpnq57(caller):
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

    if raw_input == 0:
        text = "Do you want Passion or Calm +1?"
        options = ({"key": "0", "desc": "Passion", "exec": addsheet(caller, 'Passion', 'Attributes', 1), "goto": TOUR OF DUTY},
                   {"key": "1", "desc": "Calm", "exec": addsheet(caller, 'Calm', 'Attributes', 1), "goto": TOUR OF DUTY})
        return text, options
    elif raw_input == 1:
        text = "Do you want Passion or Calm +2?"
        options = ({"key": "0", "desc": "Passion", "exec": addsheet(caller, 'Passion', 'Attributes', 2), "goto": TOUR OF DUTY},
                   {"key": "1", "desc": "Calm", "exec": addsheet(caller, 'Calm', 'Attributes', 2), "goto": TOUR OF DUTY})
        return text, options
    elif raw_input == 2:
        text = "Do you want Extrovert or Introvert +1?"
        options = ({"key": "0", "desc": "Extrovert", "exec": addsheet(caller, 'Extrovert', 'Attributes', 1), "goto": "menunode_lpn6d2"},
                   {"key": "1", "desc": "Introvert", "exec": addsheet(caller, 'Introvert', 'Attributes', 1), "goto": "menunode_lpn6d2"})
        return text, options
    elif raw_input == 3:
        text = "Do you want Faith or Ego +1?"
        options = ({"key": "0", "desc": "Faith", "exec": addsheet(caller, 'Faith', 'Attributes', 1), "goto": "menunode_lpn6a2"},
                   {"key": "1", "desc": "Ego", "exec": addsheet(caller, 'Ego', 'Attributes', 1), "goto": "menunode_lpn6a2"})
        return text, options


def menunode_lpn6d2(caller):
    text = "Do you want to Passion or Calm +2?"
    options = ({"key": "0", "desc": "Passion", "exec": addsheet(caller, 'Passion', 'Attributes', 2), "goto": "menunode_lpn6d3"},
               {"key": "1", "desc": "Calm", "exec": addsheet(caller, 'Calm', 'Attributes', 2), "goto": "menunode_lpn6d3"})
    return text, options


def menunode_lpn6d3(caller):
    if 'Fencing' in caller.db.actions:
        text = "For your dueling actions do you want Parry and Riposte or Disarm?"
        options = ({"key": "0", "desc": "Parry and Riposte", "goto": "menunode_lpn6d4"},
                   {"key": "1", "desc": "Disarm", "goto": "menunode_lpn6d4"})
        return text, options
    else:
        caller.db.actions['Fencing'] = ['Parry', 'Thrust', 'Slash', 'Draw & Strike']
        # TOUR OF DUTY


def menunode_lpn6d4(caller, raw_input):
    if raw_input == 0:
        caller.db.actions['Fencing'].append('Draw & Strike')
        caller.db.actions['Fencing'].append('Parry')
        caller.db.actions['Fencing'].append('Riposte')
        caller.db.actions['Fencing'].append('Feint')
    else:
        caller.db.actions['Fencing'].append('Draw & Strike')
        caller.db.actions['Fencing'].append('Disarm')
        caller.db.actions['Fencing'].append('Feint')

    # Tour of Duty

    # End Noble Section

    # Begin Priest Section
def menunode_lpp1(caller):
    caller.db.recbenefices.append('Ordained')
    caller.db.recbenefices.append('Vestments')
    caller.db.archetype = 'Priest'

    def ipcs(caller):
        caller.db.questing = 1
        caller.db.recbenefices.append('Cohort Badge')
        caller.db.recbenefices.append('Well-Travelled')

    text = "If you intend to do Mendicants with a custom Order, please use custom cg. What order does your priest come from?"
    options = ({"key": "0", "desc": "Urth Orthodox", "goto": "menunode_lpp2"},
               {"key": "1", "desc": "Brother Battle", "goto": "menunode_lppbb"},
               {"key": "2", "desc": "Eskatonic Order", "goto": "menunode_lpp2"},
               {"key": "3", "desc": "Temple Avesti", "goto": "menunode_lpp2"},
               {"key": "4", "desc": "Sanctuary Aeon", "goto": "menunode_lpp2"},
               {"key": "5", "desc": "Mendicant Monks", "goto": "menunode_lppmm"},
               {"key": "6", "desc": "Imperial Priest Cohort", "exec": ipcs, "goto": "menunode_lppmm"})
    return text, options


def menunode_lppmm(caller):
    text = "Which order are you mirroring for bonuses?\n"
    text += "If you picked Imperial Priest Cohort, This question is instead for picking the order you come from."
    options = ({"key": "0", "desc": "Urth Orthodox", "goto": "menunode_lppmm2"},
               {"key": "1", "desc": "Brother Battle", "goto": "menunode_lppbb"},
               {"key": "2", "desc": "Eskatonic Order", "goto": "menunode_lppmm2"},
               {"key": "3", "desc": "Temple Avesti", "goto": "menunode_lppmm2"},
               {"key": "4", "desc": "Sanctuary Aeon", "goto": "menunode_lppmm2"})
    return text, options


def menunode_lppmm2(caller, raw_input):
    caller.db.house = priesthelper[raw_input]
    addsheet(caller, 'Faction Lore: ' + priesthelper[raw_input], 'Skills', 3)

    if raw_input == 0:
        caller.db.recbenefices.append('Noble Ally')
    elif raw_input == 2:
        caller.db.recbenefices.append('Secrets')
        caller.db.recbenefices.append('Refuge')
    elif raw_input == 4:
        caller.db.recbenefices.append('Ally')

    text = "Now choose your upbringing. Upbringing for a priest has 2 factors. First pick your Environment."
    options = ({"key": "0", "desc": "City", "exec": apply_path_uppm(caller, 0, 0), "goto": "menunode_lpp3"},
               {"key": "1", "desc": "Town", "exec": apply_path_uppm(caller, 0, 1), "goto": "menunode_lpp3"},
               {"key": "2", "desc": "Country", "exec": apply_path_uppm(caller, 0, 2), "goto": "menunode_lpp22"})
    return text, options


def menunode_lpp2(caller, raw_input):
    caller.db.house = priesthelper[raw_input]
    addsheet(caller, 'Faction Lore: ' + priesthelper[raw_input], 'Skills', 3)

    if raw_input == 0:
        caller.db.recbenefices.append('Noble Ally')
    elif raw_input == 2:
        caller.db.recbenefices.append('Secrets')
        caller.db.recbenefices.append('Refuge')
    elif raw_input == 4:
        caller.db.recbenefices.append('Ally')

    text = "Now choose your upbringing. Upbringing for a priest has 2 factors. First pick your Environment."
    options = ({"key": "0", "desc": "City", "exec": apply_path_uppm(caller, 0, 0), "goto": "menunode_lpp3"},
               {"key": "1", "desc": "Town", "exec": apply_path_uppm(caller, 0, 1), "goto": "menunode_lpp3"},
               {"key": "2", "desc": "Country", "exec": apply_path_uppm(caller, 0, 2), "goto": "menunode_lpp22"})
    return text, options


def menunode_lpp22(caller):
    text = "Do you want Beast Lore or Drive Beastcraft at +1?"
    options = ({"key": "0", "desc": "Beast Lore", "exec": addsheet(caller, 'Beast Lore', 'Skills', 1), "goto": "menunode_lpp3"},
               {"key": "1", "desc": "Drive Beastcraft", "exec": addsheet(caller, 'Drive Beastcraft', 'Skills', 1), "goto": "menunode_lpp3"})
    return text, options


def menunode_lpp3(caller):
    text = "Now choose your Class."
    options = ({"key": "0", "desc": "Wealthy", "exec": apply_path_uppm(caller, 1, 0), "goto": "menunode_lpp4"},
               {"key": "1", "desc": "Average", "exec": apply_path_uppm(caller, 1, 1), "goto": "menunode_lpp3a"},
               {"key": "2", "desc": "Poor", "exec": apply_path_uppm(caller, 1, 2), "goto": "menunode_lpp3p"})
    return text, options


def menunode_lpp3a(caller):
    text = "Do you want Extrovert or Introvert +1?"
    options = ({"key": "0", "desc": "Extrovert", "exec": addsheet(caller, 'Extrovert', 'Attributes', 1), "goto": "menunode_lpp3a2"},
               {"key": "1", "desc": "Introvert", "exec": addsheet(caller, 'Introvert', 'Attributes', 1), "goto": "menunode_lpp3a2"})
    return text, options


def menunode_lpp3a2(caller):
    text = "Do you want Charm or Impress +1?"
    options = ({"key": "0", "desc": "Charm", "exec": addsheet(caller, 'Charm', 'Skills', 1), "goto": "menunode_lpp3a3"},
               {"key": "1", "desc": "Impress", "exec": addsheet(caller, 'Impress', 'Skills', 1), "goto": "menunode_lpp3a3"})
    return text, options


def menunode_lpp3a3(caller):
    text = "Do you want Lore Folk or Lore Regional +1?"
    options = ({"key": "0", "desc": "Lore Folk", "exec": addsheet(caller, 'Lore Folk', 'Skills', 1), "goto": "menunode_lpp4"},
               {"key": "1", "desc": "Lore Regional", "exec": addsheet(caller, 'Lore Regional', 'Skills', 1), "goto": "menunode_lpp4"})
    return text, options


def menunode_lpp3p(caller):
    text = "Do you want Faith or Ego +1?"
    options = ({"key": "0", "desc": "Faith", "exec": addsheet(caller, 'Ego', 'Attributes', 1), "goto": "menunode_lpp3p2"},
               {"key": "1", "desc": "Ego", "exec": addsheet(caller, 'Faith', 'Attributes', 1), "goto": "menunode_lpp3p2"})
    return text, options


def menunode_lpp3p2(caller):
    text = "Do you want Streetwise or Survival +1?"
    options = ({"key": "0", "desc": "Streetwise", "exec": addsheet(caller, 'Streetwise', 'Skills', 1), "goto": "menunode_lpp4"},
               {"key": "1", "desc": "Survival", "exec": addsheet(caller, 'Survival', 'Skills', 1), "goto": "menunode_lpp4"})
    return text, options


def menunode_lpp4(caller):
    text = "Now it's time to choose if you spent your time in a Cathedral, Parish or Monastery."
    options = ({"key": "0", "desc": "Cathedral", "exec": apply_path_priest(caller, 0, 0, caller.db.house), "goto": "menunode_lpp5"},
               {"key": "1", "desc": "Parish", "exec": apply_path_priest(caller, 0, 1, caller.db.house), "goto": "menunode_lpp5"},
               {"key": "1", "desc": "Monastery", "exec": apply_path_priest(caller, 0, 2, caller.db.house), "goto": "menunode_lpp5"})
    return text, options


def menunode_lpp5(caller):
    pass