# day 3

with open("./input/input_3.txt", 'r') as f:
    data = f.read().splitlines()

pattern_length = len(data)
pattern_width = len(data[0])

# part 1

count = 0
position = 3

for row in data[1:]:
    if row[position] == '#':
        count += 1
    position = (position + 3) % pattern_width

print("Part 1")
print("Number of trees encountered: {}\n".format(count))

# part 2

# list of slopes
# each slope: (right value, down value)
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
count_for_each_slope = list()
answer = 1

for right, down in slopes:
    count = 0
    position = right
    for row in range(down, pattern_length, down):
        if data[row][position] == '#':
            count += 1
        position = (position + right) % pattern_width
    count_for_each_slope.append(count)

print("Part 2")
for slope, count in zip(slopes, count_for_each_slope):
    print("Slope: {} Number of trees encountered: {}".format(slope, count))

for count in count_for_each_slope:
    answer *= count
print("Answer: {}".format(answer))
