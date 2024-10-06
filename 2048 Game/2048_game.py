import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 400, 450
TILE_SIZE = WIDTH // 4
FONT = pygame.font.Font(None, 40)
WHITE = (255, 255, 255)
BRIGHT_BLUE = (0, 162, 232)
BRIGHT_YELLOW = (255, 221, 51)
BRIGHT_RED = (255, 76, 76)
BRIGHT_GREEN = (76, 255, 76)
BLACK = (0, 0, 0)

# Tile colors
COLORS = {
    0: (200, 200, 200), 2: (238, 228, 218), 4: (236, 224, 200),
    8: BRIGHT_RED, 16: BRIGHT_YELLOW, 32: (246, 124, 95),
    64: (246, 94, 59), 128: BRIGHT_GREEN, 256: (237, 204, 97),
    512: (237, 200, 80), 1024: (237, 197, 63), 2048: BRIGHT_BLUE
}

# Initialize the board
def initialize_board():
    """Initialize a 4x4 game board with all zeros."""
    return [[0] * 4 for _ in range(4)]

# Adding new tile after every turn
def add_new_tile(board):
    """Add a new tile to the board with a value of 2 or 4."""
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = 2 if random.random() < 0.7 else 4

# Game over function to determine if any legal move is possible
def is_game_over(board):
    """Check if the game is over by checking for any possible moves."""
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return False
            if j < 3 and board[i][j] == board[i][j + 1]:
                return False
            if i < 3 and board[i][j] == board[i + 1][j]:
                return False
    return True

# The functions to make the moves
def move_left(board):
    """Move the tiles to the left and merge any adjacent tiles."""
    moved = False
    score = 0
    for row in board:
        temp = [cell for cell in row if cell != 0]
        for i in range(len(temp) - 1):
            if temp[i] == temp[i + 1] and temp[i] != 0:
                temp[i] *= 2
                score += temp[i]
                temp[i + 1] = 0
                moved = True
        temp = [cell for cell in temp if cell != 0]
        while len(temp) < 4:
            temp.append(0)
        if row != temp:
            moved = True
        row[:] = temp
    return moved, score

def move_right(board):
    """Move the tiles to the right and merge any adjacent tiles."""
    for row in board:
        row.reverse()
    moved, score = move_left(board)
    for row in board:
        row.reverse()
    return moved, score

def transpose(board):
    """Transpose the board."""
    return [[board[j][i] for j in range(4)] for i in range(4)]

def move_up(board):
    """Move the tiles up and merge any adjacent tiles."""
    board[:] = transpose(board)
    moved, score = move_left(board)
    board[:] = transpose(board)
    return moved, score

def move_down(board):
    """Move the tiles down and merge any adjacent tiles."""
    board[:] = transpose(board)
    moved, score = move_right(board)
    board[:] = transpose(board)
    return moved, score

# To make the structure of the board using Pygame
def draw_board(screen, board, score):
    """Draw the game board with the current tiles and score."""
    screen.fill(WHITE)
    score_text = FONT.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))
    
    for i in range(4):
        for j in range(4):
            tile_value = board[i][j]
            tile_color = COLORS[tile_value]
            pygame.draw.rect(screen, tile_color, (j * TILE_SIZE, i * TILE_SIZE + 50, TILE_SIZE, TILE_SIZE))
            pygame.draw
