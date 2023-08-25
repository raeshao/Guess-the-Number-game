import unittest
from unittest.mock import patch  # import patch
from GuessGame import GuessGame
class TestGuessGame(unittest.TestCase):
    def test_random_number_generation(self):
        game = GuessGame()
        self.assertTrue(1000 <= int(game.target_number) <= 9999)

    def test_correct_guess(self):
        game = GuessGame(target_number='1234')
        result = game.check_guess('1234')
        self.assertEqual(result, ("Congratulations! You guessed the number.", 1))

    def test_incorrect_guess(self):
        game = GuessGame(target_number='5678')
        result = game.check_guess('1234')
        self.assertEqual(result, ("Hints: circle, , , ", 1))
    # new usecase begins
    def test_continuous_guessing(self):
    game = GuessGame()
    with patch('builtins.input', side_effect=['1234', 'quit']):
        result = game.check_guess('1234')  # Simulate the first guess
        self.assertEqual(result, "Congratulations! You guessed the number in 1 attempts.")
        
        # The game should be over now, so any further guesses should return a message about the game being over
        result = game.check_guess('5678')
        self.assertEqual(result, "The game is already over. Start a new game.")
        
    self.assertEqual(game.attempts, 1)


    def test_hints_generation(self):
        game = GuessGame(target_number='1234')
        hints, _ = game.check_guess('1243')
        self.assertEqual(hints, 'circle, x, x, ')

    def test_display_attempts(self):
        game = GuessGame(target_number='1234')
        _, attempts = game.check_guess('1234')
        self.assertEqual(attempts, 1)

    def test_quit_game(self):
        game = GuessGame(target_number='1234')
        with patch('builtins.input', return_value='quit'):
            result = game.quit_game()
        self.assertEqual(result, 'Game over. Attempts: 0')

    def test_player_can_quit(self):
        game = GuessGame(target_number='1234')
        with patch('builtins.input', return_value='quit'):
            result = game.play_game()
        self.assertEqual(result, 'Game over. Attempts: 0')

if __name__ == '__main__':
    unittest.main()

