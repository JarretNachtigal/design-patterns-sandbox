import command
# this class will be used once per game loop (once thats a thing that I write)
# and will delegate to the abstracted commands


class InputHandler():
    def __init__(self) -> None:
        pass

    # this method delegates
    def handleInput(s, actor):
        if s == "w":
            # send move command
            command.MoveCommand.execute(actor)
        elif s == "space" or " ":
            # send jump command
            command.JumpCommand.execute(actor)
