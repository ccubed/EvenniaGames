"""
Fsunscmds

Fading Suns specific commands.

"""

from evennia import default_cmds
from evennia.utils.evmenu import EvMenu
from evennia.utils import evtable
from evennia.utils.utils import *


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
    
    def func(self):
        self.caller.msg(pad("Demographics", width=80))
        self.caller.msg(pad("Name: " + self.caller.key, width=40, align="l") + pad("Archetype: " + self.caller.db.archetype, width=40, align="r"))
        self.caller.msg(pad("Faction: " + self.caller.db.house, width=40, align="l") + pad("Rank: " + self.caller.db.benefices['Rank'], width=40, align="r"))
        self.caller.msg(pad("Firebirds: " + self.caller.db.firebirds, width=40, align="l") + pad("Assets: " + self.caller.db.assets, width=40, align="r"))
        self.caller.msg(pad("Attributes", width=80, align="c", fillchar="="))
        table = evtable.EvTable("Body", "Mind", "Spirit", border="cells", width=80, align="c")
        table.add_row("Strength: " + str(self.caller.db.attributes['Strength']), "Wits: " + str(self.caller.db.attributes['Wits']), "Presence: " + str(self.caller.db.attributes['Presence']))
        table.add_row("Dexterity: " + str(self.caller.db.attributes['Dexterity']), "Perception: " + str(self.caller.db.attributes['Perception']), "Will: " + str(self.caller.db.attributes['Will']))
        table.add_row("Endurance: " + str(self.caller.db.attributes['Endurance']), "Tech: " + str(self.caller.db.attributes['Tech']), "Faith: " + str(self.caller.db.attributes['Faith']))
        self.caller.msg(table)
        table = evtable.EvTable(width=80, align="c", border="cells")
        self.caller.msg(pad("Skills", width=80, align="c", fillchar="="))
        i = 0
        rows = []
        for x in self.caller.db.skills.keys():
            rows.append(x + ': ' + str(self.caller.db.skills[x]))
            if i == 2:
                table.add_rows(rows)
                rows = []
            else:
                i += 1
        self.caller.msg(table)
        if len(self.caller.db.occult):
            self.caller.msg(pad("Occult", width=80, align="c", fillchar="="))
            for x in self.caller.db.occult.keys():
                self.caller.msg(wrap(x + ": " + self.caller.db.occult[x], width=80, indent=3))
        if len(self.caller.db.actions):
            self.caller.msg(pad("Fighting Styles", width=80, align="c", fillchar="="))
            for x in self.caller.db.actions.keys():
                self.caller.msg(wrap(x + ": " + self.caller.db.actions[x], width=80, indent=3))
        if len(self.caller.db.languages):
            table = evtable.EvTable(width=80, align="c", border="cells")
            i = 0
            rows = []
            self.caller.msg(pad("Languages", width=80, align="c", fillchar="="))
            for x in self.caller.db.languages:
                rows.append(x)
                if i == 2:
                    table.add_rows(rows)
                    rows = []
                else:
                    i += 1
            self.caller.msg(table)
            
            
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
    
    def func(self):
        EvMenu(self.caller, "typeclasses.fsunscg", startnode="menunode_start", cmdset_mergetype="union", allow_quit="true", cmd_on_quit="look")