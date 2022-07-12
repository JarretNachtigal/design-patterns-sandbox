# parent class for all states that the character can be in
class CharacterState:

    def __init__(self) -> None:
        pass

    # will be overridden and used to make meaning of the player inputs given
    # the characters current state
    # it can change the state variable in the character instance to a different
    # CharacterState subclass if the input requires it
    def handle_input():
        pass

    # would be called once per game loop, could update graphics(unless that is also decoupled)
    # or other needed actions
    def update():
        pass


# these are the states that the character can be in. The character will hold
# a state class in an instance variable and delegate the handle input and update calls to it
class JumpingState(CharacterState):
    # this allows me to omit self, remove if i need class variables from the State class
    # and subclass
    @staticmethod
    def handle_input(character, input_str):
        pass

    @staticmethod
    def update(self, character):
        print("jump update action")
        pass


class DuckingState(CharacterState):
    @staticmethod
    def handle_input(self, character, input_str):
        pass

    @staticmethod
    def update(self, character):
        print("duck update action")
        pass


class StandingState(CharacterState):
    @staticmethod
    def handle_input(self, character, input_str):
        pass

    @staticmethod
    def update(self, character):
        print("standing update action")
        pass
