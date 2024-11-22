import numpy as np

class PuzzleSolver:
    def __init__(self, start_state):
        self.start_state = start_state
        self.target_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
        self.current_state = start_state

    def calculate_heuristic(self, state):
        distance = 0
        for i in range(1, 9):
            target_pos = np.argwhere(self.target_state == i)[0]
            curr_pos = np.argwhere(state == i)[0]
            distance += abs(target_pos[0] - curr_pos[0]) + abs(target_pos[1] - curr_pos[1])
        return distance

    def get_adjacent_states(self, state):
        adjacent_states = []
        empty_pos = np.argwhere(state == 0)[0]
        x, y = empty_pos

        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = state.copy()
                new_state[x, y], new_state[nx, ny] = new_state[nx, ny], new_state[x, y]
                adjacent_states.append(new_state)
        return adjacent_states

    def solve_puzzle(self):
        self.current_state = self.start_state
        current_heuristic = self.calculate_heuristic(self.current_state)

        while True:
            neighbors = self.get_adjacent_states(self.current_state)
            next_state = None
            next_heuristic = current_heuristic

            for neighbor in neighbors:
                h = self.calculate_heuristic(neighbor)
                if h < next_heuristic:
                    next_heuristic = h
                    next_state = neighbor

            if next_state is None or next_heuristic >= current_heuristic:
                break

            self.current_state = next_state
            current_heuristic = next_heuristic

        return self.current_state, current_heuristic

# Example usage
start_state = np.array([[1, 2, 3], [4, 0, 6], [7, 5, 8]])
solver = PuzzleSolver(start_state)
final_state, final_heuristic = solver.solve_puzzle()

print("Final State:\n", final_state)
print("Final Heuristic Value:", final_heuristic)
