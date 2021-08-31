import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

N = 100
population = 3000
percentage = [0.6, 0.4]  # percents
tolerance = 0.5  # percents
steps = 10

free_space = 0
first_group = 1
second_group = 2


# vals = [free_space, first_group]
def randomize_agents(grid, num, group):
    for i in range(0, num):
        x = np.random.randint(N)
        y = np.random.randint(N)
        is_empty = True
        while is_empty:
            if grid[x, y] == free_space:
                grid[x, y] = group
                is_empty = False
            else:
                x = np.random.randint(N)
                y = np.random.randint(N)
    return grid


def random_grid(N):
    num1 = int(population * percentage[0])
    num2 = int(population * percentage[1])
    grid = np.zeros([N, N])

    grid = randomize_agents(grid, num1, first_group)
    grid = randomize_agents(grid, num2, second_group)

    return grid
    # random.choice(vals, N * N, p=[1 - population / (N * N), population / (N * N)]).reshape(N, N)


def is_happy(grid):
    pass


def rearrange_grid():
    pass


def scan_grid(frameNum, img, grid, group, tolerance):
    new_grid = grid.copy()
    for i in range(0, N):
        for j in range(0, N):
            total = int((grid[i, (j - 1) % N] + grid[i, (j + 1) % N] +
                         grid[(i - 1) % N, j] + grid[(i + 1) % N, j] +
                         grid[(i - 1) % N, (j - 1) % N] + grid[(i - 1) % N, (j + 1) % N] +
                         grid[(i + 1) % N, (j - 1) % N] + grid[(i + 1) % N, (j + 1) % N]) / group)

            if grid[i, j] == group:
                if is_happy():
                    pass

    pass


def main():
    # grid = np.array([])
    grid = random_grid(N)
    plt.figure(figsize=(5, 5))
    colormap = colors.ListedColormap(["snow", "magenta", "turquoise"])
    plt.imshow(grid, cmap=colormap)
    plt.show()


if __name__ == '__main__':
    main()
