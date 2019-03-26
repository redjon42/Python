"""
Human, a number between 1 and 20.  Got it?  Type yes if so:  yes!
Is it 10?  type  Y for yes,  H for too high, L for too low.  H
Is it 5?   type Y for yes, H for too high, L for too low.  H
is it 2?   type Y for yes, H for too high, L for too low.  Y
I am smart.
"""
import random


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
    while x not in ["Y", "H", "L"]:
        x = input("I'm sorry, I don't understand, type Y for yes, H for high, and L for low: ")
    if x == "Y":
        out = "GOOD"
    elif x == "H":
        out = [low, guess-1]
    elif x == "L":
        out = [guess+1, high]

    return out


def next_step(guess_range):
    """
    :param guess_range: a list of integers at the current guess range
    :return: the next step
    """
    in_par = high_or_low(guess_range)
    if in_par == "GOOD":
        out = "Eureka!, I got it!"
    else:
        new_range = in_par
        out = new_range
    return out


def run_game():
    print("Think of a number between 1 and 20")

    first_step = [1, 20]
    current_step = next_step(first_step)
    while current_step != "Eureka!, I got it!":
            current_step = next_step(current_step)
    print(current_step)


run_game()
