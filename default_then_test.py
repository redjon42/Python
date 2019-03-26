
"""
exec(open("default_then_test.py").read())
"""

"""
The user can type lines over and over again while the line they type is not blank…
See if any of the lines are longer than 20 characters.
"""

"""
AnyLinesLong = False
while _____ :
    line = input("Type a line, blank to stop.")
    if …

if AnyLinesLong :
    print("you typed at least one line that was long!")
else:
    print("All your lines were short")
"""


def get_lines():
    line_list = []
    line = "1 2 3 4 5 6 7 8 9 10 11 12 13"
    while len(line) != 0:
        line = input("Type a line, blank to stop: ")
        line_list.append(line)
    return line_list


def any_lines_long():
    list_of_lines = get_lines()
    for line in list_of_lines:
        if len(line.split()) < 5:
            any_long = False
        else:
            any_long = True
            break
    return any_long


def while_long():
    long = False
    line = "1 2 3 4 5 6 7 8 9 10 11 12 13"
    while len(line) != 0:
        line = input("Type a line, blank to stop: ")
        if len(line.split()) > 5:
            long = True
    return long


print(while_long())

