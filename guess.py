import random

guesses_made = 0 # Set the number of guesses made to 0

name = raw_input('Hello! What is your name?\n') # Ask for the player name

number = random.randint(1,20) # Genereta a pseudorandom integer between 1 and 20

print 'Well, {0}, I am thinking of a number between 1 and 20.'.format(name)

while guesses_made < 6: # Start the while loop
    try:
        guess = int(raw_input('Take a guess: '))
    except ValueError:
        print "That is not a number."
        continue

     guesses_made+= 1

    if guess < number:
        print 'Your guess is too low.'

    if guess > number:
        print 'Your guess is to high.'

    if guess == number:
        break

if guess == number:
    print 'Good job, {0}! You guessed my number in {1} guesses!'.format(name, guesses_made)
else:
    print 'Nope. The number I was thinking of was {0}'.format(number)
