# Data

with open("./input/input_8.txt", 'r') as f:
    data = f.read().splitlines()

# format the data into a list which contains
# instructions of the form ['instruction', offset]
data = [(lambda x: [x[0], int(x[1])])(instruction.split(' '))
        for instruction in data]


def run_boot_code(data, change_instruction_idx=None):
    """
    Function to process boot code instructions

    Input:
      data (list): List of instructions
      change_instruction_idx (int): Index value of instruction to
        change from nop to jmp or vice versa. default value: None

    Returns:
      non_halting_loop (bool): Flag to indicate presence of
         non-halting loop in the code
      accumulator (int): Last updated value of accumulator
    """

    accumulator = 0
    visited_instructions = []
    non_halting_loop = bool()
    current_instruction_idx = 0

    while not non_halting_loop and current_instruction_idx < len(data):
        # check for non halting loop
        if (current_instruction_idx) in visited_instructions:
            non_halting_loop = True
            break

        visited_instructions.append(current_instruction_idx)

        instruction, arg_value = data[current_instruction_idx]

        # check if current instruction needs to be changed
        # jmp to nop or nop to jmp
        if current_instruction_idx == change_instruction_idx:
            if instruction == 'jmp':
                instruction = 'nop'
            elif instruction == 'nop':
                instruction = 'jmp'

        # process instruction
        if instruction == 'jmp':
            current_instruction_idx += arg_value
            continue
        elif instruction == 'acc':
            accumulator += arg_value

        # go to the next instruction
        current_instruction_idx += 1

    return non_halting_loop, accumulator

# Part 1


non_halting_loop, accumulator = run_boot_code(data)

# Output answer
print("Part 1")
if non_halting_loop:
    print("Non-halting loop detected")
    print("Value of accumulator: {}\n".format(accumulator))
else:
    print("Boot code executed successfully\n")


# Part 2

# list of indices of jmp and nop instructions
change_idx = list()

for idx in range(len(data)):
    if data[idx][0] == 'jmp' or data[idx][1] == 'nop':
        change_idx.append(idx)

non_halting_loop, accumulator = True, None

for idx in change_idx:
    non_halting_loop, accumulator = run_boot_code(
        data, change_instruction_idx=idx)
    if not non_halting_loop:
        break

# Print answer
print("Part 2")
if non_halting_loop:
    print("Non-halting loop detected")
else:
    print("Boot code executed successfully")
    print("Value of accumulator: {}\n".format(accumulator))
