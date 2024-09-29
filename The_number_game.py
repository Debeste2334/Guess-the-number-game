import random
import time
import os

os.system('cls' if os.name == 'nt' else 'clear')

print("Debeste2334 productions")
time.sleep(1)
print("Introduces...")
time.sleep(1)
print("The number game")
print("V.: 1.2.0")
time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')
print(os.name)
print("Loading...")

os.system('cls' if os.name == 'nt' else 'clear')
def min_range():
    while True:
        try:
            min = int(input(f"Please enter a minimum number: "))
            if min < 1:
                print("Cannot go lower than 1")
            else:
                return(min)
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Please enter a number")

def max_range():
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(0.1)
    while True:
        try:
            max = int(input(f"Please enter a maximum number: "))
            if max > 1000:
                print("Cannot go higher than 1.000")
            else:
                return(max)
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Please enter a number")

min = min_range()
max = max_range()

Answer = random.randint(int(min), int(max))
Correct = False
guesses = 0

os.system('cls' if os.name == 'nt' else 'clear')

while True:
    time.sleep(0.1)
    
    if Correct:
        min = min_range()
        max = max_range()
        guesses = 0
        Answer = random.randint(int(min), int(max))
        Correct = False
    else:
        pass

    while True:
        try:
            guess = int(input(f"Guess a number between {min} and {max}: "))
            os.system('cls' if os.name == 'nt' else 'clear')
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Please enter a number")

        if guess == "exit()":
            break

        if guess < Answer:
            print("Too low!")
            print(f"Last guess: {guess}")
        elif guess > Answer:
            print("Too high!")
            print(f"Last guess: {guess}")
        elif guess > max:
            print(f"Higher than maximum. Maximum: {max}")
            print(f"Last guess: {guess}")
        elif guess < min:
            print(f"Lower than minimum. Minimum: {min}")
            print(f"Last guess: {guess}")
        else:
            print("You got it right!")
            print(f"The number was: {Answer}")
            input("Press enter to play again!")
            Correct = True
            os.system('cls' if os.name == 'nt' else 'clear')
