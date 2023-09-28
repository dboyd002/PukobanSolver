
import manhattan_distance
import generate_legal_moves
import heapq

def print_grid(grid):
    for row in grid:
        print(" ".join(row))
    print("\n")

def greedy_search(puzzle_grid):

    fringe = []

    # Keep track of visited states
    visited = set()

    initial_heuristic = manhattan_distance.m_d_heuristic_plus(puzzle_grid)
    heapq.heappush(fringe, (initial_heuristic, puzzle_grid))

    while fringe:

          # Get the state with the lowest heuristic
        _, current_state = heapq.heappop(fringe)

        print_grid(current_state)

        # Check if the current state is the goal state
        if manhattan_distance.m_d_heuristic_plus(current_state) == 0:
            print("Goal State Found")
            return current_state

        visited.add(tuple(map(tuple, current_state)))

        # Get all legal successor states from the current state
        legal_states = generate_legal_moves.successor(current_state)

        for next_state in legal_states:
            if tuple(map(tuple, next_state)) not in visited:
                heuristic = manhattan_distance.m_d_heuristic(next_state)
                heapq.heappush(fringe, (heuristic, next_state))

    # Return the original grid if no solution is found
    print("No Solution Found")
    return puzzle_grid