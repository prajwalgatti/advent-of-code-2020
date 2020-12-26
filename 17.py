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

cubes = dict.fromkeys(itertools.product(x_range, y_range, z_range), '.')

# intialise active cubes from given input
# TODO: refactor code to improve readability
z = 0
for y in range(height):
    for x in range(width):
        if data[y][x] == '#':
            cubes[(x, -1 * y, z)] = '#'

# Neighbour cube offsets
neighbor_coord_offsets = list(
    itertools.product(*[range(-1, 2)]*3))
neighbor_coord_offsets.remove((0, 0, 0))


# Total count of active cubes
total_active_cubes = 0


def check_rules(cubes, neighbor_coord_offsets, cube_coords):
    """
    check neighbours acc. to the rules given
    """
    count = 0
    change_cube = bool()
    x, y, z = cube_coords
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
                if check_rules(cubes, neighbor_coord_offsets, (x, y, z)):
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
