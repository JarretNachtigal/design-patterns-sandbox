import stack

# this class will take in bytecode from the filled stack
# and execute the correct steps at runtime
# it is a stack machine


class VM:
    def __init__(self) -> None:
        # instruction set corresponding to stack input
        self.stack_instance = stack.Stack()
        self.instructions = {"c": "SET_HP",
                             "d": "PLAY_SOUND_DAMAGE",
                             "e": "PLAY_SOUND_HEAL"}
        pass

    def interpret(self, bytecode_stack):
        pass
