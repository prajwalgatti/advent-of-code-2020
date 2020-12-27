# Day 17
import itertools

with open("./input/input_17.txt", 'r') as f:
    data = f.read().splitlines()

# height and width of given plane
height, width = len(data), len(data[0])

NUM_CYCLES = 6

# Assigning co-ordinates for the cubes in the considered pocket volume
# Assume plane is a XY plane with z = 0
# Assume top left cube of the given plane is origin (0, 0, 0)
x_range = range(-1 * (NUM_CYCLES + 1), width + NUM_CYCLES + 1)
y_range = range(-1 * (height + NUM_CYCLES), NUM_CYCLES + 2)
z_range = range(-1 * (NUM_CYCLES + 1), NUM_CYCLES + 2)

# Format the data into a dictionary where each key is cube's co-ordinates
# ie a tuple (x, y, z) and each key has a value '#' or '.' denoting the
# active or inactive state of a cube
cubes = dict.fromkeys(itertools.product(x_range, y_range, z_range), '.')

# intialise active cubes from given input
z = 0
for y in range(height):
    for x in range(width):
        if data[y][x] == '#':
            cubes[(x, -1 * y, z)] = '#'

# Neighbour cube offsets: all the neihbor cube co-ordinates for
# the origin (0, 0, 0)
neighbor_coord_offsets = list(
    itertools.product(*[range(-1, 2)]*3))
neighbor_coord_offsets.remove((0, 0, 0))


# Total count of active cubes
total_active_cubes = 0


def check_rules(cube_coords):
    """
    Function to check a cube against the given rules
    Return change_cube (bool): Flag to indicate whether the cube's
        state needs to be changed
    """
    count = 0
    change_cube = bool()
    x, y, z = cube_coords

    # Count the number of neighboring cubes having an active state
    for (x_offset, y_offset, z_offset) in neighbor_coord_offsets:
        if cubes[(x + x_offset, y + y_offset, z + z_offset)] == '#':
            count += 1

    if cubes[cube_coords] == '#':
        if count == 3 or count == 2:
            change_cube = False
        else:
            change_cube = True
    elif cubes[cube_coords] == '.':
        if count == 3:
            change_cube = True
        else:
            change_cube = False

    return change_cube


for cycle in range(1, NUM_CYCLES + 1):

    # List of cubes that need to change after a cycle
    change_list = []

    for y in range(cycle, -1 * (height + cycle), -1):
        for x in range(-1 * cycle, width + cycle):
            for z in range(-1 * cycle, cycle + 1):
                if check_rules((x, y, z)):
                    change_list.append((x, y, z))

    # update the cube states (simultaneous update)
    for coords in change_list:
        if cubes[coords] == '#':
            cubes[coords] = '.'
        elif cubes[coords] == '.':
            cubes[coords] = '#'


# count total active cubes after NUM_CYCLES
for cube in cubes:
    if cubes[cube] == '#':
        total_active_cubes += 1

print("Part 1")
print("Total count of active cubes after {} cycles: {}\n".format(
    NUM_CYCLES, total_active_cubes))

# Part 2

# range for the 4th dimension
w_range = range(-1 * (NUM_CYCLES + 1), NUM_CYCLES + 2)

cubes4D = dict.fromkeys(itertools.product(
    x_range, y_range, z_range, w_range), '.')

# intialise active cubes from given input
z = 0
w = 0
for y in range(height):
    for x in range(width):
        if data[y][x] == '#':
            cubes4D[(x, -1 * y, z, w)] = '#'

# Neighbour cube offsets
neighbor_coord_offsets_4D = list(
    itertools.product(*[range(-1, 2)]*4))
neighbor_coord_offsets_4D.remove((0, 0, 0, 0))


# Total count of active cubes
total_active_cubes_4D = 0


def check_rules_4D(cube_coords):
    """
    Function to check a cube of 4-dimensions against the given rules
    Return change_cube (bool): Flag to indicate whether the cube's
        state needs to be changed
    """
    count = 0
    change_cube = bool()
    x, y, z, w = cube_coords

    # Count the number of neighboring cubes having an active state
    for (x_offset, y_offset, z_offset, w_offset) in neighbor_coord_offsets_4D:
        if cubes4D[(x + x_offset, y + y_offset, z + z_offset, w + w_offset)] == '#':
            count += 1

    if cubes4D[cube_coords] == '#':
        if count == 3 or count == 2:
            change_cube = False
        else:
            change_cube = True
    elif cubes4D[cube_coords] == '.':
        if count == 3:
            change_cube = True
        else:
            change_cube = False

    return change_cube


for cycle in range(1, NUM_CYCLES + 1):

    # List of cubes that need to change after a cycle
    change_list = []

    for y in range(cycle, -1 * (height + cycle), -1):
        for x in range(-1 * cycle, width + cycle):
            for z in range(-1 * cycle, cycle + 1):
                for w in range(-1 * cycle, cycle + 1):
                    if check_rules_4D((x, y, z, w)):
                        change_list.append((x, y, z, w))

    # update the cube states (simultaneous update)
    for coords in change_list:
        if cubes4D[coords] == '#':
            cubes4D[coords] = '.'
        elif cubes4D[coords] == '.':
            cubes4D[coords] = '#'


# count total active cubes after NUM_CYCLES
for cube in cubes4D:
    if cubes4D[cube] == '#':
        total_active_cubes_4D += 1

print("Part 2")
print("Total count of active cubes after {} cycles: {}\n".format(
    NUM_CYCLES, total_active_cubes_4D))
