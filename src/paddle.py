from turtle import Turtle

class Paddle(Turtle): # paddle for the player to use to bounce balls across the screen
    def __init__(self, start_x: int = 0, start_y: int = 75, move_speed: int=10):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()

        self.move_speed = move_speed # the number of pixels moved at once

        self.st_x = start_x
        self.st_y = start_y
        self.reset_position()

    def set_move_speed(self, new_speed: int):
        self.move_speed = new_speed

    def move_left(self):
        if self.xcor() - self.move_speed > -230:
            new_x = self.xcor() - self.move_speed
            self.goto(new_x, self.ycor())

    def move_right(self):
        if self.xcor() + self.move_speed < 230:
            new_x = self.xcor() + self.move_speed
            self.goto(new_x, self.ycor())

    def reset_position(self):
        self.goto(self.st_x, self.st_y)