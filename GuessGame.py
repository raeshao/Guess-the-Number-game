import random

class GuessGame:
    def __init__(self, target_number=None):
        self.target_number = target_number if target_number is not None else str(random.randint(1000, 9999))
        self.attempts = 0
        self.is_game_over = False

    def check_guess(self, guess):
        if self.is_game_over:
            return "The game is already over. Start a new game."

        self.attempts += 1
        if guess == self.target_number:
            self.is_game_over = True
            return f"Congratulations! You guessed the number in {self.attempts} attempts."

        hints = []
        for i in range(4):
            if guess[i] == self.target_number[i]:
                hints.append('circle')
            elif guess[i] in self.target_number:
                hints.append('x')
            else:
                hints.append(' ')
        
        return "Hints: " + ', '.join(hints)

    def quit_game(self):
        self.is_game_over = True
        return f"The game has ended. You made {self.attempts} attempts."

    def play_game(self):
        while not self.is_game_over:
            guess = input("Enter your guess (or 'quit' to exit): ")
            if guess.lower() == 'quit':
                return self.quit_game()
            result = self.check_guess(guess)
            print(result)

# ... 其他测试用例 ...

if __name__ == '__main__':
    unittest.main()
