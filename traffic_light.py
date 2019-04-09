
import turtle
current_state = "GREEN"
screen = turtle.Screen()
screen.exitonclick()


class Light(turtle.Turtle()):

    def __init__(self, c, x=0, y=0):
        super().__init__()
        # self = turtle.Turtle()

        self.color(c)
        self.this_color = c
        self.shape('circle')
        self.fillcolor(c)
        self.this_color = c
        self.penup()
        self.setpos(x, y)

    def turn_off(self):
        self.fillcolor("gray")

    def turn_on(self):
        self.fillcolor(self.this_color)


class Signal:

    def __init__(self, x=0, y=0):

        self.red = Light("red", x+0, y+30)
        self.yellow = Light("yellow", x+0, y+0)
        self.green = Light("green", x+0, y-30)


def set_lights():
    if current_state == "GREEN":
        red.turn_off()
        yellow.turn_off()
        green.turn_on()
    elif current_state == "YELLOW":
        red.turn_off()
        yellow.turn_on()
        green.turn_off()
    else:
        red.turn_on()
        yellow.turn_off()
        green.turn_off()


def change_state():
    global current_state
    if current_state == "GREEN":
        current_state = "YELLOW"
    elif current_state == "YELLOW":
        current_state = "RED"
    else:
        current_state = "GREEN"



screen.ontimer(change_state(), 2000)








