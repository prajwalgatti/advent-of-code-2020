# Day 6

# Part 1

with open("./input/input_6.txt", 'r') as f:
    data = [group.split('\n') for group in f.read().split('\n\n')]

for group in data:
    if '' in group:
        group.remove('')

total_count_unique = 0

for group in data:
    total_count_unique += len(set("".join(group)))

print("Part 1")
print("Total sum of the counts (unique): {}\n".format(total_count_unique))

# Part 2

total_count_common = 0

for group in data:
    diff = set(group[0])
    for entry_idx in range(1, len(group)):
        diff = diff.intersection(group[entry_idx])
    total_count_common += len(diff)

print("Part 2")
print("Total sum of the counts (common): {}".format(total_count_common))
