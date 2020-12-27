# Day 9

with open("./input/input_9.txt") as f:
    data = [int(line) for line in f]

# Length of preamble
N_PREAMBLE = 25


def pair_sum(arr, sum_val):
    """
    Function to check for a pair in a list (arr) that adds up to a
    value (sum_val)
    Returns True if such a pair exists, False if no such pair exists.
    """
    for arr_idx in range(len(arr)):
        if sum_val - arr[arr_idx] in arr[:arr_idx] + arr[arr_idx:]:
            # Pair found
            return True
    # Pair not found
    return False


# Number which does not follow the rule
invalid_number = None
invalid_number_idx = None

for idx in range(N_PREAMBLE, len(data)):
    if not pair_sum(data[idx - N_PREAMBLE: idx], data[idx]):
        invalid_number = data[idx]
        invalid_number_idx = idx
        break

print("Part 1")
if invalid_number:
    print("The first number to not follow the rule: {}\n".format(invalid_number))
else:
    print("Required number not found.")

# Part 2

# required contiguous set of numbers
contiguous_set = None

for num_data in (data[:invalid_number_idx], data[invalid_number_idx + 1:]):
    for idx_i in range(len(num_data) - 1):
        sum_val = num_data[idx_i]
        idx_j = idx_i + 1
        while (not sum_val >= invalid_number) and (idx_j < len(num_data)):
            sum_val += num_data[idx_j]
            idx_j += 1
        if sum_val == invalid_number:
            contiguous_set = num_data[idx_i: idx_j]
            break

print("Part 2")
if contiguous_set:
    print("Required contiguous set of numbers found")
    print("Answer: {}".format(min(contiguous_set) + max(contiguous_set)))
else:
    print("Required contiguous set of numbers not found.")
