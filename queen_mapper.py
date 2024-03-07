import pygame
from pygame.locals import *
from io import BytesIO

# Initialize Pygame
pygame.init()
window_size = 512  # Window size, making a 512x512 window
board_size = 8  # Chess board size, 8x8
square_size = window_size // board_size
screen = pygame.display.set_mode((window_size, window_size))

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Load the queen image
def load_queen_image():
    queen_png = pygame.image.load('queen.png')
    return queen_png

# Draw the chess board
def draw_board():
    screen.fill(black)
    for row in range(board_size):
        for col in range(board_size):
            if (row + col) % 2 == 0:
                pygame.draw.rect(screen, white, (col * square_size, row * square_size, square_size, square_size))

# Convert chess notation to screen position
def notation_to_position(notation):
    letter_to_number = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    col = letter_to_number[notation[0]]
    row = 8 - int(notation[1])
    return (col * square_size, row * square_size)

# Place a queen on the board
def place_queen(position):
    queen_png = load_queen_image()
    queen_png = pygame.transform.scale(queen_png, (square_size, square_size))
    screen.blit(queen_png, position)

# Main function to set up the board and place queens
def main(queen_positions):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        draw_board()

        for pos in queen_positions:
            place_queen(notation_to_position(pos))

        pygame.display.flip()

    pygame.quit()

# Example usage
if __name__ == "__main__":
    queen_positions = ['e5', 'd2']  # List your queen positions here
    main(queen_positions)
