"""
rules.py

Fading Suns World Rules Module
"""

from random import randint

def Roll():
    """
    Most rolls are 1d20
    """
    return randint(1,20)
    

def Roll6():
    """
    Some Rolls are 1d6
    """
    return randint(1,6)
    

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
        
        
def RollInit(player):
    return player.db.attributes['Dexterity'] + player.db.attributes['Wits'] + Roll6()
        
        
def WyrdDisplay(player):
    # Calculates and displays wyrd boxes
    temp = ''
    if player.db.wyrdused == 0:
        # No used wyrd, so this one is easy
        for i in range(0, player.db.wyrd):
            temp += "[ ]"
        return temp
    else:
        # Some wyrd used
        for i in range(0, player.db.wyrdused):
            temp += "[O]"
        for i in range(0, (player.db.wyrd - player.db.wyrdused)):
            temp += "[ ]"
        return temp
        

def VitalityDisplay(player):
    # Display the vitality boxes
    temp = ''
    if player.db.wounds == 0:
        #No wounds, easy one
        for i in range(0, player.db.vitality):
            temp += "[ ]"
        return temp
    else:
        # Some wounds
        for i in range(0, player.db.wounds):
            temp += "[X]"
        for i in range(0, (player.db.vitality - player.db.wounds)):
            temp += "[ ]"
        return temp
        
        
def WoundPenalty(player):
    # Determine Wound Penalty if any
    wpr = player.db.vitality - 5
    if player.db.wounds < wpr: # Wound penalties don't start till last 5 slots
        return 0
    else:
        # We have some
        if player.db.vitality - player.db.wounds == 5:
            return 2
        elif player.db.vitality - player.db.wounds == 4:
            return 4
        elif player.db.vitality - player.db.wounds == 3:
            return 6
        elif player.db.vitality - player.db.wounds == 2:
            return 8
        else:
            return 10
            
            
"""
GoalCheck

Takes a goal as either a number or calculation. Rolls a d20 and then gets VP from that roll.

Returns: Dictionary
    Contents of Dict:
        VP: VP given for Roll per VP Chart
        Result: Actual number Rolled on d20
        Check: Whether or not they passed the goal check
        
Special Notes:
    if Check is -1, They rolled a 20, which is a failure
    if Check is 0, they didn't put in a number or a calculation
    
Usage:
    Goals are always an Attribute+Skill.
    Complimentary Goal checks are done as separate rolls and are not directly added per rules.
    You can provide the goal as a number or calculation.
    For lores, omit the lore type. It doesn't look at that anyways. Extraneous spaces are stripped so they're fine.
    Capitalization does not matter since comparison are done through lower case.
    Examples:
        14 -  Goal is 14
        Strength+Fight - Goal is Strength+Fight
        Strength+4 - Goal is Strength+4
        10+Melee - Goal is 10+Melee
        Phoenix Empire + Intelligence - Goal is Lore Phoenix Empire + Intelligence
"""
def GoalCheck(goal, player):
    if goal.isnumeric():
        # Goal is a number, easy
        result = Roll()
        vpr = VP(result)
        if result == 20:
            return { 'VP': 0, 'Result': 20, 'Check': -1 }
        else:
            if result <= goal:
                return { 'VP': vpr, 'Result': result, 'Check': 1 }
            else:
                return { 'VP': vpr, 'Result': result, 'Check': 2 }
    elif '+' in goal:
        parts = goal.split("+")
        gc = 0
        for x in parts:
            if '-' in x:
                sub = x.split('-')
                if sub[1].strip().isdigit():
                    # Easiest, it's a number
                    gc -= int(sub[1].strip())
                else:
                    temp = attemptParse(sub[1].strip(), player)
                    if temp == 0:
                        return { 'VP': 0, 'Result': 0, 'Check': 0 }
                    else:
                        gc -= temp
                if sub[0].strip().isdigit():
                    # Easiest, it's a number
                    gc += int(sub[0].strip())
                else:
                    temp = attemptParse(sub[0].strip(), player)
                    if temp == 0:
                        return { 'VP': 0, 'Result': 0, 'Check': 0 }
                    else:
                        gc += temp
            elif not x.strip().isdigit():
                temp = attemptParse(x.strip(), player)
                if temp == 0:
                    return { 'VP': 0, 'Result': 0, 'Check': 0 }
                else:
                    gc += temp
            else:
                gc += int(x.strip())
        if gc <= 0:
            return { 'VP': 0, 'Result': 0, 'Check': 0 }
        else:
            result = Roll()
            vpr = VP(result)
            if result == 20:
                return { 'VP': 0, 'Result': 20, 'Check': -1 }
            else:
                if result <= gc:
                    return { 'VP': vpr, 'Result': result, 'Check': 1 }
                else:
                    return { 'VP': vpr, 'Result': result, 'Check': 2 }
    else:
        # I have no idea what they entered
        return { 'VP': 0, 'Result': 0, 'Check': 0 }
    
        
def attemptParse(what, who):
    for x in who.db.attributes:
        if x.lower() == what.lower():
            return who.db.attributes[x]
    for x in who.db.skills:
        if 'Lore' in x:
            if x.split('.')[1].lower() == what.lower():
                return who.db.skills[x]
        elif x.lower() == what.lower():
            return who.db.skills[x]
    return 0
        
    
# Roll d6's for weapon damage.    
def WeaponRoll(bonus):
    temp = ''
    for i in range(0,bonus):
        temp += str(Roll6()) + " "
    return temp