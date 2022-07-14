# pretends to do frame things
class FrameBuffer:
    def __init__(self):
        self.data = "this is data"

    def clear(self):
        self.data = "cleared"

    def draw(self, data):
        pass
