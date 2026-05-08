import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.board import Board, Move, Piece
from src.game import Game, Player
from src.ui import UI


def main():
    game = Game()
    ui = UI()

    while not game.is_game_over():
        ui.print_board(game._board)
        current_player = game.get_current_player()

        while True:
            try:
                move_input = input(f"{current_player.capitalize()} player's turn. Enter move (e.g., 3-10): ")
                parts = move_input.strip().split('-')
                if len(parts) != 2:
                    ui.display_message("Invalid format. Use 'from-to' (e.g., 3-10)")
                    continue

                from_pos, to_pos = int(parts[0]), int(parts[1])
                from_row, from_col = from_pos // 8, from_pos % 8
                to_row, to_col = to_pos // 8, to_pos % 8

                if game.is_valid_move(from_row, from_col, to_row, to_col):
                    game.apply_move(from_row, from_col, to_row, to_col)
                    break
                else:
                    ui.display_message("Invalid move. Try again.")
            except (ValueError, IndexError):
                ui.display_message("Invalid input. Use numbers (e.g., 3-10)")

    winner = game.check_winner()
    ui.print_board(game._board)
    ui.display_message(f"Game over! {winner.capitalize()} wins!")


if __name__ == "__main__":
    main()
