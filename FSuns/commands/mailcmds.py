"""
mailcmds

Making a mail system in python. Woot.

"""

from evennia import default_cmds
from evennia.utils.utils import *
from evennia.utils import evmore
from evennia.utils import eveditor
from evennia.utils.evmenu import get_input
from evennia.utils import search
from datetime import *
import collections

Mail = collections.namedtuple('Mail', ['sender', 'title', 'message', 'date'])

class MailList(default_cmds.MuxCommand):
    """
    List available Mails
    
    Usage:
        +mail, mail
        
    List available Mails
    """
    
    key = "mail"
    aliases = [ '+mail' ]
    locks = "cmd:all()"
    help_category = "Mail"
    
    def func(self):
        if len(self.caller.db.mailsystem) == 0:
            self.caller.msg("SYSTEM: You don't have any mails.")
        else:
            self.caller.msg("{0:3} {1:4} {2:20} {3:^36}".format("ID", "Date", "Sender", "Subject"))
            i = 0
            for x in self.caller.db.mailsystem:
                self.caller.msg("{0:3} {1:4} {2:20} {3:^36}".format(i,x['date'].month + "/" + x['date'].day, x['sender'], x['title']))
                i += 1
                

class MailRead(default_cmds.MuxCommand):
    """
    Read a mail
    
    Usage:
    read #, +read #
    
    Read a mail
    """
    
    key = "read"
    aliases = [ "+read" ]
    locks = "cmd:all()"
    help_category = "Mail"
    
    def func(self):
        if len(self.caller.db.mailsystem) == 0:
            self.caller.msg("SYSTEM: You don't have any mail!")
        elif not self.args.is_digit():
            self.caller.msg("SYSTEM: Input the index.")
        elif self.args > len(self.caller.db.mailsystem):
            self.caller.msg("SYSTEM: You don't have that many mails.")
        else:
            mail = self.caller.db.mailsystem[int(self.args)]
            self.caller.msg(pad(mail['title'], width=80))
            self.caller.msg("{0:39} {1:<39}".format("To: " + self.caller.key, "From: " + mail['sender']))
            self.caller.msg("{0:^80}".format('Sent on ' + mail['date'].month + '/' + mail['date'].day + '/' + mail['date'].year))
            self.caller.msg(pad('=',width=80,fillchar='='))
            evmore.msg(self.caller, mail['message'])
            
        
class MailDelete(default_cmds.MuxCommand):
    """
    Delete a mail
    
    Usage:
    delete #, +delete #
    
    Delete a mail
    """
    
    key = "delete"
    aliases = [ "+delete" ]
    locks = "cmd:all()"
    help_category = "Mail"
    
    def func(self):
        if len(self.caller.db.mailsystem) == 0:
            self.caller.msg("SYSTEM: You don't have any mail!")
        elif not self.args.is_digit():
            self.caller.msg("SYSTEM: Input the index.")
        elif self.args > len(self.caller.db.mailsystem):
            self.caller.msg("SYSTEM: You don't have that many mails.")
        else:
            self.caller.db.mailsystem.remove(mail)
            self.caller.msg("SYSTEM: Removed mail " + mail['title'] + " from your inbox.")
        
        
class MailSend(default_cmds.MuxCommand):
    """
    Send a mail
    
    Usage:
    There are two uses here. You can type send by itself and be prompted for the options.
    Or you can type send to/title=msg.
    You can also substitute +send for send.
    
    Send a mail
    """
    
    key = "send"
    aliases = [ "+send" ]
    locks = "cmd:all()"
    help_category = "Mail"
        
        
    def save(self, caller, buffer):
        caller.ndb.message = buffer
    
        
    def quit(self, caller):
        temp = Mail(caller.key, caller.ndb.mailtitle, caller.ndb.message, datetime.now())
        caller.ndb.mailtarget.db.mailsystem.append(temp)
        caller.ndb.mailtarget.db.notifications.append("{0}/{1}: New Mail from {2} about {3}".format(temp['date'].month, temp['date'].day, caller.key, temp['title']))
        del caller.ndb.message
        del caller.ndb.mailtitle
        caller.msg("Sent your letter to {0}.".format(caller.ndb.mailtarget.key)) 
        if caller.ndb.mailtarget.has_player:
            caller.ndb.mailtarget.msg("SYSTEM: You have pending notifications.")
        del caller.ndb.mailtarget
        
    
    def MailTo(self, caller, prompt, user_input):
        target = search.search_object(user_input, typeclass="typeclasses.characters.Character")
        if len(target) == 0:
            caller.msg("SYSTEM: That didn't match a player. Confirm the player's name and try again.")
        elif len(target) > 1:
            caller.msg("SYSTEM: That matched several players. Maybe try an alias?")
        else:
            caller.ndb.mailtarget = target[0]
            get_input(caller, "SYSTEM: What is the subject of this mail?", self.MailSubject)
            
            
    def MailSubject(self, caller, prompt, user_input):
        caller.ndb.mailtitle = user_input
        key = "{0} to {1}".format(user_input, caller.ndb.mailtarget.key)
        eveditor.EvEditor(self.caller, savefunc=self.save, quitfunc=self.quit, key=key)
    
    
    def func(self):
        print "Mailing. Got this: " + self.args
        if not self.args:
            get_input(self.caller, "SYSTEM: Who are you sending mail to?", self.MailTo)
        else:
            target = search.search_object(self.args[0].split('/')[0], typeclass="typeclasses.characters.Character")
            title = self.args[0].split('/').split('=')[0]
            message = self.args[0].split('/').split('=',1)[1]
            if len(target) == 0:
                caller.msg("SYSTEM: That didn't match a player. Confirm the player's name and try again.")
            elif len(target) > 1:
                caller.msg("SYSTEM: That matched several players. Maybe try an alias?")
            else: 
                temp = Mail(self.caller.key, title, message, datetime.now())
                target.db.mailsystem.append(temp)
                self.caller.msg("Sent your mail to {0}".format(target.key))
                target.db.notifications.append("{0}/{1}: New mail from {2} about {3}.".format(temp['date'].month, temp['date'].day, self.caller.key, temp['title']))
                if target.has_player:
                    target.msg("SYSTEM: You have pending notifications.")