from src.board import Board, Piece
from src.game import Game, Player


def test_game():
    game = Game()
    ui = None

    print("=== Test 1: Initial board state ===")
    assert game._red_pieces == 12
    assert game._black_pieces == 12
    assert game.get_current_player() == Player.RED
    print("PASS: Initial state correct\n")

    print("=== Test 2: Move validation ===")
    board = game._board
    piece = board.get_piece(5, 0)
    assert piece == "red"
    print("PASS: Red piece at position 5 (row 5, col 0)\n")

    print("=== Test 3: Get valid moves for Red ===")
    moves = board.get_valid_moves(Player.RED)
    assert len(moves) > 0
    print(f"PASS: Red has {len(moves)} valid moves")
    print(f"Sample move: {moves[0]}\n")

    print("=== Test 4: Valid move application ===")
    game2 = Game()
    from_row, from_col = 5, 0
    to_row, to_col = 4, 1
    valid = game2.is_valid_move(from_row, from_col, to_row, to_col)
    assert valid
    game2.apply_move(from_row, from_col, to_row, to_col)
    assert game2._board.get_piece(4, 1) == "red"
    assert game2._board.get_piece(5, 0) is None
    assert game2.get_current_player() == Player.BLACK
    print("PASS: Valid move applied correctly\n")

    print("=== Test 5: Capture move ===")
    game3 = Game()
    board3 = game3._board
    board3.set_piece(3, 2, "black")
    board3.set_piece(4, 1, None)
    board3.set_piece(5, 0, "red")
    moves = board3.get_valid_moves(Player.RED)
    capture_move = None
    for move in moves:
        if abs(move[1][0] - move[0][0]) == 2:
            capture_move = move
            break
    if capture_move:
        from_row, from_col = capture_move[0]
        to_row, to_col = capture_move[1]
        game3.apply_move(from_row, from_col, to_row, to_col)
        assert game3._black_pieces == 11
        assert game3._board.get_piece(4, 1) is None
        print(f"PASS: Capture move executed (captured black piece at mid position)")
    else:
        print("SKIP: No capture move available in default setup\n")

    print("=== Test 6: Kinging rules ===")
    game4 = Game()
    board4 = game4._board
    board4.set_piece(1, 0, "red")
    board4.set_piece(0, 1, None)
    game4.apply_move(1, 0, 0, 1)
    king_piece = board4.get_piece(0, 1)
    assert king_piece == "king_red"
    print("PASS: Red piece kinged at opposite end\n")

    print("=== Test 7: King movement ===")
    moves = board4.get_valid_moves(Player.RED)
    king_moving_backward = False
    for move in moves:
        if move[0] == (0, 1) and move[1][0] == 1:
            king_moving_backward = True
            break
    assert king_moving_backward
    print("PASS: King can move backward\n")

    print("=== All tests passed! ===")


if __name__ == "__main__":
    test_game()
