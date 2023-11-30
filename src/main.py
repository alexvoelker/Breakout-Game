from gamestage import GameStage

LEVEL = 0
LIVES = 3

game = GameStage(level_start=LEVEL, lives=LIVES) # additional optional argument: refresh_rate

while game.move_on:
    game.reset()

    game.play()

    while game.game_is_on:
        # refresh the screen while the game is running
        game.update_board()

    game.request_continuation()
    # if the user wants to continue to play, reset the game (i.e. game.move_on is True)

game.exitonclick()
print("GAME ENDED")
