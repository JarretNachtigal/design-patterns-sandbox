import vm

# this pattern involves creating building blocks that can be controlled
# with bytecode
# the instructions[] list will hold letters and numbers, representing valid
# instructions for the emulator
# it will be stepped through one char at a time for simplicity and mimic a user creating
# behavior by manipulating the stack at runtime
# 2 characters will be used to demonstrate

# self.instructions = {"c": "SET_HP",
#                      "d": "PLAY_SOUND_DAMAGE",
#                      "e": "PLAY_SOUND_HEAL"}


def main():
    # create characters

    # the user input - kinda pretend for now
    basic_attack = ["a", "c", "b"]  # ch_one basic attack ch_two

    machine = vm.VM()
    machine.interpret()  # takes the stack, executes intructions


if __name__ == "__main__":
    main()
