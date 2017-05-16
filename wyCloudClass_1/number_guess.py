#This is a simple game program
#Programmed by cyGwendoline
# -*- coding: UTF-8 -*-

import random
guesses_made=0
name=raw_input("Hello! What is your name?\n")

number=random.randint(1,20)
print "Well, {0} , I am thinking of a number between 1 and 20.".format(name)

while guesses_made<6:
    guess=int(raw_input("Take a guess!"))
    guesses_made +=1

    if guess<number:
        print "Your guess is too low"
    elif guess>number:
        print "Your guess is too high"
    else:
        break

if guess==number:
    print "good job, {0}! You guessed my number in {1} guesses!".format(name,guesses_made)
else:
    print "Nope, the number I was thinking of was {0}".format(number)
