import stack
import character
import vm

# this pattern involves creating building blocks that can be controlled
# with bytecode
# the instructions[] list will hold letters and numbers, representing valid
# instructions for the emulator
# it will be stepped through one char at a time for simplicity and mimic a user creating
# behavior by manipulating the stack at runtime
# 2 characters will be used to demonstrate

# a - ch_one
# b - ch_two
# c - sethp


def main():
    instructions = {"c": "SET_HP",
                    "d": "PLAY_SOUND_DAMAGE",
                    "e": "PLAY_SOUND_HEAL"}

    ch_one = character.Character(10, 2, 1)
    ch_two = character.Character(20, 3, 2)

    # the user input - kinda pretend for now
    input = ["a", "c", "b"]  # ch_one basic attack ch_two

    stack_instance = stack.Stack()

    machine = vm.VM()
    machine.interpret(stack_instance)  # takes the stack, executes intructions


if __name__ == "__main__":
    main()
