# This is a guess the number game.
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break  # This condition is the correct guess!
if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))

# Running result:
# I am thinking of a number between 1 and 20.
# Take a guess.
# 2
# Your guess is too low.
# Take a guess.
# 3
# Your guess is too low.
# Take a guess.
# 6
# Your guess is too low.
# Take a guess.
# 12
# Your guess is too low.
# Take a guess.
# 16
# Your guess is too high.
# Take a guess.
# 14
# Your guess is too high.
# Nope. The number I was thinking of was 13