import command
# this class will be used once per game loop (once thats a thing that I write)
# and will delegate to the abstracted commands


class InputHandler():
    def __init__(self) -> None:
        MOVE_COMMAND = 'w'
        JUMP_COMMAND = ' '

    # this method delegates
    def handleInput(self, s, actor):
        if s == self.MOVECOMMAND:
            # send move command
            command.MoveCommand.execute(actor)
        elif s == self.JUMP_COMMAND:
            # send jump command
            command.JumpCommand.execute(actor)
