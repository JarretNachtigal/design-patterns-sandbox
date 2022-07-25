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
    # the user input - kinda pretend for now
    # something will have to generate this in practice
    basic_attack = ["a", "c", "b"]  # ch_one basic attack ch_two
    # push 0 (char index) onto stack
    # get character 0 atk
    # push it onto stack
    # push

    # TESTS
    # ch_one attack ch_two
    # ch_two attack ch_one
    # ch_one debuff ch_two atk
    # ch_two debuff ch_one atk
    # ch_one debuff ch_two def
    # ch_two debuff ch_one def
    # ch_one buff ch_two atk
    # ch_two buff ch_one atk
    # ch_one buff ch_two def
    # ch_two buff ch_one def
    # ch_one buff own atk
    # ch_two buff own atk
    # ch_one buff own def
    # ch_two buff own def
    # ch_one heal ch_two
    # ch_two heal ch_one
    # ch_one heal self
    # ch_two heal self

    machine = vm.VM()
    machine.interpret(basic_attack)  # takes the list of stack instructions


if __name__ == "__main__":
    main()
