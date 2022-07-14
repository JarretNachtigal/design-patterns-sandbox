import frame_buffer
# holds both FrameBuffers and draw method


class Screen:
    def __init__(self):
        self.current_buffer = frame_buffer.FrameBuffer()
        self.next_buffer = frame_buffer.FrameBuffer()

    # this method would be used to draw all pixels into the next frame
    def draw(self, data):
        self.next_buffer.draw(data)
        self.swap()

    # swap current and next, clear next
    def swap(self):
        # swap
        self.current_buffer, self.next_buffer = self.next_buffer, self.current_buffer
        # clear next
        self.next_buffer.clear()

    # this method tests
    def test_actions(self):
        self.next_buffer.draw("this was the next buffer")  # setup next buffer
        self.draw()  # initial current buffer state
