import re
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.board import Board
from src.game import Player


class UI:
    def print_board(self, board: Board):
        print("\n  a b c d e f g h")
        for row in range(8):
            row_str = f"{row + 1} "
            for col in range(8):
                piece = board.get_piece(row, col)
                if piece is None:
                    row_str += ". "
                elif piece == "red" or piece == "king_red":
                    row_str += "R "
                else:
                    row_str += "B "
            print(row_str)
        print()

    def parse_move(self, input_str: str) -> tuple:
        match = re.match(r"^(\d+)-(\d+)$", input_str.strip())
        if not match:
            return None
        
        from_pos, to_pos = int(match.group(1)), int(match.group(2))
        from_row, from_col = from_pos // 8, from_pos % 8
        to_row, to_col = to_pos // 8, to_pos % 8
        
        return (from_row, from_col, to_row, to_col)

    def get_user_move(self, player: str) -> tuple:
        player_name = "Red" if player == Player.RED else "Black"
        move_str = input(f"{player_name}'s turn. Enter move (e.g., 3-10): ")
        return self.parse_move(move_str)

    def display_message(self, msg: str):
        print(msg)
