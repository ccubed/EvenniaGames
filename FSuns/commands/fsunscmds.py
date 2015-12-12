"""
Fsunscmds

Fading Suns specific commands.

"""

from evennia import default_cmds
from evennia.utils.evmenu import EvMenu
from evennia.utils import evtable
from evennia.utils.utils import *
from evennia.utils import search
from datetime import *


class Sheet(default_cmds.MuxCommand):
    """
    Sheet Display
    
    Usage:
        +sheet, sheet, score
        
    Display your sheet.
    """
    
    key = "+sheet"
    aliases = [ 'sheet', 'score' ]
    locks = "cmd:all()"
    help_category = "Characters"
    
    def func(self):
        if self.caller.db.house == 'None':
            self.caller.msg('Go through CG first. Type +cg.')
        else:
            self.caller.msg(pad("Demographics", width=80))
            self.caller.msg(pad("Name: " + self.caller.key, width=40, align="l") + pad("Archetype: " + self.caller.db.archetype, width=40, align="r"))
            self.caller.msg(pad("Faction: " + self.caller.db.house, width=40, align="l") + pad("Rank: " + self.caller.db.benefices['Rank'], width=40, align="r"))
            self.caller.msg(pad("Firebirds: " + str(self.caller.db.firebirds), width=40, align="l") + pad("Assets: " + str(self.caller.db.assets), width=40, align="r"))
            self.caller.msg(pad("Attributes", width=80, align="c", fillchar="="))
            table = evtable.EvTable("Body", "Mind", "Spirit", border="cells", width=80, align="c")
            table.add_row("Strength: " + str(self.caller.db.attributes['Strength']), "Wits: " + str(self.caller.db.attributes['Wits']), "Presence: " + str(self.caller.db.attributes['Presence']))
            table.add_row("Dexterity: " + str(self.caller.db.attributes['Dexterity']), "Perception: " + str(self.caller.db.attributes['Perception']), "Will: " + str(self.caller.db.attributes['Will']))
            table.add_row("Endurance: " + str(self.caller.db.attributes['Endurance']), "Tech: " + str(self.caller.db.attributes['Tech']), "Faith: " + str(self.caller.db.attributes['Faith']))
            self.caller.msg(table)
            self.caller.msg(pad(" Skills ", width=80, align="c", fillchar="="))
            i = 0
            temp = ''
            for x in self.caller.db.skills.keys():
                if 'Lore' not in x:
                    temp += "{0:^16}: {1:>6} ".format(crop(x, 16, '...'), self.caller.db.skills[x])
                    if i == 2:
                        self.caller.msg(temp)
                        temp = ''
                        i=0
                    else:   
                        i+=1
            self.caller.msg(pad(" Lores ", width=80, align="c", fillchar="="))
            i = 0
            temp = ''
            for x in self.caller.db.skills.keys():
                if 'Lore' in x:
                    print x
                    print x.split('.')
                    temp += "{0:^16}: {1:>6}".format(crop(x.split('.')[1],16,'...'), self.caller.db.skills[x])
                    if i == 1:
                        self.caller.msg(temp)
                        temp = ''
                        i = 0
                    else:
                        i += 1
            if len(self.caller.db.occult):
                self.caller.msg(pad(" Occult ", width=80, align="c", fillchar="="))
                for x in self.caller.db.occult.keys():
                    self.caller.msg(wrap(x + ": " + self.caller.db.occult[x], width=80, indent=3))
            if len(self.caller.db.actions):
                self.caller.msg(pad(" Fighting Styles ", width=80, align="c", fillchar="="))
                for x in self.caller.db.actions.keys():
                    self.caller.msg(wrap(x + ": " + self.caller.db.actions[x], width=80, indent=3))
            if len(self.caller.db.languages):
                self.caller.msg(pad(" Languages ", width=80, align="c", fillchar="="))
                temp = ''
                i = 0
                for x in self.caller.db.languages:
                    temp += "{0:^16}".format(crop(x,16,'...'))
                    if i == 2:
                        self.caller.msg(temp)
                        i = 0
                    else:
                        i += 1
            
            
class ChargenStart(default_cmds.MuxCommand):
    """
    Enter Chargen
    
    Usage:
        +cg, cg, chargen, start
        
    Start chargen.
    """
    
    key = "+cg"
    aliases = [ 'cg', 'chargen', 'start' ]
    locks = "cmd:attr(approved,0)"
    help_category = "Characters"
    
    def func(self):
        EvMenu(self.caller, "typeclasses.fsunscg", startnode="menunode_start", cmdset_mergetype="union", allow_quit="true", cmd_on_quit="look")
        

class ApprovePC(default_cmds.MuxCommand):
    """
    Approve a PC for play.
    
    Usage:
        @approve <name>
        
    Approve a player for play.
    """
    
    key = "@approve"
    lock = "cmd:perm(Wizards)"
    help_category = "Staff"
    
    def func(self):
        target = search.search_object(self.args, typeclass="typeclasses.characters.Character")
        if len(target) == 1:
            target[0].db.approved = 1
            self.caller.msg("SYSTEM: You have approved " + target.key + " for play.")
            if target[0].has_player:
                target[0].msg("SYSTEM: You have been approved for play by " + self.caller.key)
            else:
                now = datetime.now()
                target[0].db.notifications.append("{0}/{1}: Approved for play by {2}.".format(now.month, now.day, self.caller.key))
        else:
            if len(target) > 1:
                self.caller.msg("SYSTEM: " + self.args + " matched several Characters.")
            else:
                self.caller.msg("SYSTEM: " + self.args + " didn't match a Character.")
                
                
class NotificationNext(default_cmds.MuxCommand):
    """
    Read next notification.
    
    Usage:
        nn, +nn, notification/next, +notification/next
        
    Read next notification.
    """
    
    key = "nn"
    aliases = [ "+nn" ]
    lock = "cmd:all()"
    help_category = "Notifications"
    
    def func(self):
        if len(self.caller.db.notifications) == 0:
            self.caller.msg("SYSTEM: There aren't any notifications in your queue.")
        else:
            temp = self.caller.db.notifications[0]
            self.caller.msg(temp)
            self.caller.db.notifications.remove(temp)
            
            
class StaffNotify(default_cmds.MuxCommand):
    """
    Allows staff to add a notification to a player.
    
    Usage:
        @n/add <name>=<msg>
        
    Allows staff to add a notification to a player.
    """
    
    key = "@n/add"
    lock = "cmd:perm(Wizards)"
    help_category = "Staff"
    
    def func(self):
        target = search.search_object(self.args.split('=')[0], typeclass="typeclasses.characters.Character")
        if len(target) == 1:
            prefix = "From {0} on {1}/{2}: ".format(self.caller.key,datetime.now().month,datetime.now().day)
            target[0].db.notifications.append(prefix + self.args.split('=',1)[1])
            self.caller.msg("SYSTEM: Added notification to " + target[0].key + "'s queue.")
            if target[0].has_player:
                target[0].msg("SYSTEM: You have pending notifications.")
        else:
            if len(target) > 1:
                self.caller.msg("SYSTEM: That matched more than one player.")
            else:
                self.caller.msg("SYSTEM: That did not match a player.")