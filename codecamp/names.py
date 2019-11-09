import random, namelist

class Names:

    def __init__(self, race, gender):
        self.race = race
        self.gender = gender
        self.name = ""

    def getname(self):
        return self.name

    def getgender(self):
        return self.gender

    def setrace(race):
        self.race = race

    def setgender(gender):
        self.gender = gender

    def setname(self):

        if self.race == "half-orc":
            self.name = namelist.orks(self.gender)

        elif self.race == "dwarf":
            self.name = namelist.dwarf(self.gender)

        elif self.race == "elf":
            self.name = namelist.elf(self.gender)

        elif self.race == "halfing":
            self.name = namelist.halfing(self.gender)

        elif self.race == "gnome":
            self.name = namelist.gnome(self.gender)

        elif self.race == "dragonborn":
            self.name = namelist.dragon(self.gender)

        elif self.race == "human":
            self.name = namelist.human(self.gender)

        elif self.race == "half-elf":
            num = random.randrange(2)
            if num == 1:
                self.name = namelist.human(self.gender)
            else:
                self.name = namelist.elf(self.gender)

        elif self.race == "tiefling":
            self.name = namelist.tiefling(self.gender)

        else:
            self.name = namelist.generic(self.gender)
