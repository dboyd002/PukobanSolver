import manhattan_distance
import generate_legal_moves
import heapq

def print_grid(grid):
    for row in grid:
        print(" ".join(row))
    print("\n")

def depth_first_search(puzzle_grid):


    stack = []
    
    visited = set()
    
    # Initialize the stack with the initial state and depth 0
    stack.append((puzzle_grid, 0))
    
    while stack:
        current_state, depth = stack.pop()
        
        print(f"Depth {depth}:")
        print_grid(current_state)
        
        # Check if the current state is the goal state
        if manhattan_distance.m_d_heuristic_plus(current_state) == 0:
            print("Goal State Found")
            return current_state
        
        visited.add(tuple(map(tuple, current_state)))
        
        # Get all legal successor states from the current state
        legal_states = generate_legal_moves.successor(current_state)
        legal_states.reverse()  # Reverse the order to prioritize the first legal state
        
        for next_state in legal_states:
            if tuple(map(tuple, next_state)) not in visited:
                stack.append((next_state, depth + 1))
    
    print("No Solution Found")
    return puzzle_grid
