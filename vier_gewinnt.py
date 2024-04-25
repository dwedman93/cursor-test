import pygame
import sys

# Game Rules
# 1. This is a two-player game, with players taking turns to drop their pieces into the board.
# 2. The board consists of 6 rows and 7 columns.
# 3. Players use keyboard controls to move left, right, and drop their pieces.
# 4. Player 1 uses 'A' for left, 'D' for right, and 'X' to drop.
# 5. Player 2 uses the left arrow for left, right arrow for right, and 'Enter' to drop.
# 6. The goal is to connect four of one's own discs of the same color next to each other vertically, horizontally, or diagonally before your opponent.
# 7. The game ends when there is a four-in-a-row or a draw if the board fills up without any winning condition met.

# Constants for the game
ROW_COUNT = 6
COLUMN_COUNT = 7
PLAYER_1 = 1
PLAYER_2 = 2
PLAYER_1_KEY_LEFT = pygame.K_a
PLAYER_1_KEY_RIGHT = pygame.K_d
PLAYER_1_DROP_KEY = pygame.K_x
PLAYER_2_KEY_LEFT = pygame.K_LEFT
PLAYER_2_KEY_RIGHT = pygame.K_RIGHT
PLAYER_2_DROP_KEY = pygame.K_RETURN

# Initialize pygame
pygame.init()

# Screen dimensions
SQUARESIZE = 80  # Reduced size for smaller window
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE
size = (width, height)
screen = pygame.display.set_mode(size)
myfont = pygame.font.SysFont("monospace", 60)  # Adjusted font size for smaller window

# Game board
board = [[0 for _ in range(COLUMN_COUNT)] for _ in range(ROW_COUNT)]

def draw_board(board, current_selected_column, turn):
    screen.fill((0, 0, 0))  # Clear the screen to remove previous positions
    # Draw the additional top row if needed for game info
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            # Draw the board cells starting from the second row of pixels
            pygame.draw.rect(screen, (0, 0, 255), (c * SQUARESIZE, (r + 1) * SQUARESIZE, SQUARESIZE, SQUARESIZE))
            # Calculate the center for the pucks to be drawn
            center_x = int(c * SQUARESIZE + SQUARESIZE / 2)
            center_y = int((r + 1) * SQUARESIZE + SQUARESIZE / 2)
            # Draw the pucks
            if board[r][c] == PLAYER_1:
                pygame.draw.circle(screen, (0, 255, 0), (center_x, center_y), int(SQUARESIZE / 2 - 5))
            elif board[r][c] == PLAYER_2:
                pygame.draw.circle(screen, (255, 0, 0), (center_x, center_y), int(SQUARESIZE / 2 - 5))
            else:
                pygame.draw.circle(screen, (0, 0, 0), (center_x, center_y), int(SQUARESIZE / 2 - 5))
    # Highlight the selected column
    pygame.draw.rect(screen, (255, 255, 255), (current_selected_column * SQUARESIZE, SQUARESIZE, SQUARESIZE, height - SQUARESIZE), 2)
    # Show preview puk
    color = (0, 255, 0) if turn == PLAYER_1 else (255, 0, 0)
    pygame.draw.circle(screen, color, (int(current_selected_column * SQUARESIZE + SQUARESIZE/2), int(SQUARESIZE/2)), int(SQUARESIZE/2 - 5))
    
    pygame.display.update()

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):  # Start from top row
        if board[r][col] == 0:
            return r

def check_win(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check positively sloped diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check negatively sloped diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

    return False

def main():
    game_over = False
    turn = 0
    current_selected_column = 3
    # Initialize the board here to ensure it's in the correct scope
    board = [[0 for _ in range(COLUMN_COUNT)] for _ in range(ROW_COUNT)]

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == PLAYER_1_KEY_LEFT or event.key == PLAYER_2_KEY_LEFT:
                    current_selected_column = max(current_selected_column - 1, 0)
                elif event.key == PLAYER_1_KEY_RIGHT or event.key == PLAYER_2_KEY_RIGHT:
                    current_selected_column = min(current_selected_column + 1, COLUMN_COUNT - 1)

                if (event.key == PLAYER_1_DROP_KEY and turn == 0) or (event.key == PLAYER_2_DROP_KEY and turn == 1):
                    if is_valid_location(board, current_selected_column):
                        row = get_next_open_row(board, current_selected_column)
                        drop_piece(board, row, current_selected_column, PLAYER_1 if turn == 0 else PLAYER_2)
                        if check_win(board, PLAYER_1 if turn == 0 else PLAYER_2):
                            game_over = True
                            screen.fill((0, 0, 0))
                            win_text = myfont.render(f"Player {turn + 1} wins!", 1, (255, 255, 255))
                            screen.blit(win_text, (width//2 - win_text.get_width()//2, height//2 - win_text.get_height()//2))
                            pygame.display.update()
                            pygame.time.wait(2000)
                            # Reset the board after a win
                            board = [[0 for _ in range(COLUMN_COUNT)] for _ in range(ROW_COUNT)]
                            game_over = False
                            turn = 0
                            current_selected_column = 3  # Reset to middle column
                            continue
                        turn = 1 - turn

        # Draw the board at the end of each loop iteration
        draw_board(board, current_selected_column, turn)

if __name__ == "__main__":
    main()
