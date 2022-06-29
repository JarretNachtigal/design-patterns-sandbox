import actor

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
# essentially, this class can be used for movement/ commands for all actors, not just a playable character
# by taking in the actor as a parameter
class Command():
    def __init__(self) -> None:
        pass

    # will be overridden
    def command():
        raise NotImplementedError()  # makes sure its overridden

    # will be overridden
    def execute(actor):
        raise NotImplementedError()  # makes sure its overridden


# will make a character jump. for simplicities sake, it will increase an integer
# called jump_counter by 1
class JumpCommand(Command):

    # what is this for?
    def command():
        pass

    # calls the actor specific method
    def execute(actor):
        actor.jump()

# will move a character. for simplicities sake, it will increase an integer
# called position by 1


class MoveCommand(Command):

    # what is this for?
    def command():
        pass

    # calls the actor specific method
    def execute(actor):
        actor.move()
