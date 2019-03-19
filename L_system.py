

def apply_rules(left_char):
    """ apply rule transforming leftChar to rightStr
    Axiom: F
    F    ->    F - F + +F - F"""
    if left_char == 'F':
        right_str = "F-F++F-F"
    else:
        right_str = left_char

    return right_str


def process_string(old_str):
    """ given a string oldStr transform it into newStr with rules """
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


def build_rules(file_name):
    """
    :param file_name: a string that is the name of the rule string file
    :return: an axiom
    """
    f = open(file_name, "r")
    rule_list = f.readlines()
    f.close()
    for i in range(len(rule_list)):
        line = rule_list[i]
        rule_list[i] = line.strip().split("-->")
        for j in range(len(rule_list[i])):
            rule_list[i][j] = rule_list[i][j].strip()
    return rule_list


def test_build_rules(file_name="rules.txt"):
    print(build_rules(file_name))


def apply_rule_set(rule_set, left_char):
    """
    Write function applyRuleSet that takes a list of transformations, a rule set, and a left character,
    and returns a right character.  Dude.  That's challenging!
    :param rule_set: a list of l-system rules
    :param left_char: the name of a rule
    :return: the correct corresponding right character
    """
    for rule in rule_set:
        if rule[0] == left_char:
            out = rule[1]
    return out


def test_apply_rule_set():
    test = apply_rule_set(build_rules("rules.txt"), 'B')
    print(test)


test_apply_rule_set()

