import random


class Edit_Values:

    def __init__(self, age, lucky_number):
        self.value = str(age)
        self.age = 0
        self.lucky_number = 0

    def get_numbers(self):
        self.age = input('How old are you?  ')
        check_value.check_numbers(self.age)
        self.lucky_number = input('What is your lucky number?  ')
        check_value.check_numbers(self.lucky_number)

    def check_numbers(self, value):
        user_prompt = True
        while user_prompt:
            if self.value.isdigit():
                user_prompt = False
            else:
                print('Please enter a digit')
        print(f'your age is {self.value}')  # f does the same as .format


check_value = Edit_Values(0, 0)

check_value.get_numbers()
