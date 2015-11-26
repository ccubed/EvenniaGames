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
        self.db.attributes = {}
        self.db.benefices = {}
        self.db.skills = {}
        self.db.vitality = 0
        self.db.wyrd = 0
        self.db.blessings = ()
        self.db.curses = ()
        self.db.afflictions = {}
        self.db.languages = {}
        self.db.approved = 0
        self.db.house = 'None'
        self.db.archetype = 'None'
        self.db.choices = ()