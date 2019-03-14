"""
Write a function called goTurtleStep that takes two parameters:
a turtle - some turtle - any turtle!
a command character - any command character.
And
makes the turtle execute the command character
if the command character isn't implemented, then don't do anything.
The function need not return anything.

"""
import turtle


def go_turtle_step(turtle_name, command, distance=50, angle=90):
    """
    :param command: A single character
    :param turtle_name: the name of a turtle instance
    :param distance: integer representing the desired distance of movement
    :param angle: integer representing the desired distance of rotation
    :return:
    """

    if command == 'f':
        turtle_name.forward(distance)
    elif command == 'b':
        turtle_name.backward(distance)
    elif command == '+':
        turtle_name.right(angle)
    elif command == '-':
        turtle_name.right(angle)


def clear_and_reset_turtle(turtle_name):
    turtle_name.clear()
    turtle_name.reset()


def go_turtle_step_test(test_str):
    test_turtle = turtle.Turtle()
    test_turtle.speed(1)
    go_turtle_step(test_turtle, test_str)
    clear_and_reset_turtle(test_turtle)


""" go_turtle_step_test routine"""
wn = turtle.Screen()
wn.listen()
command_list = ['f', 'b', '+', '-']
for command in command_list:
    go_turtle_step_test(command)


