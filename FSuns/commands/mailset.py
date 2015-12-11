"""
mailset

Mail commands

"""

from evennia import CmdSet
from commands import mailcmds

class MailSet(CmdSet):
    def at_cmdset_creation(self):
        self.add(mailcmds.MailList())
        self.add(mailcmds.MailRead())
        self.add(mailcmds.MailDelete())
        self.add(mailcmds.MailSend())