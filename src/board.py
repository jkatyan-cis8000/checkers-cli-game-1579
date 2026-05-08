from typing import Optional, List, Tuple

Piece = Optional[str]
Move = Tuple[Tuple[int, int], Tuple[int, int]]


class Board:
    def __init__(self):
        self._grid: List[List[Piece]] = [[None for _ in range(8)] for _ in range(8)]
        self._initialize_board()

    def _initialize_board(self):
        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 1:
                    if row < 3:
                        self._grid[row][col] = "black"
                    elif row > 4:
                        self._grid[row][col] = "red"

    def get_piece(self, row: int, col: int) -> Piece:
        if not self.is_valid_position(row, col):
            return None
        return self._grid[row][col]

    def set_piece(self, row: int, col: int, piece: Piece):
        if self.is_valid_position(row, col):
            self._grid[row][col] = piece

    def is_valid_position(self, row: int, col: int) -> bool:
        return 0 <= row < 8 and 0 <= col < 8

    def get_valid_moves(self, player: str) -> List[Move]:
        moves = []
        for row in range(8):
            for col in range(8):
                piece = self.get_piece(row, col)
                if piece and self._is_player_piece(piece, player):
                    piece_moves = self._get_piece_moves(row, col, piece)
                    moves.extend(piece_moves)
        return moves

    def _is_player_piece(self, piece: Piece, player: str) -> bool:
        color = piece if isinstance(piece, str) else None
        return color == player

    def _get_piece_moves(self, row: int, col: int, piece: Piece) -> List[Move]:
        moves = []
        is_king = self._is_king(piece)
        directions = self._get_directions(piece, is_king)

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if self.is_valid_position(new_row, new_col):
                target = self.get_piece(new_row, new_col)
                if target is None:
                    moves.append(((row, col), (new_row, new_col)))
                elif self._is_opponent(piece, target):
                    jump_row, jump_col = new_row + dr, new_col + dc
                    if self.is_valid_position(jump_row, jump_col) and self.get_piece(jump_row, jump_col) is None:
                        moves.append(((row, col), (jump_row, jump_col)))

        return moves

    def _is_king(self, piece: Piece) -> bool:
        return piece.startswith("king_")

    def _get_directions(self, piece: Piece, is_king: bool) -> List[Tuple[int, int]]:
        if is_king:
            return [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        color = piece if isinstance(piece, str) else None
        if color == "red":
            return [(-1, -1), (-1, 1)]
        else:
            return [(1, -1), (1, 1)]

    def _is_opponent(self, piece: Piece, target: Piece) -> bool:
        piece_color = piece if isinstance(piece, str) else None
        target_color = target if isinstance(target, str) else None
        return piece_color != target_color and piece_color is not None and target_color is not None
