"""
Fsunsset

Fading Suns command set

"""

from evennia import CmdSet
from commands import fsunscmds

class FSunSet(CmdSet):
    def at_cmdset_creation(self):
        self.add(fsunscmds.Sheet())
        self.add(fsunscmds.ChargenStart())
        self.add(fsunscmds.ApprovePC())
        self.add(fsunscmds.NotificationNext())
        self.add(fsunscmds.StaffNotify())
        self.add(fsunscmds.ReadAllNotifications())
        self.add(fsunscmds.RollGoalCheck())
        self.add(fsunscmds.AddResources())
        self.add(fsunscmds.RollWeaponDmg())
        self.add(fsunscmds.WriteBG())
        self.add(fsunscmds.ViewBG())