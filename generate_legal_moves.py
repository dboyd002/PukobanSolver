
def move_is_legal(puzzle_grid, robot_position, direction, pulling):

    # Define possible movement directions
    directions = {'North': (0, -1), 'South': (0, 1), 'West': (-1, 0), 'East': (1, 0)}

    # Calculate the new position of the robot after moving in the given direction
    new_x = robot_position[0] + directions[direction][0]
    new_y = robot_position[1] + directions[direction][1]

    # Check if the new position is in the bounds of the puzzle grid
    if not (0 <= new_x < len(puzzle_grid[0]) and 0 <= new_y < len(puzzle_grid)):
        return None  # Illegal move, out of bounds

    # Check if there is an obstacle or wall in the new position
    if puzzle_grid[new_y][new_x] == 'O':
        return None  # Illegal move, obstacle or wall in the way
    
    box_to_pull_position = None

    # Create a new puzzle grid based on the current state
    new_puzzle_grid = [list(row) for row in puzzle_grid]

    try:
        if pulling:
            if direction == "North":
                box_to_pull_position = (robot_position[1] + 1, robot_position[0])
            elif direction == "South":
                box_to_pull_position = (robot_position[1] - 1, robot_position[0])
            elif direction == "West":
                box_to_pull_position = (robot_position[1], robot_position[0] + 1)
            elif direction == "East":
                box_to_pull_position = (robot_position[1], robot_position[0] - 1)

            if new_puzzle_grid[box_to_pull_position[0]][box_to_pull_position[1]] != "B" and new_puzzle_grid[box_to_pull_position[0]][box_to_pull_position[1]] != "C":
                return None
            
    except IndexError:
        return None  # Index out of range, illegal move

    # Check if there is a box in the new position
    if puzzle_grid[new_y][new_x] == 'B' or puzzle_grid[new_y][new_x] == 'C':
        # Calculate the position behind the box in the same direction
        box_behind_x = new_x + directions[direction][0]
        box_behind_y = new_y + directions[direction][1]

        # Check if the space behind the box is inbounds and is empty or storage
        if not (0 <= box_behind_x < len(puzzle_grid[0]) and 0 <= box_behind_y < len(puzzle_grid)) or \
                puzzle_grid[box_behind_y][box_behind_x] not in [' ', 'S']:
            return None  # Illegal move, cannot push the box

        # Update the box's position in the new grid
        if new_puzzle_grid[box_behind_y][box_behind_x] == 'S':
            if puzzle_grid[new_y][new_x] == 'C':
                new_puzzle_grid[new_y][new_x] = 'S'
                new_puzzle_grid[box_behind_y][box_behind_x] = 'C'
            else:
                new_puzzle_grid[new_y][new_x] = ' '
                new_puzzle_grid[box_behind_y][box_behind_x] = 'C'
        else:
            if puzzle_grid[new_y][new_x] == 'C':
                new_puzzle_grid[new_y][new_x] = 'S'
                new_puzzle_grid[box_behind_y][box_behind_x] = 'B'
            else:
                new_puzzle_grid[new_y][new_x] = ' '
                new_puzzle_grid[box_behind_y][box_behind_x] = 'B'

    # Update the robot's position in the new grid
    if pulling == True:
        
        if new_puzzle_grid[box_to_pull_position[0]][box_to_pull_position[1]] == 'C':
            new_puzzle_grid[box_to_pull_position[0]][box_to_pull_position[1]] = 'S'
        else:
            new_puzzle_grid[box_to_pull_position[0]][box_to_pull_position[1]] = ' '
        
        # Check if the space the box is being moved to is storage
        if puzzle_grid[robot_position[1]][robot_position[0]] == 'T':
            new_puzzle_grid[robot_position[1]][robot_position[0]] = 'C'
        else:
            new_puzzle_grid[robot_position[1]][robot_position[0]] = 'B'

        # Check if the space the robot is being moved to is storage
        if puzzle_grid[new_y][new_x] == 'S':
            new_puzzle_grid[new_y][new_x] = 'T'
        else:
            new_puzzle_grid[new_y][new_x] = 'R'

    # Check if there is storage in the new position and represent robot overlapping storage as 'T'
    elif puzzle_grid[new_y][new_x] == 'S' or puzzle_grid[new_y][new_x] == 'C':

        if new_puzzle_grid[robot_position[1]][robot_position[0]] == 'T':
            new_puzzle_grid[robot_position[1]][robot_position[0]] = 'S'
            new_puzzle_grid[new_y][new_x] = 'T'
        else:
            new_puzzle_grid[robot_position[1]][robot_position[0]] = ' '
            new_puzzle_grid[new_y][new_x] = 'T'
        
    else:

        if new_puzzle_grid[robot_position[1]][robot_position[0]] == 'T':
            new_puzzle_grid[robot_position[1]][robot_position[0]] = 'S'
            new_puzzle_grid[new_y][new_x] = 'R'
        else:
            new_puzzle_grid[robot_position[1]][robot_position[0]] = ' '
            new_puzzle_grid[new_y][new_x] = 'R'

    return new_puzzle_grid


# Generates legal successor states for greedy search using manhattan distance heuristic
def successor(current_puzzle_state):

    robot_position = (0, 0)
    legal_states = []

    # Iterate through the puzzle grid to get robot current location
    for row_idx, row in enumerate(current_puzzle_state):
        for col_idx, cell in enumerate(row):
            if cell == 'R' or cell == 'T':
                robot_position = (col_idx, row_idx)

    # Check if which directions the robot can legally move in
    north_move_puzzle_state = move_is_legal(current_puzzle_state, robot_position, 'North', False)
    south_move_puzzle_state = move_is_legal(current_puzzle_state, robot_position, 'South', False)
    west_move_puzzle_state = move_is_legal(current_puzzle_state, robot_position, 'West', False)
    east_move_puzzle_state = move_is_legal(current_puzzle_state, robot_position, 'East', False)
    north_move_puzzle_state_pulling = move_is_legal(current_puzzle_state, robot_position, 'North', True)
    south_move_puzzle_state_pulling = move_is_legal(current_puzzle_state, robot_position, 'South', True)
    west_move_puzzle_state_pulling = move_is_legal(current_puzzle_state, robot_position, 'West', True)
    east_move_puzzle_state_pulling = move_is_legal(current_puzzle_state, robot_position, 'East', True)
    
    if north_move_puzzle_state != None:
        legal_states.append(north_move_puzzle_state)
    if south_move_puzzle_state != None:
        legal_states.append(south_move_puzzle_state)
    if west_move_puzzle_state != None:
        legal_states.append(west_move_puzzle_state)
    if east_move_puzzle_state != None:
        legal_states.append(east_move_puzzle_state)
    if north_move_puzzle_state_pulling != None:
        legal_states.append(north_move_puzzle_state_pulling)
    if south_move_puzzle_state_pulling != None:
        legal_states.append(south_move_puzzle_state_pulling)
    if west_move_puzzle_state_pulling != None:
        legal_states.append(west_move_puzzle_state_pulling)
    if east_move_puzzle_state_pulling != None:
        legal_states.append(east_move_puzzle_state_pulling)

    return legal_states