import character
# import character_state


# "The goal of the State pattern is to encapsulate
# all of the behavior and data for one state in a single class."
def main():
    # create character
    hp = 2
    mario = character.Character(hp)
    # game loop begin
    s = input("give me and input - w s or None")
    while s != "stop":
        mario.handle_input(mario, s)  # call Character class handle_input()
        pass
        # get input - duck, jump, return to standing position


if __name__ == "__main__":
    main()
