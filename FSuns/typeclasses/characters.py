"""
Characters

Characters are (by default) Objects setup to be puppeted by Players.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
from evennia import DefaultCharacter

class Character(DefaultCharacter):
    """
    The Character defaults to implementing some of its hook methods with the
    following standard functionality:

    at_basetype_setup - always assigns the DefaultCmdSet to this object type
                    (important!)sets locks so character cannot be picked up
                    and its commands only be called by itself, not anyone else.
                    (to change things, use at_object_creation() instead)
    at_after_move - launches the "look" command
    at_post_puppet(player) -  when Player disconnects from the Character, we
                    store the current location, so the "unconnected" character
                    object does not need to stay on grid but can be given a
                    None-location while offline.
    at_pre_puppet - just before Player re-connects, retrieves the character's
                    old location and puts it back on the grid with a "charname
                    has connected" message echoed to the room

    """
    def at_object_creation(self):
        """

        Set up Fading Suns attributes.

        """
        self.db.attributes = {'Strength': 3, 'Dexterity': 3, 'Endurance': 3, 'Wits': 3, 'Perception': 3, 'Tech': 3, 'Presence': 3, 'Will': 3, 'Faith': 3}
        self.db.benefices = {}
        self.db.skills = {'Faction Lore.Phoenix Empire': 3, 'Fight': 3, 'Influence': 3, 'Observe': 3, 'Sneak': 3, 'Throwing': 3, 'Vigor': 3}
        self.db.vitality = 0
        self.db.wyrd = 0
        self.db.blessings = []
        self.db.curses = []
        self.db.afflictions = {}
        self.db.languages = [ 'Urthish' ]
        self.db.approved = 0
        self.db.house = 'None'
        self.db.archetype = 'None'
        self.db.questing = 0  # Track questing choice. Matters to CG because forces their first tour of duty to be the questing knight tour.
        self.db.actions = {}
        self.db.minor = 0
        self.db.recbenefices = []
        self.db.mirrorhouse = 'None'
        self.db.occult = {} # occult powers
        self.db.tours = [] # duty tours
        self.db.cyber = [] # Cybernetics
        self.db.notes = {}
        self.db.firebirds = 250
        self.db.assets = 0
        self.db.notifications = []
        self.db.mailsystem = []
        self.cmdset.add("fsunsset.FSunSet", permanent=True)
        self.cmdset.add("mailset.MailSet", permanent=True)
        
        
def at_pre_puppet(self, player, session=None):
    print "At pre puppet"
    if len(self.db.notifications) > 0:
        print "Pending Notifications"
        player.msg("SYSTEM: You have pending notifications. Type nn to read them.")
    