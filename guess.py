import random

name = raw_input("Welcome. Enter your name here: ")
print "Ok, %s, I'm thinking of a number between 1 and 100." % name 
print "Keep entering a guess, I'll give you hints to tell you if your high or low"
guess = int(raw_input("Guess a number: "))
answer = random.randint(0,101)
tries = 0

if guess == answer:
    print "Good job %s! You guessed correctly in %s tries! You win!" (name, tries)

elif guess > answer:
    print "Your guess is too high, try again."

elif guess < answer:
    print "Your guess is too low, try again."

 
