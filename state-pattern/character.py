import character_state


# class used to create the player character object
# delegates handle input and update methods to character_state
# and its subclasses, which will be stored in an instance variable
class Character:
    def __init__(self, hp) -> None:
        self.hp = hp
        self.state = character_state.StandingState()  # character spawns standing
