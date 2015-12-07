"""
Fsunsset

Fading Suns command set

"""

from evennia import CmdSet
from commands import fsunscmds

class FSunSet(CmdSet):
    def at_cmdset_creation(self):
        self.add(fsunscmds.Sheet())
