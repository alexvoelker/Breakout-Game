from level_data import levels, total_levels
from turtle import Screen
from ball import Ball
from paddle import Paddle
from time import sleep


class GameStage(Screen):
    def __init__(self, level_start: int = 1, lives=2):
        super().__init__()
        self.setup(width=500, height=750)
        self.bgcolor("black")
        self.title("Breakout")
        self.tracer(0)

        self.move_on = True
        self.game_is_on = True
        self.lives = lives

        self.level_start = level_start
        self.current_level = self.level_start

        self.bricks = []
        # self.ball = Ball()
        self.paddle = Paddle()

        self.listen()
        self.onkeypress(self.paddle.move_left, "Left")
        self.onkeypress(self.paddle.move_right, "Right")
        self.onkeypress(self.paddle.move_left, "a")
        self.onkeypress(self.paddle.move_right, "d")

    def play(self):
        self.create_current_level_on_board()
        self.start_ball_movement()

    def start_ball_movement(self):
        # begin the ball's movement from a still position
        pass

    def create_current_level_on_board(self):
        # clear what's currently on the board, and place all bricks corresponding to the current level
        pass

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

        sleep(self.ball.move_speed)
        # self.ball.check_collide_bricks(self.bricks)
        # self.ball.check_collide_walls()
        # self.ball.check_collide_paddle()
        # self.ball.check_collide_floor() # if collided with floor, decrement lives and check for game end
        # self.ball.move()
        # self.check_level_complete()
        self.screen.update()

    def reset(self):
        # go back to the starting level
        # set up the board for that level
        self.current_level = self.level_start
        self.create_current_level_on_board()
        self.start_ball_movement()

    def request_continuation(self):
        # prompt user with a choice to continue or not
        to_continue = False

        if input("Play again? (Y/n) ").upper() in ['YES', 'Y', 'TRUE', 'T']:
            to_continue = True

        if not to_continue:
            # signals the game to end
            self.move_on = False
