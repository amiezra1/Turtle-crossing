from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE_UP = 10
MOVE_DISTANCE_DOWN = -10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goToStart()
        self.setheading(90)
    
    def goUp(self):
        self.forward(MOVE_DISTANCE_UP)
    
    def goDown(self):
        self.forward(MOVE_DISTANCE_DOWN)

    def goToStart(self):
        self.goto(STARTING_POSITION)

    def isAtFinishLine(self):
        return self.ycor() > FINISH_LINE_Y