#Filename: Guess_The_Number_Game.py
#Author: Tan Di Sheng
#Created: 20130116
#Modified: 20130116
#Description: This game allows the user to guess and random integer between 1
#and 100.

import random
number = round(random.randrange (1,100))
print ("""Welcome to the Number Game, you have to guess the correct number
with the hints given at each incorrect guess! The number is between
1 and 100. You have 10 tries. Have fun :)\n""")
    
var = input("Enter your name: ")
print ("\nYour name is", var + "\n")
guessTaken = 10
guessesTaken = 0

while (guessTaken > 0):
    guessTaken = guessTaken - 1
    guessesTaken = guessesTaken + 1
    Guess = int(False)
    Guess = input(var + " please input an integer \n")
    if Guess.isdigit()== False or int(Guess) > 100 or int(Guess) < 0:
        print("Please input an integer between 1 and 100.\nYou have "
              + str(guessTaken) + " tries left")
        continue
    Guess = int(Guess)
    if(Guess > number):
        print("Please guess lower ~\nYou have " + str(guessTaken)+
              " tries left")
    elif(Guess < number):
        print("Please guess higher ~\nYou have " + str(guessTaken)+
              " tries left")
    else:
        break
if Guess != number:
    number = str(number)
    print ("Too bad..... you've exceeded ten tries. The number was "
           + number + ". ): Better luck next time!")
else:
    number = str(number)
    print("Congratulations! You've guessed the number " + number +
          " correctly in " + str(guessesTaken) + " tries!")
