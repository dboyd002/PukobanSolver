import manhattan_distance
import generate_legal_moves
import heapq

def print_grid(grid):
    for row in grid:
        print(" ".join(row))
    print("\n")

def astar_search(puzzle_grid):

    priority_queue = []
    
    visited = set()
    
    # Initialize the priority queue with the initial state and priority 0
    initial_heuristic = manhattan_distance.m_d_heuristic_plus(puzzle_grid)
    heapq.heappush(priority_queue, (initial_heuristic, puzzle_grid, 0))
    
    while priority_queue:
        _, current_state, cost = heapq.heappop(priority_queue)
        
        print(f"Cost {cost}:")
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
                heuristic = manhattan_distance.m_d_heuristic_plus(next_state)
                heapq.heappush(priority_queue, (cost + heuristic, next_state, cost + 1))
    
    # Return None if no solution is found
    print("No Solution Found")
    return puzzle_grid