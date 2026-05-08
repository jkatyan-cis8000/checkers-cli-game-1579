from typing import Optional
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.board import Board, Move, Piece


class Player:
    RED = "red"
    BLACK = "black"


class Game:
    def __init__(self):
        self._board = Board()
        self._current_player = Player.RED
        self._red_pieces = 12
        self._black_pieces = 12

    def get_current_player(self) -> str:
        return self._current_player

    def is_valid_move(self, from_row: int, from_col: int, to_row: int, to_col: int) -> bool:
        if not self._board.is_valid_position(from_row, from_col) or not self._board.is_valid_position(to_row, to_col):
            return False
        
        piece = self._board.get_piece(from_row, from_col)
        if piece is None:
            return False

        valid_moves = self._board.get_valid_moves(self._current_player)
        move = ((from_row, from_col), (to_row, to_col))
        return move in valid_moves

    def apply_move(self, from_row: int, from_col: int, to_row: int, to_col: int) -> bool:
        if not self.is_valid_move(from_row, from_col, to_row, to_col):
            return False

        piece = self._board.get_piece(from_row, from_col)
        self._board.set_piece(from_row, from_col, None)
        self._board.set_piece(to_row, to_col, piece)

        if abs(to_row - from_row) == 2:
            mid_row = (from_row + to_row) // 2
            mid_col = (from_col + to_col) // 2
            captured = self._board.get_piece(mid_row, mid_col)
            if captured:
                self._board.set_piece(mid_row, mid_col, None)
                if captured == "red":
                    self._red_pieces -= 1
                else:
                    self._black_pieces -= 1

        self._king_piece(to_row, to_col, piece)

        self._current_player = Player.BLACK if self._current_player == Player.RED else Player.RED
        return True

    def _king_piece(self, row: int, col: int, piece: Piece):
        if piece == "red" and row == 0:
            self._board.set_piece(row, col, "king_red")
        elif piece == "black" and row == 7:
            self._board.set_piece(row, col, "king_black")

    def check_winner(self) -> Optional[str]:
        if self._red_pieces == 0:
            return Player.BLACK
        if self._black_pieces == 0:
            return Player.RED
        
        red_moves = self._board.get_valid_moves(Player.RED)
        black_moves = self._board.get_valid_moves(Player.BLACK)
        
        if self._current_player == Player.RED and len(red_moves) == 0:
            return Player.BLACK
        if self._current_player == Player.BLACK and len(black_moves) == 0:
            return Player.RED
        
        return None

    def is_game_over(self) -> bool:
        return self.check_winner() is not None
