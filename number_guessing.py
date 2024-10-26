import random

def validateGuess():
    global guess
    validG = False
    while not validG:
        guess = input("What number am I thinking? ")
        try:
            guess = int(guess)
            if (guess < lowerRange or guess > upperRange):
                print("The guess is out of range!")
            else:
                validG = True
        except ValueError:
            print("This is not a valid guess!")

print("Welcome to the number guessing game!")
valid = False
while not valid:
    lowerRange:int = input("Enter a lower range: ")
    upperRange:int = input("Enter a upper range: ")
    try:
        lowerRange = int(lowerRange)
        upperRange = int(upperRange)
        if (lowerRange < 0 or upperRange < 0):
            print("The upper and lower range must be positive values!")
        elif (upperRange <= lowerRange):
            print("Upper range must be greater than lower range!")
        else:
            valid = True
    except ValueError:
        print("The lower or upper range is not a valid integer!")

print()
print("Alright, I'm picking a random number! I'll give you three guesses")
rand_num = random.randint(lowerRange, upperRange)
won = False

for i in range(3):
    validateGuess()
    if (guess == rand_num and i == 0):
        print("Wow! Getting it on the first try is impressive!")
        won = True
        break
    elif (guess == rand_num):
        print("Good job!")
        won = True
        break
    else:
        print("Wrong answer!")

if (won == True):
    print("Thanks for playing! You're a good guesser!")
else:
    print("That was rough! Better luck next time!")
