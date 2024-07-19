#Guess my number game

#The computer picks a random number between 1 and 100
#The player tries to guess it and the computer lets
#the player know if the guess is too high, too low
#or right on the money
#the player will have a limited number of guesses

#to do: add in a method for the computer to play as well

#imports
import random

#output to explain game to player
print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it within a certain number of guesses.\n")


#setting initial values
the_number = random.randint(1, 100)
limit = int(input("How many tries would you like? "))
guess = int(input("Take a guess: "))
tries = 1

#guessing loop
while guess != the_number and tries < limit:
    if guess > the_number:
        print("Lower...")
    else:
        print("Higher...")

    guess = int(input("Take a guess: "))
    tries += 1

if guess == the_number:
    print("You guessed it!  The number was", the_number)
    print("And it only took you", tries, "tries!\n")
else:
    print("Sorry, better luck next time")
    print("The number was", the_number)

input("\n\nPress the enter key to exit.")
