import stack
import character

# this pattern involves creating building blocks that can be controlled
# with bytecode
# the instructions[] list will hold letters and numbers, representing valid
# instructions for the emulator
# it will be stepped through one char at a time for simplicity and mimic a user creating
# behavior by manipulating the stack at runtime
# 2 characters will be used to demonstrate


def main():
    instructions = []  # the user input - kinda pretend for now
    ch_one = character.Character(10, 2, 1)
    ch_two = character.Character(20, 3, 2)
    stack_instance = stack.Stack()

    stack_instance.handle_input()  # pass the instructions to the stack


if __name__ == "__main__":
    main()
