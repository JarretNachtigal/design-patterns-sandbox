from mimetypes import init


class Stack:
    def __init__(self) -> None:
        self.data = []
    # add 1 value to top of stack

    def push(self, value):
        self.data.append(value)
