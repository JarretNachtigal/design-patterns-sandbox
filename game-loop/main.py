# this file will hold the main method for the game loop pattern
# essentially it is a while loop that calls the update method(s)
# for each tic of in game time
# in prebuild engines like unity, this is already implemented and needs to
# be worked with correctly


def main():
    # this needs to run (asynchoronously???)
    # - update and render should not wait for process input / game time should not wait for a user to input
    # while loop:

    # get current time

    # process_input()
    # update() # state pattern?
    # render() # double buffer?

    # sleep for needed amount of time to keep frame rate where
    # it needs it - depends on how long the loop takes to run compared to time at beginning
    pass


if __name__ == "__main__":
    main()
