from mimetypes import init


class Stack:
    def __init__(self) -> None:
        self.data = []
    # add 1 value to top of stack

    def push(self, value):
        self.data.append(value)

    # remove top value from 'stack' and return it
    def pop(self):
        val = self.data[len(self.data)-1]
        self.data.remove(len(self.data)-1)
        return val
