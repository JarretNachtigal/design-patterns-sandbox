# basic character class with 3 fields
# atk, hp, defence
# to interface with the stack instructions, it will heve general methods to manipulating
# its stats/state
from re import L


class Character:
    def __init__(self, hp, atk, defence) -> None:
        self.hp = hp
        self.atk = atk
        self.defence = defence

    # these methods will take a character to manipulate as an argument rather
    # than useing self

    @staticmethod
    def setHealth(character, change_val):
        return character

    @staticmethod
    def setHp(character, change_val):
        return character

    @staticmethod
    def setDefence(character, change_val):
        return character
