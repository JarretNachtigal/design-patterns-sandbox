import character_state


# class used to create the player character object
# delegates handle input and update methods to character_state
# and its subclasses, which will be stored in an instance variable
class Character:

    def __init__(self, hp) -> None:
        # these are the 3 states, static approach
        # creating them this way is bigger at the beginning but less intensive at runtime
        self.static_standing_state = character_state.StandingState()
        self.static_ducking_state = character_state.DuckingState()
        self.static_jumping_state = character_state.JumpingState()
        self.hp = hp
        self.state = self.static_standing_state  # character spawns standing

    def handle_input(self, s):
        # pass the call along to the current State class
        self.state.handle_input(self, s)
