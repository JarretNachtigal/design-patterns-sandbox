import enemy


# can hold a prototype of any enemy and then spawn new ones with the same attributes
class EnemyGenerator:
    def __init__(self, prototype: enemy.Enemy) -> None:
        self.prototype = prototype

    def spawn(self):
        return self.prototype.clone()
