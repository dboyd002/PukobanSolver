
import manhattan_distance

def greedy_search(puzzle_grid):

    # Initialize a tuple to storage robot coordinates
    robot_location = (0, 0)

    # Initialize an empty list to store box coordinates
    box_locations = []

    # Initialize an empty list to store storage location coordinates
    storage_locations = []

    # Initialize an empty list to store obstacle location coordinates
    obstacle_locations = []

    # Iterate through the puzzle grid to find box locations
    for row_idx, row in enumerate(puzzle_grid):
        for col_idx, cell in enumerate(row):
            if cell == "R":
                robot_location = (col_idx, row_idx)
            if cell == 'B':
                box_locations.append((col_idx, row_idx))
            if cell == 'S':
                storage_locations.append((col_idx, row_idx))
            if cell == "O":
                obstacle_locations.append((col_idx, row_idx))

    # For each box identify the closest storage location 