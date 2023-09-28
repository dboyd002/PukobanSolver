
# Returns the distance between point p1 and p2 measured along axes at right angles
def manhattan_distance(p1, p2):

    distance = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    return distance

# Returns an estimated number of moves to find a solution based on the shortest manhattan
# distance between each box and the closest storage location to that box
def m_d_heuristic(puzzle_grid):

    # Initialize an empty list to store box coordinates
    box_locations = []

    # Initialize an empty list to store storage location coordinates
    storage_locations = []

    # Iterate through the puzzle grid to find box locations
    for row_idx, row in enumerate(puzzle_grid):
        for col_idx, cell in enumerate(row):
            if cell == 'B':
                box_locations.append((col_idx, row_idx))
            if cell == 'S':
                storage_locations.append((col_idx, row_idx))

    # Stores the estimated number of moves to find a solution
    sum_distance = 0

    # For each box identify the closest storage location and add the distance to sum
    for box in box_locations:
        # Holds the shorter distance each time two are compared, init to large number
        shorter_distance = float('inf')
        for storage in storage_locations:
            distance = manhattan_distance(box, storage)
            shorter_distance = min(shorter_distance, distance)
        sum_distance += shorter_distance

    return sum_distance

# Improved manhattan distance heuristic takes into account the distance between the player
# and target box and penalizes solutions that go through obstacles
def m_d_heuristic_plus(puzzle_grid):

    # Initialize lists to store box and storage locations
    box_locations = []
    storage_locations = []
    obstacle_locations = []

    # Initialize the player (robot) location
    player_location = None

    # Iterate through the puzzle grid to find box, storage, and obstacle locations
    storage_exists = False
    for row_idx, row in enumerate(puzzle_grid):
        for col_idx, cell in enumerate(row):
            if cell == 'B':
                box_locations.append((col_idx, row_idx))
            elif cell == 'C':
                box_locations.append((col_idx, row_idx))
            elif cell == 'S':
                storage_locations.append((col_idx, row_idx))
                storage_exists = True
            elif cell == 'O':
                obstacle_locations.append((col_idx, row_idx))
            elif cell == 'R':
                player_location = (col_idx, row_idx)
            elif cell == 'T':
                player_location = (col_idx, row_idx)
                storage_locations.append((col_idx, row_idx))
                storage_exists = True

    if not storage_exists:
        return 0

    # Stores the estimated number of moves to find a solution
    sum_distance = 0

    # Calculate the distance between the player (robot) and the closest box
    closest_box_distance = float('inf')
    for box in box_locations:
        distance = manhattan_distance(player_location, box)
        closest_box_distance = min(closest_box_distance, distance)

    # For each box, identify the closest storage location and add the distance to sum
    for box in box_locations:
        # Calculate the distance to the closest storage location for each box
        closest_storage_distance = float('inf')
        for storage in storage_locations:
            distance = manhattan_distance(box, storage)
            closest_storage_distance = min(closest_storage_distance, distance)

        # Add the distance to the sum, considering both player-box and box-storage distances
        sum_distance += closest_box_distance + closest_storage_distance

    return sum_distance
