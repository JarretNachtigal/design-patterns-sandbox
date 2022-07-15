# this file will hold the main method for the game loop pattern
# essentially it is a while loop that calls the update method(s)
# for each tic of in game time
# in prebuild engines like unity, this is already implemented and needs to
# be worked with correctly
# "variable / fluid time step" - does not account for multiplayer with 2 different machine specs

def main():
    # this needs to run (asynchoronously???)
    # - update and render should not wait for process input / game time should not wait for a user to input

    # save current and last time of loop iteration
    current_time = 0
    last_time = 0

    # while(true) loop:

    current_time += 1  # this should call a method to get current time
    # get time between last and current loop iteration
    time_elapsed = current_time - last_time

    process_input()
    update(time_elapsed)  # state pattern?
    render()  # double buffer?

    # sleep for needed amount of time to keep frame rate where
    # it needs it - depends on how long the loop takes to run compared to time at beginning
    last_time = current_time


# this version has a fixed time step - decouple render and update timing
# the rendering and input processing happen every tic, the game state update does not
# used to sync game time with real time between different machines in a multiplayer game
def main_loop_two():
    MS_PER_UPDATE = 10

    # this needs to run (asynchoronously???)
    # - update and render should not wait for process input / game time should not wait for a user to input

    # save current and last time of loop iteration
    current_time = 0
    lag = 0.0  # used for fixed time step
    last_time = 0

    # while(true) loop:

    current_time += 1  # this should call a method to get current time
    # get time between last and current loop iteration
    time_elapsed = current_time - last_time
    last_time = current_time
    lag += time_elapsed  # sync ingame and real world time

    process_input()  # every tic

    # fixed step
    # while(lag >= MS_PER_UPDATE)
    # update(time_elapsed)  # state pattern?
    # end loop

    # double buffer? - params used to keep time consistant between update calls
    render(lag / MS_PER_UPDATE)


# update the game state based on time elapsed since last call
def update(time_elapsed):
    pass


def render():
    pass


def process_input():
    pass


if __name__ == "__main__":
    main()


# the 4 examples from the reading

# Fixed time step with no synchronization:
# - loop, process, update, render, no sleep()
# Fixed time step with synchronization:
# - same as before with sleep(start + MS_PER_FRAME - getCurrentTime())
# Variable time step: - main()
# Fixed update time step, variable rendering: - main_loop_two()
# - render can probably also be fixed in the same way to implement locked FPS
# 60 FPS - 16.6 repeating MS_PER_UPDATE
