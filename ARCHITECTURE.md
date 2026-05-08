# ARCHITECTURE.md

Written by team-lead before spawning teammates. This is the shared blueprint —
teammates read it to understand what they are building and how their module fits.

## Module Structure

- src/board.py: 8x8 board state, piece management, validation helpers
- src/game.py: turn management, move execution, capture/kinging rules
- src/ui.py: terminal rendering, move input parsing (notation format like "3-10")
- main.py: entry point, coordinates game loop via UI and Game

## Interfaces

### board.py
- `Board`: class managing 8x8 grid
  - `__init__()` - initialize empty board with starting positions
  - `get_piece(row, col)` - returns piece object or None
  - `set_piece(row, col, piece)` - places a piece
  - `is_valid_position(row, col)` - returns bool
  - `get_valid_moves(player)` - returns list of valid moves for player

### game.py
- `Game`: main game state and rules
  - `__init__()` - creates board, sets initial turn (Player.RED starts)
  - `get_current_player()` - returns current player
  - `is_valid_move(from_row, from_col, to_row, to_col)` - validates move
  - `apply_move(from_row, from_col, to_row, to_col)` - executes move, handles captures/kinging
  - `check_winner()` - returns winning player or None
  - `is_game_over()` - returns bool

### ui.py
- `UI`: handles terminal interaction
  - `print_board(board)` - renders board to stdout
  - `parse_move(input_str)` - parses "3-10" format, returns (from_row, from_col, to_row, to_col)
  - `get_user_move(player)` - prompts player, returns parsed move
  - `display_message(msg)` - prints game messages

### main.py
- Entry point that ties Game and UI together in a loop
- Creates Game instance, calls UI to get moves, applies to Game

## Shared Data Structures

### Piece
```python
class Piece:
    color: str  # "red" or "black"
    is_king: bool
```

### Move
```python
Move = Tuple[Tuple[int, int], Tuple[int, int]]  # ((from_row, from_col), (to_row, to_col))
```

### Player
```python
class Player:
    RED = "red"
    BLACK = "black"
```

## External Dependencies

- No external dependencies required (standard library only)
