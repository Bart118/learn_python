#Fortune Cookie

#program that simulates a fortune cookie

#imports
import random

#set initial values
fortune = 0  #initial value for fortune

#generate a random number to determine which fortune to give
fortune = random.randint(1, 5)  #returns int from 1-5, inclusive

#Greet the player
print("Hello, please take a fortune cookie!")

#branch to fortune based on random number
if fortune == 1:
    print("fortune 1")
elif fortune == 2:
    print("fortune 2")
elif fortune == 3:
    print("fortune 3")
elif fortune == 4:
    print("fortune 4")
elif fortune == 5:
    print("fortune 5")
else:
    print("Sorry we are out of fortunes, please try again later.")
    
#End the Program
print("Thank you for visiting, please come again!")
input("\n\nPress the enter key to exit.")
