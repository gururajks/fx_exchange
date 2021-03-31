# functionalities
# it will have a grid of 7 x 6
from enum import Enum
from pprint import pprint

class PlayerStatus(Enum):
    WON = 1,
    IN_GAME = 2,
    DRAW = 3


class Connect4:

    def __init__(self):
        self.grid = [[None] * 7 for _ in range(6)]

    def game_board_check(self, player, row, col, row_offset, col_offset):

        check = 0
        max_adj = 0
        while 0 < row < len(self.grid) and 0 < col < len(self.grid[0]):
            if self.grid[row][col] == player:
                check += 1
            else:
                check = 0
            if check == 4:
                return True

            row += row_offset
            col += col_offset

        return False

    def did_player_win(self, player, row, col):
        # check vertically
        if self.game_board_check(player, row, col, 0, 1) or self.game_board_check(player, row, col, 0, -1):
            return True

        if self.game_board_check(player, row, col, 1, 0) or self.game_board_check(player, row, col, -1, 0) >= 3:
            return True

        if self.game_board_check(player, row, col, 1, 1) or self.game_board_check(player, row, col, -1, -1):
            return True

        if self.game_board_check(player, row, col, 1, -1) or self.game_board_check(player, row, col, -1, 1):
            return True

        return False

    def game_draw(self):
        for col in range(len(self.grid[0])):
            if self.grid[0][col] is None:
                return False
        return True

    def play(self, player, col):

        if col < 0 or col >= len(self.grid[0]):
            print("invalid column")
            return
        if self.grid[0][col] is not None:
            print("Column is full")
            return

        row = len(self.grid) - 1
        while row >= 0:
            if self.grid[row][col] is None:
                self.grid[row][col] = player
                break
            row -= 1

        if self.did_player_win(player, row, col):
            return PlayerStatus.WON

        if self.game_draw():
            return PlayerStatus.DRAW

        return PlayerStatus.IN_GAME

    def __repr__(self):
        return self.grid


if __name__ == "__main__":
    c = Connect4()
    p = 'O'
    while True:
        i = input(f'{p}  Col:')
        if c.play(p, int(i)) == PlayerStatus.WON:
            pprint(c.grid)
            break
        if p == 'O':
            p = 'X'
        else:
            p = 'O'
        pprint(c.grid)