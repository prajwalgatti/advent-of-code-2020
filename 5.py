# Day 5

with open("./input/input_5.txt", 'r') as f:
    data = f.read().splitlines()

# Part 1

seat_dict = {}
for seat in data:
    row, col = 0, 0
    # lower and upper limit for row number
    ll, ul = 1, 128
    for letter in seat[:-3]:
        if letter == 'F':
            ul -= (ul - ll + 1) / 2
        elif letter == 'B':
            ll += (ul - ll + 1) / 2

    # assign row number
    # (-1 because seats are 0-indexed)
    row = int(ll) - 1

    ll, ul = 1, 8
    for letter in seat[-3:]:
        if letter == 'L':
            ul -= (ul - ll + 1) / 2
        elif letter == 'R':
            ll += (ul - ll + 1) / 2
    # assign column number
    # (-1 because seats are 0-indexed)
    col = int(ll) - 1
    seat_dict[row * 8 + col] = (row, col)

highest_seat_id = max(seat_dict.keys())
print("Part 1")
print("Highest seat ID on a boarding pass: {}\n".format(highest_seat_id))

# Part 2
required_seat_id = 0
SEAT_ID_LIST = list(seat_dict.keys())
SEAT_ID_LIST.sort()
for idx in range(0, len(SEAT_ID_LIST) - 1):
    if SEAT_ID_LIST[idx + 1] == SEAT_ID_LIST[idx] + 2:
        required_seat_id = SEAT_ID_LIST[idx] + 1
        break

print("Part 2")
if required_seat_id:
    print("Required seat ID: {}".format(required_seat_id))
else:
    print("Required seat ID not found.")
print(SEAT_ID_LIST)
