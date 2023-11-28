import turtle
from level_data import levels, total_levels


class Stage():
    def __init__(self, level_start: int = 1, refresh_rate: int = 0, lives=2):
        self.game_is_on = True
        self.move_on = True

        self.level_start = level_start
        self.current_level = self.level_start
        self.refresh_rate = refresh_rate
        self.lives = lives

        # create the turtle stage
        self.background_color = 'black'

    def create_current_level_on_board(self):
        # clear what's currently on the board, and place all bricks corresponding to the current level
        pass

    def reset(self):
        # go back to the starting level
        # set up the board for that level
        self.current_level = self.level_start
        self.create_current_level_on_board()
        self.start_ball_movement()

    def update_board(self):
        # move the paddle's position
        # move the ball's position
        # check for ball collisions with bricks, the paddle, the walls, ceiling, or ground
        # update/delete brick if collided
        # change ball's direction if it hit the ceiling or walls
        # kill the ball if it hit the ground, subtract a life.
        # if lives reach 0, game ends
        # if all bricks are destroyed, move the paddle and ball to the starting position and move to the next level
        # if moving to next level,
        #   increment current_level,
        #   call create_current_level_on_board,
        #   then call start_ball_movement
        # the player wins when they complete the final level (self.current_level > total_levels).
        pass

    def start_ball_movement(self):
        # begin the ball's movement from a still position
        pass

    def get_refresh_time(self):
        return 0 if self.refresh_rate == 0 else 1 / self.refresh_rate

    def request_continuation(self):
        # prompt user with a choice to continue or not
        to_continue = False

        if input("Play again? (Y/n) ").upper() in ['YES', 'Y', 'TRUE', 'T']:
            to_continue = True

        if not to_continue:
            # signals the game to end
            self.move_on = False
