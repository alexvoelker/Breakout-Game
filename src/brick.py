class Brick(): # the brick template for each

    def __init__(self, hits_left: int):
        colors = {
            1: 'red',
            2: 'orange',
            3: 'yellow',
            4: 'green'
        }

        self.color = colors[hits_left]

    def draw_brick(self):
        # draw this brick
        pass