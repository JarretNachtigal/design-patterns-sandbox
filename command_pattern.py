# this file contains my attempt/notes at implementing the command design pattern in
# chapter 2 of https://gameprogrammingpatterns.com/contents.html
# comments will be braindead obvious, but are for note taking purposes
# --------------------------------------------------------------------------------
# NOTES
#
# "A command is a reified method call."
#
# "Both terms mean taking some concept and turning it into a piece of data
#  — an object — that you can stick in a variable, pass to a function, etc.
# So by saying the Command pattern is a “reified method call”, what I mean is that
# it’s a method call wrapped in an object."

# "represents a triggerable game command"
# parent class for all game commands
class Command():
    def __init__(self) -> None:
        pass

    # will be overridden
    def command():
        pass

    # will be overridden
    def execute():
        pass


# will make a character jump. for simplicities sake, it will increase an integer
# called jump_counter by 1
class JumpCommand(Command):
    def __init__(self) -> None:
        pass
        # will be overridden

    def command():
        pass

    # will be overridden
    def execute():
        pass


# will move a character. for simplicities sake, it will increase an integer
# called position by 1
class MoveCommand(Command):
    def __init__(self) -> None:
        pass

    # will be overridden
    def command():
        pass

    # will be overridden
    def execute():
        pass


# this class will be used once per game loop (once thats a thing that I write)
# and will delegate to the abstracted commands
class InputHandler():
    def __init__(self) -> None:
        pass

    # this method delegates
    def handleInput():
        pass
