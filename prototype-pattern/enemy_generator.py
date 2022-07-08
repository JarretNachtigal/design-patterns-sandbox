import enemy


class enemy_generator:
    def __init__(self, prototype: enemy.Enemy) -> None:
        self.prototype = prototype

    # i guess this is how this works. probably could be built to be more reusable with
    # better methods for different enemy types, ex: a method in each enemy type that returns all its data
    # instead of individual generators
    def clone(self):
        return enemy.Enemy(self.prototype.get_hp(), self.prototype.get_atk())
