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
        print("parent CharacterState class update action")
        pass


# these are the states that the character can be in. The character will hold
# a state class in an instance variable and delegate the handle input and update calls to it
class JumpingState(CharacterState):
    # this allows me to omit self, remove if i need class variables from the State class
    # and subclass
    @staticmethod
    def handle_input(character, input_str):
        # if none input, return to standing
        # cannot duck
        if input_str == "none":
            character.state = character.static_standing_state  # swap states
        else:
            pass

    @staticmethod
    def update(character):
        print("jump update action")
        pass


class DuckingState(CharacterState):
    @staticmethod
    def handle_input(character, input_str):
        # if none input, return to standing
        # if w, then jump
        if input_str == "none":
            character.state = character.static_standing_state
        elif input_str == "w":
            character.state = character.static_jumping_state
        else:
            pass

    @staticmethod
    def update(character):
        print("duck update action")
        pass


class StandingState(CharacterState):
    @staticmethod
    def handle_input(character, input_str):
        # if none input, stay standing
        # if w input, jump
        # if s input, duck
        if input_str == "w":
            character.state = character.static_jumping_state
        elif input_str == "s":
            character.state = character.static_ducking_state
        else:
            pass

    @staticmethod
    def update(character):
        print("standing update action")
        pass
