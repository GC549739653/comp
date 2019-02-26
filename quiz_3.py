# Randomly generates a grid with 0s and 1s, whose dimension is controlled by user input,
# as well as the density of 1s in the grid, and finds out, for given step_number >= 1
# and step_size >= 2, the number of stairs of step_number many steps,
# with all steps of size step_size.
#
# A stair of 1 step of size 2 is of the form
# 1 1
#   1 1
#
# A stair of 2 steps of size 2 is of the form
# 1 1
#   1 1
#     1 1
#
# A stair of 1 step of size 3 is of the form
# 1 1 1
#     1
#     1 1 1
#
# A stair of 2 steps of size 3 is of the form
# 1 1 1
#     1
#     1 1 1
#         1
#         1 1 1
#
# The output lists the number of stairs from smallest step sizes to largest step sizes,
# and for a given step size, from stairs with the smallest number of steps to stairs
# with the largest number of stairs.
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randint
import sys
from collections import defaultdict


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))

def stairs_in_grid():
    dic_size = defaultdict(list)
    len_grid = len(grid)

    for i in range(0, len_grid):
        for j in range(0, len(grid[i])):
            if grid[i][j] != 0:
                grid[i][j] = 1

    size = 2
    while True:
        
        if size * 2 - 1 > len_grid:
            break

        steps = 1
        stair_paths = []

        while True:
            stair = get_stair(size, steps)
            len_stair = len(stair)

            if len_stair > len_grid or len(stair[0]) > len_grid:
                break

            cropped_row_range = len_grid - len_stair + 1
            cropped_col_range = len(grid[0]) - len(stair[0]) + 1

            for i in range(0, cropped_row_range):
                for j in range(0, cropped_col_range):
                    cropped_grid = crop_grid(grid, i, j, len_stair, len(stair[0]))

                    if contains_stair(cropped_grid, stair):
                        path = get_stair_path(size, steps, i, j)

                        stair_paths.append((steps, path))

            steps += 1

        stair_paths = sorted(stair_paths, key=lambda x: x[0], reverse=True)
        len_stair_paths = len(stair_paths)

        not_valid_stair_indexes = set()
        for i in range(0, len_stair_paths):
            for j in range(i + 1, len_stair_paths):
                if overlap(stair_paths[i][1], stair_paths[j][1]):
                    not_valid_stair_indexes.add(j)

        valid_stair_paths = []
        for i in range(0, len_stair_paths):
            if i not in not_valid_stair_indexes:
                valid_stair_paths.append(stair_paths[i])

        valid_stair_paths = sorted(valid_stair_paths, key=lambda x: x[0])
        
        dic_steps = defaultdict(int)
        for stair_path in valid_stair_paths:
            dic_steps[stair_path[0]] += 1

        for _steps, num_of_stairs in dic_steps.items():
            dic_size[size].append((_steps, num_of_stairs))

        size += 1

    return dic_size


def overlap(long_path, short_path):
    len_long = len(long_path)
    len_short = len(short_path)

    if len_long <= len_short:
        return False

    i = 0
    j = 0
    while i < len_long:
        if long_path[i] == short_path[0]:
            break
        i += 1

    while i < len_long and j < len_short:
        if long_path[i] != short_path[j]:
            return False
        i += 1
        j += 1

    return j == len_short


def contains_stair(cropped_grid, stair):
    for i in range(0, len(stair)):
        for j in range(0, len(stair[i])):
            if stair[i][j] == 1 and cropped_grid[i][j] == 0:
                    return False

    return True


def crop_grid(original_grid, start_row, start_col, num_row, num_col):

    cropped_grid = [[0 for _ in range(0, num_col)] for _ in range(0, num_row)]

    for i in range(0, num_row):
        for j in range(0, num_col):
            cropped_grid[i][j] = original_grid[start_row + i][start_col + j]

    return cropped_grid


def get_stair_path(size, steps, start_row, start_col):
    row = size * steps - (steps - 1)

    path = []
    pos = 0 
    for i in range(0, row):
        if i % (size - 1) == 0:
            for j in range(0, size):
                path.append((start_row + i, start_col + pos))
                pos += 1
            pos -= 1
        else:
            path.append((start_row + i, start_col + pos))

    return path


def get_stair(size, steps):
    row = size * steps - (steps - 1)
    col = size * (steps + 1) - steps

    stair = [[0 for _ in range(0, col)] for _ in range(0, row)]

    pos = 0 
    for i in range(0, row):
        if i % (size-1) == 0:
            for j in range(0, size):
                stair[i][pos] = 1
                pos += 1
            pos -= 1
        else:
            stair[i][pos] = 1

    return stair
    # Replace return {} above with your code

# Possibly define other functions

try:
    arg_for_seed, density, dim = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, density, dim = int(arg_for_seed), int(density), int(dim)
    if arg_for_seed < 0 or density < 0 or dim < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()
# A dictionary whose keys are step sizes, and whose values are pairs of the form
# (number_of_steps, number_of_stairs_with_that_number_of_steps_of_that_step_size),
# ordered from smallest to largest number_of_steps.
stairs = stairs_in_grid()
for step_size in sorted(stairs):
    print(f'\nFor steps of size {step_size}, we have:')
    for nb_of_steps, nb_of_stairs in stairs[step_size]:
        stair_or_stairs = 'stair' if nb_of_stairs == 1 else 'stairs'
        step_or_steps = 'step' if nb_of_steps == 1 else 'steps'
        print(f'     {nb_of_stairs} {stair_or_stairs} with {nb_of_steps} {step_or_steps}')
