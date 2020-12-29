# Day 11

import itertools
from copy import deepcopy

with open("./input/input_11.txt", 'r') as f:
    data = [list(line) for line in f.read().splitlines()]

# Copying data since they will be edited in the process
part1_data = deepcopy(data)
part2_data = deepcopy(data)

n_rows, n_cols = len(data), len(data[0])

# Part 1

stable_state = False

# Co-ordinate offset values of adjacent seats
adjacent_seat_coords = list(itertools.product(range(-1, 2), range(-1, 2)))
adjacent_seat_coords.remove((0, 0))

while not stable_state:

    # List of seats whose states need to be changed
    update_list = []

    for i in range(n_rows):
        for j in range(n_cols):

            # If the position is floor
            if part1_data[i][j] == '.':
                continue

            occupied_seat_count = 0

            for i_offset, j_offset in adjacent_seat_coords:
                # Check if index is out of grid range
                if not (i + i_offset < 0 or j + j_offset < 0
                        or i + i_offset >= n_rows or j + j_offset >= n_cols):
                    if part1_data[i + i_offset][j + j_offset] == '#':
                        occupied_seat_count += 1

            if part1_data[i][j] == 'L' and not occupied_seat_count:
                update_list.append((i, j))
            elif part1_data[i][j] == '#' and occupied_seat_count >= 4:
                update_list.append((i, j))

    if update_list:
        # Perfrom simultaneous update
        for i, j in update_list:
            if part1_data[i][j] == '#':
                part1_data[i][j] = 'L'
            elif part1_data[i][j] == 'L':
                part1_data[i][j] = '#'
    else:
        # No seats to be updated at the end of the round
        # So equilibrium has been reached
        stable_state = True

total_occupied_seat_count_1 = sum([row.count('#') for row in part1_data])

print("Part 1")
print("Number of occupied seats after stable state: {}\n".format(
    total_occupied_seat_count_1))

# Part 2

stable_state = False

while not stable_state:

    # List of seats whose states need to be changed
    update_list = []

    for i in range(n_rows):
        for j in range(n_cols):

            # If the position is floor
            if part2_data[i][j] == '.':
                continue

            occupied_seat_count = 0

            for i_direction, j_direction in adjacent_seat_coords:

                i_offset = i_direction
                j_offset = j_direction

                while not (i + i_offset < 0 or j + j_offset < 0
                           or i + i_offset >= n_rows or j + j_offset >= n_cols):

                    # Check if index is out of grid range
                    if part2_data[i + i_offset][j + j_offset] == '#':
                        occupied_seat_count += 1
                        break
                    elif part2_data[i + i_offset][j + j_offset] == 'L':
                        break

                    # update offsets
                    i_offset += i_direction
                    j_offset += j_direction

            if part2_data[i][j] == 'L' and not occupied_seat_count:
                update_list.append((i, j))
            elif part2_data[i][j] == '#' and occupied_seat_count >= 5:
                update_list.append((i, j))

    if update_list:
        # Perfrom simultaneous update
        for i, j in update_list:
            if part2_data[i][j] == '#':
                part2_data[i][j] = 'L'
            elif part2_data[i][j] == 'L':
                part2_data[i][j] = '#'
    else:
        # No seats to be updated at the end of the round
        # So equilibrium has been reached
        stable_state = True

total_occupied_seat_count_2 = sum([row.count('#') for row in part2_data])

print("Part 2")
print("Number of occupied seats after stable state: {}\n".format(
    total_occupied_seat_count_2))
