import unittest
from connect4 import Connect4, PlayerStatus
import random
from pprint import pprint

class TestConnect4(unittest.TestCase):

    def setUp(self) -> None:
        self.test_board = Connect4()

    def tearDown(self) -> None:
        self.test_board = None

    def test_play(self):
        self.test_board.play('X', 3)
        self.test_board.play('Y', 2)
        self.assertEqual(self.test_board.grid[5][3], 'X')
        self.assertEqual(self.test_board.grid[5][2], 'Y')
        pprint(self.test_board.grid)

    def test_vertical_check_did_player_win(self):
        self.test_board.play('X', 3)
        self.test_board.play('X', 3)
        self.test_board.play('X', 3)
        self.assertEqual(self.test_board.play('X', 3), PlayerStatus.WON)

    def test_horz_check_did_player_win(self):
        self.test_board.play('X', 1)
        self.test_board.play('X', 2)
        self.test_board.play('X', 3)
        self.assertEqual(self.test_board.play('X', 4), PlayerStatus.WON)
        pprint(self.test_board.grid)

    def test_rev_diag_check_did_player_win(self):
        self.test_board.play('Y', 1)
        self.test_board.play('Y', 1)
        self.test_board.play('X', 2)
        self.test_board.play('Y', 2)
        self.test_board.play('X', 3)
        self.test_board.play('Y', 3)
        self.test_board.play('Y', 3)
        self.test_board.play('X', 4)
        self.test_board.play('Y', 4)
        self.test_board.play('X', 4)
        self.assertEqual(self.test_board.play('Y', 4), PlayerStatus.WON)
        pprint(self.test_board.grid)

    def test_diag_check_player_win(self):
        self.test_board.play('Y', 1)
        self.test_board.play('Y', 1)
        self.test_board.play('X', 2)
        self.test_board.play('Y', 2)
        self.test_board.play('X', 3)
        self.test_board.play('X', 3)
        self.test_board.play('Y', 3)
        self.test_board.play('X', 4)
        self.test_board.play('Y', 4)
        self.test_board.play('Y', 4)
        self.assertEqual(self.test_board.play('Y', 4), PlayerStatus.WON)
        pprint(self.test_board.grid)


    def test_computer_play(self):
        pass

if __name__ == '__main__':
    unittest.main()
