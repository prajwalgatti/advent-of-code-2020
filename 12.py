# Day 12

with open("./input/input_12.txt") as f:
    data = [[line[0], int(line[1:])] for line in f.read().splitlines()]

directions = ('E', 'N', 'W', 'S')

displacement_values = dict.fromkeys(directions, 0)

# Index of current direction
idx_current_dir = 0

for action, value in data:
    if action in directions:
        displacement_values[action] += value
    elif action == 'R':
        if (idx_current_dir := idx_current_dir - (value // 90)) < 0:
            idx_current_dir = 4 + idx_current_dir
    elif action == 'L':
        if (idx_current_dir := idx_current_dir + (value // 90)) >= 4:
            idx_current_dir = idx_current_dir % 4
    elif action == 'F':
        displacement_values[directions[idx_current_dir]] += value

print("Part 1")
print("Total displacement: {}".format(abs(
    displacement_values['S'] - displacement_values['N'] + displacement_values['E'] - displacement_values['W'])))

# Part 2
