# M&M Guessing Game
# Same code from Chapter 5 but improved with functions.
import random

def main():
    show_header()
    play_game()

def show_header():
    print("-------------------------------")
    print("      M&M Guessing Game        ")
    print("-------------------------------")

    print("Guess the number of M&Ms and you get lunch on the house!")
    print()

def play_game():
    mm_count = random.randint(1, 100)
    attempt_limit = 5
    attempts = 0
    while attempts < attempt_limit:
        guess = int(input("How many M&Ms are in the jar? ")) #increment attempts +1
        attempts += 1
    if mm_count == guess:
        print(f"You've won! The number was {mm_count}. Lunch is on us!")
        # break
    elif guess < mm_count:
        print("Sorry, that's too LOW.")
    else:
        print("That's too HIGH.")

    print(f"I can't believe you got it in {attempts} attempts")


def get_guess():


if __name__ == "__main__":
    main()