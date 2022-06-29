# this class will be a parent for all actors in the limited 'game'
class Actor:
    position = None
    jump_count = None

    # override
    def jump(self):
        self.jump_count += 1
        # raise NotImplementedError()  # makes sure its overridden

    # override
    def move(self):
        self.position += 1
        # raise NotImplementedError()  # makes sure its overridden

    def identify(self):
        raise NotImplementedError()  # makes sure its overridden


# not gonna make another file for these
# uses Actor class jump and move
class PlayableCharacter(Actor):
    def __init__(self) -> None:
        self.position = 0
        self.jump_count = 0

    def identify(self):
        print("i am a playable character")


# uses Actor class jump and move
class AICharacter(Actor):
    def __init__(self) -> None:
        self.position = 10
        self.jump_count = 0

    def identify(self):
        print("i am an AI character")
