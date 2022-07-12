import character


# "The goal of the State pattern is to encapsulate
# all of the behavior and data for one state in a single class."
# this implementation uses static states
# there is another way of implementing the CharacterStates (instantiated states)
# in which a new object is created at runtime. this is needed when the variables inside that
# object are reset on each press ex: charge attack timer
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
