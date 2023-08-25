import random

class GuessGame:
    def __init__(self):
        self.target_number = str(random.randint(1000, 9999))
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
