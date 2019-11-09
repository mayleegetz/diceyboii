import random, names, backstory

#prints the menus to be used in main
def menus():
    print("""welcome to the dnd thing
choose an option to continue
[r] for roller
[s] for a set of stats
[n] for a random name
[b] for a generic backstory
[q] to quit""")
    return

def optionSelector():
    option = ""
    option = input("choice? ")
    print("\n")
    if option == "q":
        print("goodbye")
        return False
    if option != "r" and option != "n" and option != "b" and option != "s":
        print("not an option, buddy \n \n")
        return True
    if option == "r":
        rolls()
    if option == "s":
        stats()
    if option == "n":
        n()
    if option == "b":
        backstorys()
    print("\n\n")
    return True


#rolls the dice
def rolls():
    numDice=input("how many dice? ")
    numSize=input("and of what size? ")
    i=0
    nums=[]
    total=0
    for i in range(int(numDice)):
        nums.append(random.randrange(int(numSize))+1)
        total+=nums[i]

    print("you rolled ", str(total) + ". ", end="(")
    for i in range(int(numDice)-1):
        print(str(nums[i]) + ",", end="")
    print(str(nums[i+1]) + ")", end="")
    return

def stats():
    i=0
    totals=[]
    for i in range(6):
        totals.append(oneStat())

    i=0
    for i in range(5):
        print(str(totals[i]) + ",", end="")
    print(str(totals[i+1]) , end="")
    return

def oneStat():
    i=0
    nums=[]
    total=0
    for i in range(4):
        nums.append(random.randrange(6)+1)
        total+=nums[i]
    total-=min(nums)
    return total


def n():
    print("choose a character race!")
    print("you can be a half-orc, dwarf, elf, halfing, gnome, dragonborn, human, tiefling, or a half-elf")
    race = input()
    gender = input("male or female: ")
    namess = names.Names(race, gender)
    namess.setname()
    print(str(namess.getname()))
    return

def backstorys():
    print(str(backstory.getstory()))
    return

def main():
    go=True
    while go:
        menus()
        go=optionSelector()
    print("©daftFunc() 2019")
    return

main()
