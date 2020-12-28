# Day 10

with open("./input/input_10.txt", 'r') as f:
    data = [int(line) for line in f]

# Effective Joltage of the outlet
OUTLET_JOLTAGE = 0

# Device Joltage
DEVICE_JOLTAGE = max(data) + 3

# Allowable difference in Joltage values for the adapters
allowable_differences = (1, 2, 3)

# Sort the adapters by Joltage values
data.sort()

# List of Joltage differences between adapters in the chain
difference_list = [b - a for a,
                   b in zip([OUTLET_JOLTAGE] + data, data + [DEVICE_JOLTAGE])]

# Check if differences are in the allowed range of values
if set(difference_list).difference(allowable_differences):
    raise Exception(
        "Incorrect chaining of adapters. Difference in joltage exceed the allowable values")

print("Part 1")
print("Answer: {}".format(difference_list.count(1) * difference_list.count(3)))
