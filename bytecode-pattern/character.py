# basic character class with 3 fields
# atk, hp, defence
# to interface with the stack instructions, it will heve general methods to manipulating
# its stats/state

class Character:
    def __init__(self, hp, atk, defence) -> None:
        self.hp = hp
        self.atk = atk
        self.defence = defence

    @staticmethod
    def setHealth(character, hp):
        character.hp = hp

    @staticmethod
    def setAtk(character, atk):
        character.atk = atk

    @staticmethod
    def setDefence(character, defense):
        character.defence = defense

    @staticmethod
    def getHealth(character):
        return character.hp

    @staticmethod
    def getAtk(character):
        return character.atk

    @staticmethod
    def getDefence(character):
        return character.defence
