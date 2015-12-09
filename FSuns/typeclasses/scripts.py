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
import datetime import *

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
            