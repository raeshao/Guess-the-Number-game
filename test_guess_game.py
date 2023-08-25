"""Test guess number game"""
import unittest
from GuessGame import GuessNumberGame


class TestGuessGame(unittest.TestCase):
    """Class reprenting Test Guess Game"""
    def test_generate_secret_number(self):
        """Function: test generate secret number"""
        game = GuessNumberGame()
        secret_number = game.secret_number
        self.assertTrue(secret_number.isdigit())
        self.assertEqual(len(secret_number), 4)

    def test_generate_hint(self):
        """Function: test generate hint"""
        game = GuessNumberGame()
        game.secret_number = '1234'
        hint = game.generate_hint('1324')
        self.assertEqual(hint, 'circle x x circle ')

    def test_player_wins(self):
        """Function: test player wins"""
        game = GuessNumberGame()
        game.secret_number = '1234'
        result = game.evaluate_guess('1234')
        self.assertIn("Congratulations", result)
        self.assertEqual(game.attempts, 1)

    def test_player_guesses_wrong_then_wins(self):
        """Function: test player guesses wrong then wins"""
        game = GuessNumberGame()
        game.secret_number = '1234'
        result1 = game.evaluate_guess('5678')
        result2 = game.evaluate_guess('1234')
        self.assertIn("Hint:", result1)
        self.assertIn("Congratulations", result2)
        self.assertEqual(game.attempts, 2)


if __name__ == '__main__':
    unittest.main()


