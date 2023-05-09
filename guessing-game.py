from random import randint

Guess_number = int(input("Enter the number between 1 to 10: "))

random_number = randint (1,10)

if Guess_number == random_number:
    print("You have won")
else:
    print("You have lost")
    print("Random number was = ",random_number)
