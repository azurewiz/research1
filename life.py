import numpy as np
import matplotlib.pyplot as plt

def create(size, alive_prob=0.2):

    return np.random.choice([0, 1], size=(size, size), p=[1-alive_prob, alive_prob])

def alive(grid, row, col):
 
    n = grid.shape[0]
    count = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            count += grid[(row + dr) % n, (col + dc) % n]
    return count

def update(current_grid, use_modified_rules=False, extra_birth_prob=0.1):

    n = current_grid.shape[0]
    new_grid = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            neighbors = alive(current_grid, i, j)
            if current_grid[i, j] == 1:
                new_grid[i, j] = 1 if neighbors in [2, 3] else 0
            else:
                if neighbors == 3:
                    new_grid[i, j] = 1
                else:
                    new_grid[i, j] = 1 if use_modified_rules and np.random.rand() < extra_birth_prob else 0
    return new_grid

def run(initial_grid, iterations, use_modified_rules=False, extra_birth_prob=0.1):
    """
    Run the cellular automaton for a specified number of iterations.
    Returns a list containing the grid at each step.
    """
    history = [initial_grid.copy()]
    grid = initial_grid.copy()
    for _ in range(iterations):
        grid = update(grid, use_modified_rules, extra_birth_prob)
        history.append(grid.copy())
    return history

# Simulation settings
grid_dim = 50  # 50x50 grid
num_iterations = 100
mod_prob = 0.1  # 10% chance for spontaneous birth in modified version

# Create initial grid and run two simulations:
# one with standard rules and one with the modified rule.
initial = create(grid_dim, alive_prob=0.2)
history_standard = run(initial, num_iterations, use_modified_rules=False)
history_modified = run(initial.copy(), num_iterations, use_modified_rules=True, extra_birth_prob=mod_prob)

# Visualization helper function:
def show_grid(grid, title=""):
    plt.figure(figsize=(6,6))
    plt.imshow(grid, cmap="binary")
    plt.title(title)
    plt.axis("off")
    plt.show()

# Display final states of both simulations
show_grid(history_standard[-1], title="Final State - Standard Rules")
show_grid(history_modified[-1], title="Final State - Modified Rules")

# Save the final states as images for external visualization (e.g., in Power BI)
plt.imsave("final_standard.png", history_standard[-1], cmap="binary")
plt.imsave("final_modified.png", history_modified[-1], cmap="binary")
