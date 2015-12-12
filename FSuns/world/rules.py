"""
rules.py

Fading Suns World Rules Module

Reference: VP Chart
1: 0 (marginal)
2-3: 1
4-5: 2 (mediocre)
6-7: 3
8-9: 4 (satisfactory)
10-11: 5
12-13: 6 (Excellent)
14-15: 7
16-17: 8 (brilliant)
18-19: 9
20 - fail
"""

from random import randint

def Roll():
    """
    All rolls are 1d20
    """
    return randint(1,20)
    

def VP(roll):
    """
    Return VP given a roll.
    """
    if roll == 20 or roll == 1:
        return 0
    elif 2 <= roll <= 3:
        return 1
    elif 4 <= roll <= 5:
        return 2
    elif 6 <= roll <= 7:
        return 3
    elif 8 <= roll <= 9:
        return 4
    elif 10 <= roll <= 11:
        return 5
    elif 12 <= roll <= 13:
        return 6
    elif 14 <= roll <= 15:
        return 7
    elif 16 <= roll <= 17:
        return 8
    elif 18 <= roll <= 19:
        return 9
        