from art import logo
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def check_answer(guess, answer, turns):
    """Checks answer against the guess.

    Args:
        guess (int): user guess
        answer (int): number picked by computer
        turns (int): number of turns user has

    Returns:
        int: returns the turns remaining
    """
    if guess > answer:
        print("Too high.\nGuess again.")
        return turns - 1
    elif guess < answer:
        print("Too low.\nGuess again.")
        return turns - 1
    else:
        print(f"You got it. The answer was {original}")


def game():
    print(logo)
    print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)

    guess = int(input("Make a guess: "))
    turns = set_difficulty()

    guess = 0

    while guess != answer:
        print(
            f"You have {check_answer(guess, answer, turns)} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        check_answer(guess, answer, turns)


game()
