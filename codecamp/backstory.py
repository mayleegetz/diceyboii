import random

def getstory():
    parents = ['you do know who your parents are. ', 'you do not know who your parents are. ']
    birthplace = ['at home. ', 'in a cave. ', 'in the home of a healer or midwife. ', 'in the Shadowfell. ', 'in a forest. ', 'in a field. ']
    grewup = ['in a temple. ', 'in a castle. ','comfortably with both parents. ', 'modest with your mother and father. ', 'wretchedly with your mother and father. ', 'poor with your paternal or maternal granparents. ', 'with your adopted parents. ', 'with your single mother. Your father vanished to an unkown place. ', 'with your single father. Your mother vanished to an unkown place. ','with your single mother. Your father passed away before you were born. ','with your single father. Your mother passed away before you were born. ','with a gaurdian. Your mother died and your father abandoned you at a young age. ','with a gaurdian. Your father died and your mother abandoned you at a young age.']
    siblings = ['have no siblings. ', 'have 3 siblings, all older than you. ', '2 siblings, 1 older and 1 younger. ', '6 siblings, all younger than you. ' ]
    livedin = ['in a mansion. ', 'in a shack. ', 'in a large house. ', 'in a small house. ', 'in an encampment or village in the wilderness. ','without permanent residence; I moved around a lot. ']
    friends = ['many friends. Others saw you as fun and charming. ', 'little friends. Others found you as different or strange. ']
    background = ['Acolyte', 'Charlatan', 'Criminal', 'Entertainer', 'Folk Hero', 'Guild Artisan', 'Hermit', 'Noble', 'Outlander', 'Sage', 'Sailor', 'Soldier', 'Urchin']
    classes = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']
    age = ['20 years old or younger. ', '21-30 years old. ', '41-50 years old. ', '51-60 years old. ', '61 years old or older. ']
    lifestory = ['You spent time working in a job related to your background. Start game with an extra 2gp. ', 'You fell in love and got married. If this event happens more than once, you may choose to have a child. ', 'you made an enemy. '     ,  'you made a friend. '     ]

    print('you are a(n) ' + str(classes[random.randrange(len(classes))]) + ', ' + str(background[random.randrange(len(background))]) + ' - ' + str(age[random.randrange(len(age))]) , end = '')
    #print('Family', end="")
    print(str(parents[random.randrange(len(parents))]), end="")
    print('you were born ' + str(birthplace[random.randrange(len(birthplace))]) ,end="")
    print('you grew up ' + str(grewup[random.randrange(len(grewup))])  ,end="")
    print('you ' + str(siblings[random.randrange(len(siblings))]) ,end="")

    #print('Childhood' ,end="")
    print('you lived ' + str(livedin[random.randrange(len(livedin))]) ,end="")
    print('you had ' + str(friends[random.randrange(len(friends))]) ,end="")
    # print('you became a(n) ' + background ,end="")
    # print('you also became a(n) ' + classes ,end="")

    #print('life so far' ,end="")
    # print('you are ' + age ,end="")
    print(str(lifestory[random.randrange(len(lifestory))]) ,end="")

    return

def main():
    getstory()
    return
