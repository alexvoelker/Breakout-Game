from stage import Stage
import time

# REFRESH_RATE = 20 # number of refreshes per second, defaults to '0' for constant refreshing
LEVEL = 0
LIVES = 3

game = Stage(level_start=LEVEL, lives=LIVES) # additional optional argument: refresh_rate

while game.move_on:
    game.reset()

    while game.game_is_on:
        # refresh the screen while the game is running
        game.update_board()
        time.sleep(game.get_refresh_time())

    game.request_continuation()
    # if the user wants to continue to play, reset the game (i.e. game.move_on is True)

print("GAME ENDED")
