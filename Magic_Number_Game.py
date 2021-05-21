# magic number game
import random

#
# def game_start():
#     game_starter_message = "Guess a number between 1- 100"
#     print(game_starter_message)
#
#
# def end_game():
#     print(f'thank you {name} for playing!')
#     print(f'total guesses = {game()}')

# def game():
correct_guesses = 0
guess_total = 0
name = input('What is your name?  ')
game_active = True
while game_active:
    game_random_number = random.randint(1, 10)
    attempts_remaining = 3
    while attempts_remaining != 0:
        user_guess = int(input("Enter a guess:  "))
        guess_total += 1
        if user_guess == game_random_number:
            print(game_random_number, ".You guessed correctly")
            print("well done!")
            # game_active = False
            break
        elif user_guess > game_random_number:
            attempts_remaining = attempts_remaining - 1
            print(f"Your guess was too high, {attempts_remaining}{game_random_number} attempts remaining")
        # elif user_guess < game_random_number:
        #     print(f"Your guess was too low, {attempts_remaining} attempts remaining")
        #     attempts_remaining = attempts_remaining - 1
        else:
            print(game_random_number, ".Unlucky, try again")
    else:
        program_end = input('Press any key to continue, or type "exit" to leave: ')
        exit_rule = program_end.find("exit")
        if exit_rule > 0:  # checks if the input == "exit"
            game_active = False  # ends loop
            print(f'Goodbye {name}!')
            print(f'You guessed a total of {guess_total} times')
            print("Exiting...")
        else:
            continue
else:
    game_active = False



# game_start()
# game()
