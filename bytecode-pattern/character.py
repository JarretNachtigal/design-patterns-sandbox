# basic character class with 3 fields
# atk, hp, defence
class Character:
    def __init__(self, hp, atk, defence) -> None:
        self.hp = hp
        self.atk = atk
        self.defence = defence
