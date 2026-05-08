from src.game import Game
from src.ui import UI


def main():
    game = Game()
    ui = UI()

    while not game.is_game_over():
        ui.print_board(game._board)
        move = ui.get_user_move(game.get_current_player())
        
        if move is None:
            ui.display_message("Invalid move format. Use 'from-to' notation (e.g., 3-10).")
            continue
        
        from_row, from_col, to_row, to_col = move
        
        if not game.is_valid_move(from_row, from_col, to_row, to_col):
            ui.display_message("Invalid move.")
            continue
        
        game.apply_move(from_row, from_col, to_row, to_col)

    winner = game.check_winner()
    ui.display_message(f"Game over! {winner} wins!" if winner else "Game over!")


if __name__ == "__main__":
    main()
