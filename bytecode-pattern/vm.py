import stack
import character

# this class will take in bytecode from the filled stack
# and execute the correct steps at runtime
# it is a stack machine


class VM:
    def __init__(self, ch_one, che_two) -> None:
        # instruction set corresponding to stack input
        self.ch_one = character.Character(10, 2, 1)
        self.ch_two = character.Character(20, 3, 2)
        self.stack_instance = stack.Stack()
        # list of valid vm instructions and corresponding 'bytecode' (letter)
        self.instructions = {"a": "SET_CHARACTER",
                             "c": "SET_HP",
                             "d": "PLAY_SOUND_DAMAGE",
                             "e": "PLAY_SOUND_HEAL",
                             "f": "INST_LITERAL"}

    # switch case of self.instructions
    def interpret(self, instructions_list):
        # loop though given instructions_list bytecode
        for i, bytecode in enumerate(instructions_list):
            # get the string value for each bytecode
            instruction = self.instructions[bytecode]

            if instruction == "SET_CHARACTER":  # push 0 or 1 onto stack
                self.stack_instance.push(instructions_list[i+1])
                # remove from instructions list to prevent breaking the ifelse
                del instructions_list[i+1]
            elif instruction == "SET_HP":
                pass
            elif instruction == "GET_HP":
                pass
            elif instruction == "SET_ATK":
                pass
            elif instruction == "GET_ATK":
                pass
            elif instruction == "SET_DEFENSE":
                pass
            elif instruction == "GET_DEFENSE":
                pass
            elif instruction == "PLAY_SOUND_DAMAGE":
                print("imaginary damage sounds")
            elif instruction == "PLAY_SOUND_HEAL":
                print("imaginary heal sounds")
            elif instruction == "INST_LITERAL":
                # add next instruction to stack as an int
                self.stack_instance.push(instructions_list[i+1])
                # remove from instructions list to prevent breaking the ifelse
                del instructions_list[i+1]
            else:
                print("broken :)")
