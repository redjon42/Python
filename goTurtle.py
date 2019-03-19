"""
Write a function called goTurtleStep that takes two parameters:
a turtle - some turtle - any turtle!
a command character - any command character.
And
makes the turtle execute the command character
if the command character isn't implemented, then don't do anything.
The function need not return anything.

"""
FORWARD_SIZE = 10
ANGLE_SIZE = 60

import turtle


def go_turtle_step(turtle_name, turtle_command, distance=50, angle=90):
    """
    :param turtle_command: A single character
    :param turtle_name: the name of a turtle instance
    :param distance: integer representing the desired distance of movement
    :param angle: integer representing the desired distance of rotation
    :return:
    """

    if turtle_command == 'f':
        turtle_name.forward(distance)
    elif turtle_command == 'b':
        turtle_name.backward(distance)
    elif turtle_command == '+':
        turtle_name.right(angle)
    elif turtle_command == '-':
        turtle_name.right(angle)


def clear_and_reset_turtle(turtle_name):
    turtle_name.clear()
    turtle_name.reset()


def go_turtle_step_test(test_str):
    test_turtle = turtle.Turtle()
    test_turtle.speed(1)
    go_turtle_step(test_turtle, test_str)
    clear_and_reset_turtle(test_turtle)


def go_turtle_go(some_turtle, cmd_string, step_size=FORWARD_SIZE):
    print(f"We are going to run the turtle with this command string: \n  {cmdString} ")

    some_turtle.penup()
    some_turtle.setpos(-200, 0)  # put someT on the screen left.
    some_turtle.setheading(0)
    some_turtle.pendown()
    for cmd in cmd_string:
        go_turtle_step(some_turtle, cmd, step_size)


def colorAngleToRGB(degrees, intensity=1.0):
    """ Take an angle in degrees and convert it to a color combo of red, green, and blue
     This gives us a convenient way to cycle through colors with just one parameter.
     intensity of 1 is on the edge of the circle.  intensity of 0 is in the middle and is black.
     The returned RGB are using red green blue values between 0 and 1.
     """
    redAngle   = math.radians(degrees)
    greenAngle = math.radians(degrees + 120.0)
    blueAngle  = math.radians(degrees + 240.0)
    red   = intensity * (math.sin(redAngle)   + 1) / 2   # convert range -1 .. 1 to range 0..1.
    green = intensity * (math.sin(greenAngle) + 1) / 2   # add one makes it 1 .. 2
    blue  = intensity * (math.sin(blueAngle)  + 1) / 2   # divide by 2 makes 1 ... 2 range into 0..1
    return red,green,blue  #  RGB color model in range 0,1



""" go_turtle_step_test routine"""
wn = turtle.Screen()
wn.listen()
command_list = ['f', 'b', '+', '-']
for command in command_list:
    go_turtle_step_test(command)


