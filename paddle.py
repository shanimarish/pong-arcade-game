from turtle import Turtle

X_POSITION_RIGHT = 350
X_POSITION_LEFT = -350
Y_POSITION = 0

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.up()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(X_POSITION_RIGHT, Y_POSITION)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
