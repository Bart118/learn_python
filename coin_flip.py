#Coin Flip

#flips a coin 100 times and counts the number of heads and tails

#imports
import random

#initial values
heads = 0  #counts number of heads
tails = 0  #counts number of tails
count = 0  #counts number of flips
flip = 0  #takes a random int to decide if we flipped heads or tails
guess = " "  #player guess on if there will be more heads or tails

#greeting and taking guess
guess = input("Will there be more heads or tails?")

#flipping the coin
while count < 100:
    flip = random.randint(1,2)
    count += 1
    if flip == 1:
        heads += 1
    elif flip == 2:
        tails += 1

#print results
print("After", count, "flips, the total is:")
print("heads:", heads, "tails:", tails)
if heads > tails:
    print("There were more heads")
    if guess == "heads":
        print("Congrats, you were right!")
    else:
        print("Sorry, better luck next time")
elif heads < tails:
    print("There were more tails")
    if guess == "heads":
        print("Sorry, better luck next time")
    else:
        print("Congrats, you were right!")
else:
    print("No winner this time!")

#end program
input("\n\nPress the enter key to exit.")
