# import command
import actor
import input_handler
# this folder contains my attempt/notes at implementing the command design pattern in
# chapter 2 of https://gameprogrammingpatterns.com/contents.html
# comments will be braindead obvious, but are for note taking purposes


# main function to be used with this experiment/notes
def main():
    character = actor.PlayableCharacter()
    enemy = actor.AICharacter()

    # pretend this is used in a loop that gets inputs from a controller or keyboard
    game_input = input_handler.InputHandler()

    # this will be used as a cringe controller for the game
    s = "start"
    # game loop
    while(s != ""):
        s = input("input key command ")
        # pass 'controller command' to input handler
        # take user input for move or jump
        game_input.handleInput(s, character)
        game_input.handleInput("w", enemy)  # 'ai' input for move
        # debug
        character.identify()
        enemy.identify()


if __name__ == "__main__":
    main()
