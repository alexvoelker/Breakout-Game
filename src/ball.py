from turtle import Turtle


class Ball(Turtle):
    def __init__(self, start_x: int = 0, start_y: int = 75):
        super().__init__()
        self.color("gray")
        self.penup()
        self.shape("circle")

        self.move_speed = 0.1
        self.x_move = 10
        self.y_move = 10

        self.st_x = start_x
        self.st_y = start_y
        self.reset_position()

    def set_move_speed(self, new_speed: float):
        self.move_speed = new_speed

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.75

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.75

    def reset_position(self):
        self.goto(self.st_x, self.st_y)
