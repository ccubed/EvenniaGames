"""

world/fsutils.py

Utility functions

"""

# add to a stat
def addsheet(pc, what, which, amt):
    if which == 'Attributes':
        if what in pc.db.attributes:
            pc.db.attributes[what] += amt
        else:
            pc.db.attributes[what] = amt
    elif which == 'Skills':
        if what in pc.db.skills:
            pc.db.skills[what] += amt
        else:
            pc.db.skills[what] = amt
    elif which == 'Afflictions':
        #  How do these work?
        pass
    elif which == 'Blessings':
        if not what in pc.db.blessings:
            pc.db.blessings.append(what)
    elif which == 'Curses':
        if not what in pc.db.curses:
            pc.db.curses.append(what)
    elif which == 'Languages':
        if not what in pc.db.languages:
            pc.db.languages.append(what)

