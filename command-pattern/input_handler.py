import command
# this class will be used once per game loop (once thats a thing that I write)
# and will delegate to the abstracted commands


class InputHandler():
    def __init__(self) -> None:
        self.MOVE_COMMAND = 'w'
        self.JUMP_COMMAND = ' '

    # this method delegates
    def handleInput(self, s, actor):
        if s == self.MOVE_COMMAND:
            # send move command
            command.MoveCommand.execute(actor)
        elif s == self.JUMP_COMMAND or 'space':
            # send jump command
            command.JumpCommand.execute(actor)
