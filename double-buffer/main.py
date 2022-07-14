# this file contains the main method for the double buffer pattern
import frame_buffer
import screen


def main():
    buffer = frame_buffer.FrameBuffer()
    print(buffer.get_buffer())
    pass


if __name__ == "__main__":
    main()


# https://gameprogrammingpatterns.com/double-buffer.html
# "A buffered class encapsulates a buffer: a piece of state that can be modified.
# This buffer is edited incrementally, but we want all outside code to see the edit
# as a single atomic change. To do this, the class keeps two instances of the buffer:
# a next buffer and a current buffer."

# "More specifically, this pattern is appropriate when all of these are true:
# - We have some state that is being modified incrementally.
# - That same state may be accessed in the middle of modification.
# - We want to prevent the code that’s accessing the state from seeing the work in progress.
# - We want to be able to read the state and we don’t want to have to wait while it’s being written."

# "no code can access either state while they are being swapped."

# more memory intensive, as there must be 2 copies of the state
