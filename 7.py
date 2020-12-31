# Day 7

import re

with open("./input/input_7.txt", 'r') as f:
    data = f.read().splitlines()

# Format the rules, create a dictionary structure
# {'bagname': {'bagname1': number1, 'bagname2': number2}, ...}


def format_bag_list(x): return [x[1], int(x[0])]


pat = r'^\w+ \w+|\d+ \w+ \w+'

data = [re.findall(pat, item) for item in data]
data = {item[0]: dict(
    [format_bag_list(bag.split(' ', maxsplit=1)) for bag in item[1:]])
    for item in data}

GIVEN_BAG = "shiny gold"

# Part 1

container_bags = [GIVEN_BAG]
idx = 0

while(idx < len(container_bags)):
    for bag, bags_contained in data.items():
        if container_bags[idx] in bags_contained.keys():
            if bag not in container_bags:
                container_bags.append(bag)
    idx += 1

print("Part 1")

# len(container_bags) - 1 because the given bag
# is present in container_bags and the given bag
# should not be accounted for.

print("Number of bags that directly/indirectly contain given bag: {}\n".format(len(container_bags) - 1))

# Part 2


def get_bag_capacity(bag):
    if not data[bag]:
        return 0
    capacity = 0
    for contained_bag in data[bag]:
        capacity += data[bag][contained_bag] + \
            get_bag_capacity(contained_bag) * data[bag][contained_bag]
    return capacity


print("Part 2")
print("Capacity of given bag: {}".format(get_bag_capacity(GIVEN_BAG)))
