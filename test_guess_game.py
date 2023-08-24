import unittest
from guess_game import GuessGame

class TestGuessGame(unittest.TestCase):
    def test_random_number_generation(self):
        game = GuessGame()
        self.assertTrue(1000 <= game.target_number <= 9999)

    def test_correct_guess(self):
        game = GuessGame(target_number=1234)
        result = game.check_guess(1234)
        self.assertEqual(result, ("Congratulations! You guessed the number.", 1))

    def test_incorrect_guess(self):
        game = GuessGame(target_number=5678)
        result = game.check_guess(1234)
        self.assertEqual(result, ("Hints: circle, , , ", 1))

if __name__ == '__main__':
    unittest.main()

