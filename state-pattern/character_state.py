# parent class for all states that the character can be in
class CharacterState:

    def __init__(self) -> None:
        pass

    # will be overridden and used to make meaning of the player inputs given
    # the characters current state
    def handle_input():
        pass

    # would be called once per game loop, could update graphics(unless that is also decoupled)
    # or other needed actions
    def update():
        pass


# these are the states that the character can be in. The character will hold
# a state class in an instance variable and delegate the handle input and update calls to it

#
class JumpingState(CharacterState):
    pass


class DuckingState(CharacterState):
    pass


class StandingState(CharacterState):
    pass
