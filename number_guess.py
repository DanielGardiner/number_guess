
# going to make a number guessing game

#x = input("Please guess a number:")
x = 799

import random

random_number = random.randint(10, 10000)

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
        
    x = input("Please guess a number:") 

        

print(message1 + message2)

