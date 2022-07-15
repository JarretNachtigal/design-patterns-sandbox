# this file will hold the main method for the game loop pattern
# essentially it is a while loop that calls the update method(s)
# for each tic of in game time
# in prebuild engines like unity, this is already implemented and needs to
# be worked with correctly


def main():
    # this needs to run (asynchoronously???)
    # - update and render should not wait for process input / game time should not wait for a user to input

    # save current and last time of loop iteration
    current_time = 0
    last_time = 0

    # while loop:

    # get current time
    current_time += 1  # this should call a method to get current time
    # get time between last and current loop iteration
    time_elapsed = current_time - last_time

    # process_input()

    update(time_elapsed)  # state pattern?
    render()  # double buffer?

    # sleep for needed amount of time to keep frame rate where
    # it needs it - depends on how long the loop takes to run compared to time at beginning
    last_time = current_time
    pass


# update the game state based on time elapsed since last call
def update(time_elapsed):
    pass


def render():
    pass


def process_input():
    pass


if __name__ == "__main__":
    main()
