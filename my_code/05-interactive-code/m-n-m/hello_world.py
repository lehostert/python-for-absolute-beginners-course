print("Please give me a number and I will tell you if it is even or odd.")
print("")

num = 1

while num != 0:
    num = int(input("What number would you like to pick? "))
    rem = num % 2

    if num == 0:
        break
    elif rem == 0:
        print(f"{num} is EVEN!")
    else:
        print(f"{num} is ODD!")

print("")
print("Thanks for playing. Goodbye.")