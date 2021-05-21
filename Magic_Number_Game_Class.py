import random


class Magic_Number_Game:

    def __init__(self, name, guess_total, correct_guesses, game_active):
        self.game_active = True
        self.correct_guesses = correct_guesses
        self.guess_total = guess_total
        self.name = name

    def game_start(self):
        self.name = input('What is your name?  ')
        print(self.name)
        game_starter_message = "Guess a number between 1- 100"
        print(game_starter_message)
        test.game()

    def end_game(self):
        print(f'thank you {self.name}, for playing!')
        print(f'total guesses = {self.guess_total}')
        print(f'total correct guesses = {self.correct_guesses}')

    def continue_game(self):
        program_end = input('Press any key to continue, or type "exit" to leave: ')
        exit_rule = program_end.find("exit")
        if exit_rule > 0:  # checks if the input == "exit"
            self.game_active = False  # ends loop
            print("Exiting...")
            test.end_game()
        else:
    def game(self):

        self.game_active = True
        while self.game_active:
            game_random_number = random.randint(1, 10)
            attempts_remaining = 3
            while attempts_remaining != 0:
                user_guess = int(input("Enter a guess:  "))
                self.guess_total += 1
                if user_guess == game_random_number:
                    print(game_random_number, ".You guessed correctly")
                    print("well done!")
                    self.correct_guesses += 1
                    test.continue_game()
                    # game_active = False
                    break
                elif user_guess > game_random_number:
                    attempts_remaining = attempts_remaining - 1
                    print(f"Your guess was too high, {attempts_remaining},{game_random_number} attempts remaining")
                # elif user_guess < game_random_number:
                #     print(f"Your guess was too low, {attempts_remaining} attempts remaining")
                #     attempts_remaining = attempts_remaining - 1
                else:
                    print(game_random_number, ".Unlucky, try again")
            else:
                test.continue_game()
        else:
            self.game_active = False


test = Magic_Number_Game('', 0, 0, True)
test.game_start()
