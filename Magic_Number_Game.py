# magic number game

import random
game_starter_message = "Guess a number between 1- 100"
game_active = True
while game_active:

    game_random_number = random.randint(1, 10)
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