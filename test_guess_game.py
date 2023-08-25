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

if __name__ == '__main__':
    unittest.main()

