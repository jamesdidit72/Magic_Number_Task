# Magic number Game!
## Timings
40-60 Minutes
## Summary
This is a sequel to your previous Magic Number Program, Welcome to the MAGIC NUMBER GAME!
This time we'll increase complexity up a notch to use other things such as:
- libraries
- control flow
- conditions
- while loops
Read the user stories.
## Task
The following are the user stories
```
# User story 1 - As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.

# 2 - As a user, I should get feedback if my number is too high or too low so I can adjust my guess.

# 3 - as a user I should only be able to guess 3 times before a new number is generated

# 4 - as a user, I should be able to keep playing until I respond with exit

# 5 - as a user, I should be able to use exit in a sentence and still terminate the program

# extra 6 - as a user, when I terminate the program I should get a message thanking me for playing and the number of times I guesses and number of times I found the number.

# Extra 7 - as a user, I should be asked the highest number that can be used to generate a random number


# self five
```
## Acceptance Criteria
* random number is generate by random library
* all core 5 user stories should be done
* program should **not break** when given strings
* program should use while loop

### User story 1
#### As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.
```python
import random



game_starter_message = "Guess a number between 1- 100"

game_active = True
while game_active:
    game_random_number = random.randint(1, 100)
    user_guess = int(input("Enter a guess:  "))
    if user_guess == game_random_number:
        print(game_random_number, ".You guessed correctly")
        game_active = False
    else:
        print(game_random_number, ".Unlucky, try again")
print("well done!")
```
### User story 2
#### As a user, I should get feedback if my number is too high or too low, so I can adjust my guess.
```python
import random
game_starter_message = "Guess a number between 1- 100"
game_active = True
while game_active:
    game_random_number = random.randint(1, 100)
    user_guess = int(input("Enter a guess:  "))
    if user_guess == game_random_number:
        print(game_random_number, ".You guessed correctly")
        game_active = False
    elif user_guess > game_random_number:     
        print("Your guess was too high")
    elif user_guess < game_random_number:
        print("Your guess was too low")
    else:
        print(game_random_number, ".Unlucky, try again")
print("well done!")
        
```
### User story 3
#### as a user I should only be able to guess 3 times before a new number is generated
```python
# magic number game
import random
game_starter_message = "Guess a number between 1- 100"
game_active = True
while game_active:
    game_random_number = random.randint(1, 100)
    attempts_remaining = 3
    while attempts_remaining != 0:
        user_guess = int(input("Enter a guess:  "))
        if user_guess == game_random_number:
            print(game_random_number, ".You guessed correctly")
            game_active = False
        elif user_guess > game_random_number:
            attempts_remaining = attempts_remaining - 1
            print(f"Your guess was too high, {attempts_remaining} attempts remaining")
        elif user_guess < game_random_number:
            print(f"Your guess was too low, {attempts_remaining} attempts remaining")
            attempts_remaining = attempts_remaining - 1
        else:
            print(game_random_number, ".Unlucky, try again")
    else:
        print("Wrong, try again")
else:
    print("well done!")
```
### User story 4
#### as a user, I should be able to keep playing until I respond with exit
```python
# magic number game

import random

game_starter_message = "Guess a number between 1- 100"
game_active = True
while game_active:

    game_random_number = random.randint(1, 100)
    attempts_remaining = 3
    while attempts_remaining != 0:
        user_guess = int(input("Enter a guess:  "))
        if user_guess == game_random_number:
            print(game_random_number, ".You guessed correctly")
            print("well done!")
            game_active = False
        elif user_guess > game_random_number:
            attempts_remaining = attempts_remaining - 1
            print(f"Your guess was too high, {attempts_remaining} attempts remaining")
        elif user_guess < game_random_number:
            print(f"Your guess was too low, {attempts_remaining} attempts remaining")
            attempts_remaining = attempts_remaining - 1
        else:
            print(game_random_number, ".Unlucky, try again")
    else:
        program_end = input('Press any key to continue, or type "exit" to leave: ')
        if program_end.upper() == "EXIT":  # checks if the input == "exit"
            game_active = False  # ends loop
            print("Exiting...")
        else:
            continue

else:
    game_active = False

```
### User story 5
#### as a user, I should be able to use exit in a sentence and still terminate the program
```python
# magic number game

import random

game_starter_message = "Guess a number between 1- 100"
game_active = True
while game_active:

    game_random_number = random.randint(1, 100)
    attempts_remaining = 3
    while attempts_remaining != 0:
        user_guess = int(input("Enter a guess:  "))
        if user_guess == game_random_number:
            print(game_random_number, ".You guessed correctly")
            print("well done!")
            game_active = False
        elif user_guess > game_random_number:
            attempts_remaining = attempts_remaining - 1
            print(f"Your guess was too high, {attempts_remaining} attempts remaining")
        elif user_guess < game_random_number:
            print(f"Your guess was too low, {attempts_remaining} attempts remaining")
            attempts_remaining = attempts_remaining - 1
        else:
            print(game_random_number, ".Unlucky, try again")
    else:
        program_end = input('Press any key to continue, or type "exit" to leave: ')
        exit_rule = program_end.find("exit")
        if exit_rule > 0:  # checks if the input == "exit"
            game_active = False  # ends loop
            print("Exiting...")
        else:
            continue

else:
    game_active = False

```