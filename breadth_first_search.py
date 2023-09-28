import manhattan_distance
import generate_legal_moves
from collections import deque
import heapq

def print_grid(grid):
    for row in grid:
        print(" ".join(row))
    print("\n")

def breadth_first_search(puzzle_grid):

    queue = deque()
    
    visited = set()
    
    # Initialize the queue with the initial state and depth 0
    queue.append((puzzle_grid, 0))
    
    while queue:
        current_state, depth = queue.popleft()
        
        # Print the current state
        print(f"Depth {depth}:")
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
                queue.append((next_state, depth + 1))
    
    print("No Solution Found")
    return puzzle_grid
