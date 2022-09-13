# importing the random module
import random

# generating a random number using .randint and 
# looks like: random.randint(start,stop+1)
number = random.randint(1, 10)

# asking the user to enter their name 
# and then assinging that to player name
player_name = input("Hello, what's your name?")

# number of guesses - going to loop over
number_of_guesses = 0 

# printing the reply to the user
print('Hello, '+ player_name+ '! I am thinking of a number between 1 and 10... make your guess as a whole number (e.g. 1) not a word (e.g. one) and do not use any punctuation!')

# designing a "while loop" - 
# while the number of guesses is less than five, perform the following
while number_of_guesses < 5:
    # converting the user input into an integer called guess
    guess = int(input())
    # confirming that the user has used one guess
    number_of_guesses += 1
    
    if guess < number:
        print('Too low!')
    if guess > number:
        print('Too high!')
    if guess == number:
        # terminates the loop
        break
# responding to guesses
if guess == number:
    print('Nice one! You guessed the number in ' + str(number_of_guesses) + ' tries!')
else:
    print('You did not guess in time! The number was ' + str(number))

    
    
    