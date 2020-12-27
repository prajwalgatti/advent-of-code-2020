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
required_num = None

for idx in range(N_PREAMBLE, len(data)):
    if not pair_sum(data[idx - N_PREAMBLE: idx], data[idx]):
        required_num = data[idx]
        break

print("Part 1")
if required_num:
    print("The first number to not follow the rule: {}\n".format(required_num))
else:
    print("Required number not found.")
