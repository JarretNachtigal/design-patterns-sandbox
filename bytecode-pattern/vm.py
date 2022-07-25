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
        # list of characters so that they can be indexed
        self.characters = [self.ch_one, self.ch_two]
        # create stack
        self.stack_instance = stack.Stack()
        # list of valid vm instructions and corresponding 'bytecode' (letter)
        self.instructions = {"a": "SET_CHARACTER",
                             "b": "SET_HP",
                             "c": "GET_HP",
                             "d": "SET_ATK",
                             "e": "GET_ATK",
                             "f": "SET_DEFENSE",
                             "g": "GET_DEFENSE",
                             "h": "PLAY_SOUND_DAMAGE",
                             "i": "PLAY_SOUND_HEAL",
                             "j": "INST_LITERAL"}

    # if else for self.instructions and instructions_list - bytecode from
    def interpret(self, instructions_list):
        # loop though given instructions_list bytecode
        for i, bytecode in enumerate(instructions_list):
            # get the string value for each bytecode
            instruction = self.instructions[bytecode]

            if instruction == "SET_CHARACTER":  # push 0 or 1 onto stack
                self.stack_instance.push(instructions_list[i+1])
                # skip number index in loop
                i += 1
            elif instruction == "SET_HP":
                # grab change_val off of stack
                change_val = self.stack_instance.pop()
                # grab character index off of stack
                index = self.stack_instance.pop()
                # get character current hp
                # math
                # set character hp
                pass
            elif instruction == "GET_HP":
                # grab character index off of stack
                # get character from index
                # push character hp onto stack
                pass
            elif instruction == "SET_ATK":
                # grab character index off of stack
                index = self.stack_instance.pop()
                pass
            elif instruction == "GET_ATK":
                # grab character index off of stack
                index = self.stack_instance.pop()
                # get character from index
                # push character atk onto stack
                pass
            elif instruction == "SET_DEFENSE":
                # grab character index off of stack
                index = self.stack_instance.pop()
                pass
            elif instruction == "GET_DEFENSE":
                # grab character index off of stack
                index = self.stack_instance.pop()
                # get character from index
                # push character defense onto stack
                pass
            elif instruction == "PLAY_SOUND_DAMAGE":
                # pretend to make game sounds
                print("imaginary damage sounds")
            elif instruction == "PLAY_SOUND_HEAL":
                # pretend to make game sounds
                print("imaginary heal sounds")
            elif instruction == "INST_LITERAL":
                # add next instruction to stack as an int
                self.stack_instance.push(instructions_list[i+1])
                # skip number index in loop
                i += 1
            else:
                print("broken :)")
