"""
The initialization file to the entire `pychess` package.
All files and modules will have docstrings at the top.
Code is commented throughout.
"""

# version info
__version__ = 'v0.0.1'

# external imports
import numpy as np


# Game class
class Game(object):

    def __init__(self):

        """
        BOARD CODES:
            '_' -- BLANK SQUARE
            'p'/'P' -- PAWN (WHITE/BLACK)
            'r'/'R' -- ROOK (WHITE/BLACK)
            'n'/'N' -- KNIGHT (WHITE/BLACK)
            'b'/'B' -- BISHOP (WHITE/BLACK)
            'q'/'Q' -- QUEEN (WHITE/BLACK)
            'k'/'K' -- KING (WHITE/BLACK)
        BOARD IS ALWAYS STORED FROM
        WHITE'S PERSPECTIVE (WHITE ON 'TOP')
        """

        self.board = np.asarray([['_'] * 8] * 8)
        self.board[0] = np.asarray(['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'])
        self.board[1] = np.asarray(['p'] * 8)
        self.board[7] = np.asarray(['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'])
        self.board[6] = np.asarray(['P'] * 8)

        self.turn = 'white'

    def display(self):

        disp_board = self.board

        # flip board right-side-up
        if self.turn == 'white':
            disp_board = disp_board[::-1]

        # replace chess codes with respective unicode symbols
        for x in range(disp_board.shape[0]):
            for y in range(disp_board.shape[1]):

                if disp_board[x, y] == '_' and (x % 2) == (y % 2):
                    disp_board[x, y] = '■'
                elif disp_board[x, y] == '_':
                    disp_board[x, y] = '□'
                if disp_board[x, y] == 'p':
                    disp_board[x, y] = '♙'
                if disp_board[x, y] == 'P':
                    disp_board[x, y] = '♟'
                if disp_board[x, y] == 'r':
                    disp_board[x, y] = '♖'
                if disp_board[x, y] == 'R':
                    disp_board[x, y] = '♜'
                if disp_board[x, y] == 'n':
                    disp_board[x, y] = '♘'
                if disp_board[x, y] == 'N':
                    disp_board[x, y] = '♞'
                if disp_board[x, y] == 'b':
                    disp_board[x, y] = '♗'
                if disp_board[x, y] == 'B':
                    disp_board[x, y] = '♝'
                if disp_board[x, y] == 'q':
                    disp_board[x, y] = '♕'
                if disp_board[x, y] == 'Q':
                    disp_board[x, y] = '♛'
                if disp_board[x, y] == 'k':
                    disp_board[x, y] = '♔'
                if disp_board[x, y] == 'K':
                    disp_board[x, y] = '♚'

        printed_result = ''
        for line in disp_board:
            printed_result += ' '.join(line)
            printed_result += '\n'

        print(printed_result)
        return disp_board

    def move(self, fro, to, prom=None, castling=False, en_passant=False):
        """
        THIS IS NOT A STANDARD CHESS MOVE
        COORDINATES SHOULD BE IN FORM (Y, X)
        DOES NOT CHECK IF MOVE IS LEGAL
        MOVES PIECE ON FRO TO PIECE ON TO AND ALLOWS FOR PROMOTION, CAPTURES, AND EN PASSANT
        CASTLING MUST BE DONE AS TWO SEPARATE MOVES (SET CASTLING=TRUE FOR FIRST MOVE)
        """

        self.board[to] = self.board[fro]
        self.board[fro] = '_'

        if en_passant:
            # left capture
            if to[1] == fro[1] - 1:
                self.board[fro[0], fro[1] - 1] == '_'
            # right capture
            if to[1] == fro[1] + 1:
                self.board[fro[0], fro[1] - 1] == '_'

        # promotion
        if prom:
            self.board[to] = prom

        # change turn
        if not castling:
            if self.turn == 'white':
                self.turn == 'black'
            else:
                self.turn = 'white'

        return self.board
