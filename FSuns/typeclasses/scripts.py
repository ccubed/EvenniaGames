"""
Scripts

Scripts are powerful jacks-of-all-trades. They have no in-game
existence and can be used to represent persistent game systems in some
circumstances. Scripts can also have a time component that allows them
to "fire" regularly or a limited number of times.

There is generally no "tree" of Scripts inheriting from each other.
Rather, each script tends to inherit from the base Script class and
just overloads its hooks to have it perform its function.

"""

from evennia import DefaultScript
from datetime import *
from evennia.utils import search

class Assets(DefaultScript):
    "Gives monthly assets. Global Script."
    def at_script_creation(self):
        self.key = "Monthly_Assets"
        self.desc = "Gives monthly assets"
        self.interval = 86400 # 24 hours
        self.persistent = True
        
    def at_repeat(self):
        "called every 24 hours"
        if datetime.now().day == 1:
            # First day of the month, deposit time.
            players = evennia.search_object(1, typeclass="typeclasses.characters.Character", attribute_name="approved")
            for x in players:
                if 'Assets' in x.db.benefices:
                    if x.db.benefices['Assets'] == 4:
                        x.assets += 250
                    elif x.db.benefices['Assets'] == 8:
                        x.assets += 417
                    elif x.db.benefcies['Assets'] == 12:
                        x.assets += 833
                    elif x.db.benefices['Assets'] == 16:
                        x.assets += 1250
                    else:
                        x.assets += 1667
                        
                    if x.has_player() != 0:
                        x.msg("Your monthly assets have been deposited.")
                    else:
                        x.db.notifications.put_nowait((1,'{0}/{1}: Your monthly assets have been deposited.'.format(datetime.now().month,datetime.now().day)))