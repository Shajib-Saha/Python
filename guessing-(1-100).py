import random

guessing_number = int(input("Enter the number between 1 to 100 : "))

random_number = random.randint(1,100)

if guessing_number == random_number :
    print("You have won")

else :
    print("You have lost")
    print("Random number was : ",random_number)