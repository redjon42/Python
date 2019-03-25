"""
Human, a number between 1 and 20.  Got it?  Type yes if so:  yes!
Is it 10?  type  Y for yes,  H for too high, L for too low.  H
Is it 5?   type Y for yes, H for too high, L for too low.  H
is it 2?   type Y for yes, H for too high, L for too low.  Y
I am smart.
"""
import random


def get_number():
    x = input("Give me a number between 1 and 20: ")
    x = int(x)
    return x


def make_guess(guess_range=[1, 20]):
    """
    :param guess_range: a list of integers at the current guess range
    :return: a new guess
    """
    low = guess_range[0]
    high = guess_range[1]
    x = random.randint(low, high)
    return x


def high_or_low(guess_range):
    """
    :param guess_range: a list of integers at the current guess range
    :return: the new low and high
    """
    guess = make_guess(guess_range)
    x = input("Is it {}?, type Y for yes, H for high, and L for low: ".format(guess))
    low = guess_range[0]
    high = guess_range[1]
    if x == "Y":
        out = "GOOD"
    elif x == "H":
        out = [low, guess-1]
    elif x == "L":
        out = [guess+1, high]
    else:
        out = "BAD"

    return out


def next_step(guess_range):
    """
    :param guess_range: a list of integers at the current guess range
    :return: the next step
    """
    in_par = high_or_low(guess_range)
    if in_par == "GOOD":
        out = "Eureka!, I got it!"
    elif in_par == "BAD":
        out = "I'm sorry, I don't understand."
    else:
        new_range = in_par
        out = new_range
    return out


def run_game():
    x = get_number()
    print("You're number is {}".format(x))

    first_step = [1, 20]
    current_step = next_step(first_step)
    while current_step != "Eureka!, I got it!":
        if current_step == "I'm sorry, I don't understand.":
            print(current_step, "Let's Start Over!")
            current_step = next_step(first_step)
        else:
            current_step = next_step(current_step)
    print(current_step)


run_game()
