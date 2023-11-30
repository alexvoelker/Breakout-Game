from turtle import Turtle

colors = {
    0: 'purple',
    1: 'red',
    2: 'orange',
    3: 'yellow',
    4: 'green'
}


class Brick(Turtle):  # the brick template for each

    def __init__(self, hits_left: int):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.hits_left = hits_left
        self.color(colors[self.hits_left])


    def hit_brick(self) -> bool:
        # returns if the brick should continue to exist
        if self.hits_left - 1 < 1:
            self.color(colors[0])
            return False

        self.hits_left -= 1
        self.color(colors[self.hits_left])
        return True


