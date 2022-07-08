# enemy class for prototype
class Enemy:
    def __init__(self, hp, atk) -> None:
        self.hp = hp
        self.atk = atk

    def do_something():
        print('did something')

    def clone(self):
        return Enemy(self.hp, self.atk)

    def describe(self):
        print(self.hp)
        print(self.atk)

# another enemy type


class BigEnemy(Enemy):

    # add to parent init
    def __init__(self, hp, atk, height) -> None:
        self.height = height
        # use the rest of the params for Enemy init
        super(BigEnemy, self).__init__(hp, atk)

    def clone(self):
        return BigEnemy(self.hp, self.atk, self.height)

    def describe(self):
        print(self.height)
        print(self.hp)
        print(self.atk)
