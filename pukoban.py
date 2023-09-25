import pygame
import manhattan_distance

WALL_SYMBOL = 'O'
STORAGE_SYMBOL = 'S'
BOX_SYMBOL = 'B'
ROBOT_SYMBOL = 'R'

EMPTY_COLOR = (255, 255, 255) # White
WALL_COLOR = (160, 172, 180)      # Gray
STORAGE_COLOR = (0, 255, 0)  # Green
BOX_COLOR = (161, 112, 22)    # Brown
ROBOT_COLOR = (62, 176, 138)   # Teal

# Load custom sprite images
wall_image = pygame.image.load("sprites/PukoWall.png")
storage_image = pygame.image.load("sprites/PukoX.png")
box_image = pygame.image.load("sprites/PukoCrate.png")
robot_image = pygame.image.load("sprites/RobotBoy.png")

# Initialize pygame
pygame.init()

# Constants for button properties
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 50
BUTTON_COLOR = (0, 0, 0)
TEXT_COLOR = (255, 255, 255)
FONT = pygame.font.Font(None, 36)

def read_puzzle_file(filename):
    with open(filename, 'r') as file:
        puzzle_lines = [line.strip() for line in file]

    # Determine the dimensions of the puzzle
    num_rows = len(puzzle_lines)
    num_columns = len(puzzle_lines[0])

    # Create a 2D grid to represent the puzzle
    puzzle_grid = [[' ' for _ in range(num_columns)] for _ in range(num_rows)]

    # Fill the grid and get symbols used
    symbols = set()
    for row_idx, row in enumerate(puzzle_lines):
        for col_idx, char in enumerate(row):
            puzzle_grid[row_idx][col_idx] = char
            symbols.add(char)

    return puzzle_grid, num_rows, num_columns, symbols

puzzle_grid, num_rows, num_columns, symbols = read_puzzle_file("puzzle_files/puzzle_miniscule.txt")

INITIAL_WINDOW_WIDTH = num_rows * 80 + (BUTTON_WIDTH * 2)
INITIAL_WINDOW_HEIGHT = num_columns * 80
INITIAL_CELL_SIZE = 80

# Flag to stop rendering buttons after one is pressed
draw_buttons = True

# Define button positions and labels
buttons = [
    {"rect": pygame.Rect(INITIAL_WINDOW_WIDTH - (BUTTON_WIDTH * 1.5), 20, BUTTON_WIDTH, BUTTON_HEIGHT), "label": "BFS", "algorithm": "BFS"},
    {"rect": pygame.Rect(INITIAL_WINDOW_WIDTH - (BUTTON_WIDTH * 1.5), 90, BUTTON_WIDTH, BUTTON_HEIGHT), "label": "DFS", "algorithm": "DFS"},
    {"rect": pygame.Rect(INITIAL_WINDOW_WIDTH - (BUTTON_WIDTH * 1.5), 160, BUTTON_WIDTH, BUTTON_HEIGHT), "label": "Greedy", "algorithm": "Greedy"},
    {"rect": pygame.Rect(INITIAL_WINDOW_WIDTH - (BUTTON_WIDTH * 1.5), 230, BUTTON_WIDTH, BUTTON_HEIGHT), "label": "A*", "algorithm": "A*"},
]

# Create the game window
screen = pygame.display.set_mode((INITIAL_WINDOW_WIDTH, INITIAL_WINDOW_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Pukoban Solver")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and draw_buttons:  # Left mouse button
                for button in buttons:
                    if button["rect"].collidepoint(event.pos):
                        draw_buttons = False
                        # Handle button click here based on button["algorithm"]
                        if button["algorithm"] == "Greedy":
                            print(manhattan_distance.m_d_heuristic(puzzle_grid))
                            print(manhattan_distance.m_d_heuristic_plus(puzzle_grid))

    # Clear the screen
    screen.fill(EMPTY_COLOR)

    # Scale sprite images based on the scaling factor
    scaled_wall_image = pygame.transform.scale(wall_image, (INITIAL_CELL_SIZE, INITIAL_CELL_SIZE))
    scaled_storage_image = pygame.transform.scale(storage_image, (INITIAL_CELL_SIZE, INITIAL_CELL_SIZE))
    scaled_box_image = pygame.transform.scale(box_image, (INITIAL_CELL_SIZE, INITIAL_CELL_SIZE))
    scaled_robot_image = pygame.transform.scale(robot_image, (INITIAL_CELL_SIZE, INITIAL_CELL_SIZE))

    # Set an initial value for scaled_cell_size
    scaled_cell_size = INITIAL_CELL_SIZE


    for row_idx, row in enumerate(puzzle_grid):
        for col_idx, char in enumerate(row):
            cell_rect = pygame.Rect(
                col_idx * scaled_cell_size, row_idx * scaled_cell_size, scaled_cell_size, scaled_cell_size
            )

            if char == WALL_SYMBOL:
                screen.blit(scaled_wall_image, cell_rect.topleft)
                pygame.draw.rect(screen, WALL_COLOR, cell_rect, 1)  # Cell borders
            elif char == STORAGE_SYMBOL:
                screen.blit(scaled_storage_image, cell_rect.topleft)
            elif char == BOX_SYMBOL:
                screen.blit(scaled_box_image, cell_rect.topleft)
            elif char == ROBOT_SYMBOL:
                screen.blit(scaled_robot_image, cell_rect.topleft)

    # Draw buttons
    if draw_buttons:
        for button in buttons:
            pygame.draw.rect(screen, BUTTON_COLOR, button["rect"])
            text_surface = FONT.render(button["label"], True, TEXT_COLOR)
            text_rect = text_surface.get_rect(center=button["rect"].center)
            screen.blit(text_surface, text_rect)

    pygame.display.flip()

pygame.quit()