from art import logo, vs
from game_data import data
import random
from replit import clear


def format_data(account):
    """ Format the account data and returns the printable format.
    """
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """Take the user guess and the follwer counts and returns if they got it right.
    """
    if a_followers > b_followers:
        return guess == "A"
    else:
        return guess == "B"


# Display art
print(logo)

score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    # Check if user is correct.
    # Get foller count of each account.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    clear()
    print(logo)

    # Give user feedback on their guess.
    if is_correct:
        score += 1
        print(f"You're right! Current score is {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False

# Make the game repeatable.
# making account at position B become the next account at position A

# Clear the screen between rounds.
