import random

name = raw_input("Welcome. Enter your name here: ")
print "Ok, %s, I'm thinking of a number between 1 and 100." % name 
print "Keep entering a guess, I'll give you hints to tell you if your high or low"
answer = random.randint(0,101)
tries = 1
guess = int(raw_input("Guess a number: "))

while tries >= 1:
    if guess > answer:
        print "Your guess is too high, try again."
        guess = int(raw_input("Guess a number: "))
        tries += 1
    elif guess < answer:
        print "Your guess is too low, try again."
        guess = int(raw_input("Guess a number: "))
        tries += 1
    else:
        print "Good job %s! You guessed correctly in %d tries! You win!" % (name,tries)
        break