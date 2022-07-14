import frame_buffer
# holds both FrameBuffers and draw method


class Screen:
    def __init__(self):
        self.current_buffer = frame_buffer.FrameBuffer()
        self.next_buffer = frame_buffer.FrameBuffer()

    # this method would be used to draw all pixels into the next frame
    def draw_to_next(self, data):
        self.next_buffer.draw(data)

    def draw_to_screen(self):
        # get data from current, buffer
        print(self.current_buffer.get_buffer())

    # swap current and next, clear next
    def swap(self):
        # swap
        self.current_buffer, self.next_buffer = self.next_buffer, self.current_buffer
        # clear next
        self.next_buffer.clear()

    # this method tests
    def test_actions(self):
        # draw current buffer
        self.draw_to_screen()  # => "this is data"
        # fill next buffer
        self.draw_to_next("first swap data")
        # swap
        self.swap()
        # draw current buffer
        self.draw_to_screen()  # => "first swap data"
        # fill next buffer
        self.draw_to_next("first swap data")
        # swap
        self.swap()
