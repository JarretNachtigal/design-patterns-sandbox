class Rock:
    def __init__(self, shared_resource, position, size_modifier) -> None:
        # color and texture from SharedResouce instance, should all reference the same one
        self.shared_resource = shared_resource
        # instance variables for each rock
        self.position = position
        self.size_modifier = size_modifier

    def get_position(self):
        return self.position

    def get_size_modifier(self):
        return self.size_modifier

    def get_shared_resource(self):
        return self.shared_resource
