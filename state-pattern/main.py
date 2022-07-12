import character
# import character_state


# "The goal of the State pattern is to encapsulate
# all of the behavior and data for one state in a single class."
def main():
    # create character
    hp = 2
    mario = character.Character(hp)
    # game loop begin
    s = input("give me and input - w s or None - stop to stop")
    while s != "stop":
        mario.handle_input(s)  # call Character class handle_input()
        mario.update()  # call Character class update()
        # get input - duck, jump, return to standing position
        s = input("give me and input - w s or None - stop to stop")


if __name__ == "__main__":
    main()
