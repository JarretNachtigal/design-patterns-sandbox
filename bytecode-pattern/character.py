# basic character class with 3 fields
# atk, hp, defence
# to interface with the stack instructions, it will heve general methods to manipulating
# its stats/state

class Character:
    def __init__(self, hp, atk, defence) -> None:
        self.hp = hp
        self.atk = atk
        self.defence = defence

    def setHealth(self, change_val):
        self.hp += change_val

    def setAtk(character, change_val):
        character.atk += change_val

    def setDefence(self, change_val):
        self.defence += change_val

    def getHealth(self):
        return self.hp

    def getAtk(self):
        return self.atk

    def getDefence(self):
        return self.defence
