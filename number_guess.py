
# going to make a number guessing game

x = int(input("Please guess a number:"))

import random

random_number = random.randint(1, 20)

#random_number = 778

while (x - random_number) != 0:
    if (x - random_number) == 0:
        message1 = "CORRECT!"
    elif (x - random_number) < 0:
        message1 = "HIGHER!"
    else:
        message1 = "LOWER!"

    if abs(x - random_number) == 0:
        message2 = " well done"
    elif abs(x - random_number) <= 10:
        message2 = " but close..."
    elif abs(x - random_number) <= 20:
        message2 = " sort of close..."
    else:
        message2 = " (not even close!)"

    print(message1 + message2)

    x = int(input("Guess another number:"))

print("CORRECT!!")
