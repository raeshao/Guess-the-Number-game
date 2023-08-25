import random

class GuessGame:
    def __init__(self):
        self.secret_number = self.generate_secret_number()
        self.attempts = 0

    def generate_secret_number(self):
        return str(random.randint(1000, 9999))

    def get_guess(self):
        return input("Enter your guess: ")

    def evaluate_guess(self, guess):
        self.attempts += 1
        if guess == self.secret_number:
            return "Congratulations! You guessed the number in {} attempts.".format(self.attempts)
        else:
            hint = self.generate_hint(guess)
            return "Hint: {}".format(hint)

    def generate_hint(self, guess):
        hint = ''
        for i in range(4):
            if guess[i] == self.secret_number[i]:
                hint += 'circle '
            elif guess[i] in self.secret_number:
                hint += 'x '
            else:
                hint += '- '
        return hint

    def play(self):
        print("Welcome to the Number Guessing Game!")
        while True:
            guess = self.get_guess()
            if guess.lower() == 'quit':
                print("Quitting the game.")
                break
            result = self.evaluate_guess(guess)
            print(result)
            if guess == self.secret_number:
                break

if __name__ == "__main__":
    game = GuessGame()
    game.play()
