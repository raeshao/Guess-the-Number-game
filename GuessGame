import random

class GuessGame:
    def __init__(self, target_number=None):
        self.target_number = target_number if target_number else random.randint(1000, 9999)
        self.attempts = 0

    def check_guess(self, guess):
        self.attempts += 1
        if guess == self.target_number:
            return "Congratulations! You guessed the number.", self.attempts
        else:
            hints = []
            for i in range(4):
                if guess[i] == self.target_number[i]:
                    hints.append('circle')
                elif guess[i] in str(self.target_number):
                    hints.append('x')
                else:
                    hints.append(' ')
            return "Hints: " + ', '.join(hints), self.attempts
