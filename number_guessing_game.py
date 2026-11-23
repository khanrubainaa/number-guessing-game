
import random


def generate_number():
    return random.randint(1, 100)


def get_guess():
    try:
        guess = int(input("Enter your guess (1-100): "))
        return guess
    except ValueError:
        print("Please enter a valid number!")
        return None


def check_guess(guess, secret_number):
    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    else:
        return True

    return False


def play_game():
    secret_number = generate_number()
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I have picked a number between 1 and 100.")

    while True:
        guess = get_guess()

        if guess is None:
            continue

        attempts += 1

        if check_guess(guess, secret_number):
            print(f"Correct! You guessed it in {attempts} attempts.")
            break


play_game()
