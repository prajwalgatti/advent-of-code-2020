# day 2

import re

with open("input.txt", 'r') as f:
    data = f.read().splitlines()

pat = re.compile(r'(\d+)-(\d+)\s(\w):\s(\w+)')
count = 0

data = [pat.match(item).groups() for item in data]

# part 1

for item in data:
    freq = item[3].count(item[2])
    if freq <= int(item[1]) and freq >= int(item[0]):
        count += 1

print("Part 1")
print("Number of valid entries: {}".format(count))

# part 2

count_p2 = 0
for item in data:
    if (item[3][int(item[0])-1] == item[2]) ^ (item[3][int(item[1])-1] == item[2]):
        count_p2 += 1

print("Part 2")
print("Number of valid entries: {}".format(count_p2))
