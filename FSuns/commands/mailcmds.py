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

# Note: Sender, Title, Message, Datetime

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
            self.caller.msg("{0:>3} {1:>4} {2:^20} {3:^36}".format("ID", "Date", "Sender", "Subject"))
            i = 0
            for x in self.caller.db.mailsystem:
                self.caller.msg("{0:>3} {1:>4} {2:^20} {3:^36}".format(i,str(x[3].month) + "/" + str(x[3].day), x[0], x[1]))
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
        elif not self.args.isnumeric():
            self.caller.msg("SYSTEM: Index must be a number.")
        elif int(self.args) > len(self.caller.db.mailsystem)-1:
            self.caller.msg("SYSTEM: You don't have that many mails.")
        else:
            mail = self.caller.db.mailsystem[int(self.args)]
            self.caller.msg(pad(" Mail Sys ", width=80, fillchar="="))
            self.caller.msg(pad(mail[1], width=80))
            self.caller.msg("{0:39} {1:>39}".format("To: " + self.caller.key, "From: " + mail[0]))
            self.caller.msg("{0:^80}".format('Sent on ' + str(mail[3].month) + '/' + str(mail[3].day) + '/' + str(mail[3].year)))
            self.caller.msg(pad('=',width=80,fillchar='='))
            evmore.msg(self.caller, mail[2] + "\n")
            
        
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
        elif not self.args.isnumeric():
            self.caller.msg("SYSTEM: Index must be a number.")
        elif int(self.args) > len(self.caller.db.mailsystem)-1:
            self.caller.msg("SYSTEM: You don't have that many mails.")
        else:
            self.caller.db.mailsystem.remove(mail)
            self.caller.msg("SYSTEM: Removed mail " + mail[1] + " from your inbox.")
        
        
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
        temp = Mail(self.caller.key, self.caller.ndb.mailtitle, self.caller.ndb.message, datetime.now())
        caller.ndb.mailtarget.db.mailsystem.append(temp)
        #caller.ndb.mailtarget.db.notifications.append("{0}/{1}: New Mail from {2} about {3}".format(temp[3].month, temp[3].day, self.caller.key, temp[1]))
        del caller.ndb.message
        del caller.ndb.mailtitle
        #caller.msg("Sent your letter to {0}.".format(caller.ndb.mailtarget.key)) 
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
            get_input(self.caller, "SYSTEM: What is the subject of this mail?", self.MailSubject)
            return True
            
            
    def MailSubject(self, caller, prompt, user_input):
        print "MailSubject: We got " + user_input
        caller.ndb.mailtitle = user_input
        key = "{0} to {1}".format(user_input, caller.ndb.mailtarget.key)
        eveditor.EvEditor(self.caller, savefunc=self.save, quitfunc=self.quit, key=key)
    
    
    def func(self):
        print "Mailing. Got this: " + self.args
        if not self.args:
            get_input(self.caller, "SYSTEM: Who are you sending mail to?", self.MailTo)
        else:
            target = search.search_object(self.args.split('/')[0], typeclass="typeclasses.characters.Character")
            title = self.args.split('/')[1].split('=')[0]
            message = self.args.split('/')[1].split('=',1)[1]
            if len(target) == 0:
                caller.msg("SYSTEM: That didn't match a player. Confirm the player's name and try again.")
            elif len(target) > 1:
                caller.msg("SYSTEM: That matched several players. Maybe try an alias?")
            else: 
                target = target[0]
                temp = [ self.caller.key, title, message, datetime.now() ]
                target.db.mailsystem.append(temp)
                self.caller.msg("Sent your mail to {0}".format(target.key))
                msg = "{0}/{1}: New mail from {2} about {3}.".format(temp[3].month, temp[3].day, self.caller.key, temp[1])
                target.db.notifications.append(msg)
                if target.has_player:
                    target.msg("SYSTEM: You have pending notifications.")