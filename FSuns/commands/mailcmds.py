"""
mailcmds

Making a mail system in python. Woot.

"""

from evennia import default_cmds
from evennia.utils.utils import *
import collections

Mail = collections.namedtuple('Mail', ['sender', 'title', 'message', 'date'])

class MailList(default_cmds.MuxCommand):
    """
    List available Mails
    
    Usage:
        @mail, +mail, mail
        
    List available Mails
    """
    
    key = "@mail"
    aliases = [ '+mail', 'mail' ]
    locks = "cmd:all()"
    
    def func(self):
        if len(self.caller.db.mailsystem) == 0:
            self.caller.msg("You don't have any mails.")
        else:
            self.caller.msg("{0:3} {1:4} {2:20} {3:^36}".format("ID", "Date", "Sender", "Subject"))
            i = 0
            for x in self.caller.db.mailsystem:
                self.caller.msg("{0:3} {1:4} {2:20} {3:^36}".format(i,x['date'].month + "/" + x['date'].day, x['sender'], x['title']))
                

class MailRead(default_cmds.MuxCommand):
    """
    Read a mail
    
    Usage:
    read #, @read #, +read #
    
    Read a mail
    """
    
    key = "@read"
    aliases = [ "+read", "read" ]
    locks = "cmd:all()"
    
    def func(self):
        