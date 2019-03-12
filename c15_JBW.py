def apply_rules(left_char):
    """ apply rule transforming left_char to right_char """
    if left_char == 'A':
        right_char = 'B'   # Rule 1
    elif left_char == 'B':
        right_char = 'AB'  # Rule 2
    else:
        right_char = left_char    # no rules apply so keep the character
    return right_char


def process_string(old_str):
    """ given a string old_str transform it into newStr with rules """
    new_str = ""
    for ch in old_str:
        new_str = new_str + apply_rules(ch)

    return new_str


def execute_l_system(num_iterations, axiom):
    result_string = axiom
    for i in range(num_iterations):
        new_string = process_string(result_string)
        result_string = new_string

    return result_string


print(execute_l_system(4, "A"))

from heapq import nlargest
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
three_largest = nlargest(3, my_dict, key=my_dict.get)
print(three_largest)

