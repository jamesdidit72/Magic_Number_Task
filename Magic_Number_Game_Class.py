import random


class Magic_Number_Game:

    def __init__(self, name, guess_total, correct_guesses, game_active, range_max):
        self.range_max = range_max
        self.game_active = True
        self.correct_guesses = correct_guesses
        self.guess_total = guess_total
        self.name = name

    def game_start(self):
        self.name = input('What is your name?  ')
        print(self.name)
        self.range_max = int(input('What is the biggest number you would like to guess?  '))
        game_starter_message = f"Guess a number between 1 - {self.range_max}"
        print(game_starter_message)
        magic_game.game()

    def game_end(self):
        print(f'thank you {self.name}, for playing!')
        print(f'total guesses = {self.guess_total}')
        print(f'total correct guesses = {self.correct_guesses}')

    def game_continue(self):
        program_end = input('Press any key to continue, or type "exit" to leave: ')
        exit_rule = program_end.find("exit")
        if exit_rule > 0:  # checks if the input == "exit"
            self.game_active = False  # ends loop
            print("Exiting...")
            magic_game.game_end()
        else:
            magic_game.game()

    def game(self):

        self.game_active = True
        while self.game_active:
            game_random_number = random.randint(1, self.range_max)
            attempts_remaining = 3
            while attempts_remaining != 0:
                user_guess = int(input("Enter a guess:  "))
                self.guess_total += 1
                if user_guess == game_random_number:
                    print(game_random_number, ".You guessed correctly")
                    print("well done!")
                    self.correct_guesses += 1
                    magic_game.game_continue()
                    break
                elif user_guess > game_random_number:
                    attempts_remaining = attempts_remaining - 1
                    print(f"Your guess was too high, {attempts_remaining},{game_random_number} attempts remaining")
                elif user_guess < game_random_number:
                    print(f"Your guess was too low, {attempts_remaining} attempts remaining")
                    attempts_remaining = attempts_remaining - 1
                else:
                    print(game_random_number, ".Unlucky, try again")
            else:
                magic_game.game_continue()
        else:
            self.game_active = False


magic_game = Magic_Number_Game('', 0, 0, True, 0)
magic_game.game_start()
