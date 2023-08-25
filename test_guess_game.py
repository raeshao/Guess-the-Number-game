import unittest
from GuessGame import GuessGame

class TestGuessGame(unittest.TestCase):
    def test_generate_secret_number(self):
        game = GuessGame()
        secret_number = game.secret_number
        self.assertTrue(secret_number.isdigit())
        self.assertEqual(len(secret_number), 4)

    def test_generate_hint(self):
        game = GuessGame()
        game.secret_number = '1234'
        hint = game.generate_hint('1324')
        self.assertEqual(hint, 'circle x x circle ')

    def test_player_wins(self):
        game = GuessGame()
        game.secret_number = '1234'
        result = game.evaluate_guess('1234')
        self.assertIn("Congratulations", result)
        self.assertEqual(game.attempts, 1)

    def test_player_guesses_wrong_then_wins(self):
        game = GuessGame()
        game.secret_number = '1234'
        result1 = game.evaluate_guess('5678')
        result2 = game.evaluate_guess('1234')
        self.assertIn("Hint:", result1)
        self.assertIn("Congratulations", result2)
        self.assertEqual(game.attempts, 2)

    def test_invalid_guess(self):
        game = GuessGame()
        result = game.evaluate_guess('abcd')
        self.assertIn("Invalid guess", result)

    def test_quit_game(self):
        game = GuessGame()
        result = game.evaluate_guess('quit')
        self.assertEqual(result, "Quitting the game.")

    # 添加更多测试用例...

if __name__ == '__main__':
    unittest.main()


