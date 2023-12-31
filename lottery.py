from random import choice

MIN_CODE_LENGTH = 2
MAX_CODE_LENGTH = 5

class Lottery:

    def __init__(self, lottery_codes, min_code_length, max_code_length):
        self.lottery_codes = lottery_codes
        self.min_code_length = min_code_length
        self.max_code_length = max_code_length

    def _ask_ticket(self):
        self.user_ticket = input("Enter from 2 to 5 symbols in ONE string of your ticket number (numbers and letters):")

    def _validate_ticket(self):
        if len(self.user_ticket) < self.min_code_length:
            print("Your ticket number less than 3. Try again!")
            self._ask_ticket()

        elif len(self.user_ticket) > self.max_code_length:
            print("Your ticket number more than 5. Try again!")
            self._ask_ticket()

        else:
            print(f"You have entered {len(self.user_ticket)} symbols. Calculating is starting...")

    def _process(self):
        self.counter = 0
        self.result = ''
        while self.result != self.user_ticket:
            self.result = ''
            for i in range(len(self.user_ticket)):
                a = choice(self.lottery_codes)
                self.result += str(a)
            print(self.result)
            self.counter += 1

    def _inform(self):
        print(f"Attempt: {self.counter} / result: {self.result}")

    def run(self):
        self._ask_ticket()
        self._validate_ticket()
        self._process()
        self._inform()


if __name__ == '__main__': #read
    lottery = Lottery([1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e'])
    lottery.run()



# print(f"The winner is this ticket number: '{choice(lottery_codes)}{choice(lottery_codes)}{choice(lottery_codes)}{choice(lottery_codes)}'. Congratulations!")

