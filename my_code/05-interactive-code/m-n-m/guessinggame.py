import random

print("-------------------------------")
print("      M&M Guessing Game        ")
print("-------------------------------")

print("Guess the number of M&Ms and you get lunch on the house!")
print()

mm_count = random.randint(1, 100)
attempt_limit = 5
attempts = 0

while attempts < attempt_limit:
    guess = int(input("How many M&Ms are in the jar? ")) #increment attempts +1
    attempts += 1

    if mm_count == guess:
        print(f"You've won! The number was {mm_count}. Lunch is on us!")
        break
    elif guess < mm_count:
        print("Sorry, that's too LOW.")
    else:
        print("That's too HIGH.")

# guess != mm_count AND attempts < attempt limit continue if guess = then print("You've won!")

print(f"I can't believe you got it in {attempts} attempts")