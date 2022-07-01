class SharedResource:
    def __init__(self, color, texture) -> None:
        self.color = color
        self.texture = texture

    def get_color(self):
        return self.color

    def get_texture(self):
        return self.texture
