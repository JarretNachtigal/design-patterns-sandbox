import stack
import character

# this class will take in bytecode from the filled stack
# and execute the correct steps at runtime
# it is a stack machine


class VM:
    def __init__(self, ch_one, che_two) -> None:
        # instruction set corresponding to stack input
        ch_one = character.Character(10, 2, 1)
        ch_two = character.Character(20, 3, 2)
        self.stack_instance = stack.Stack()
        self.instructions = {"c": "SET_HP",
                             "d": "PLAY_SOUND_DAMAGE",
                             "e": "PLAY_SOUND_HEAL"}

    # switch case of self.instructions
    def interpret(self, instructions_list):
        pass
