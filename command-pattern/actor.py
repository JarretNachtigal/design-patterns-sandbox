# this class will be a parent for all actors in the limited 'game'
class Actor:
    position = None
    jump_count = None


# not gonna make another file for these
class PlayableCharacter(Actor):
    def __init__(self) -> None:
        self.position = 0
        self.jump_count = 0


class AICharacter(Actor):
    def __init__(self) -> None:
        self.position = 10
        self.jump_count = 0
