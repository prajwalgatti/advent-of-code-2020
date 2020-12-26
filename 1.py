# solution to day 1

# import requests
# import os.path
#
# url = 'https://adventofcode.com/2020/day/1/input'
#
# if not path.exists("input.txt"):
#    r = requests.get(url, allow_redirects=True)
#    open('input.txt', 'wb').write(r.content)

with open("input.txt", 'r') as f:
    data = [int(num) for num in f.read().splitlines()]

# Part 1

temp = set()
print("Part 1")
for num in data:
    if (2020 - num) in temp:
        print("num1: {}\nnum2: {}\nnum1*num2: {}\n".format(
              num, 2020 - num, num * (2020 - num)))
        break
    temp.add(num)
else:
    print("Pair not found")

# Part 2
# This problem is a subset sum problem where
# length of subset = 3... so it can be solved
# in a non-DP way. This soln has the time
# complexity of O(n^2)

n = len(data)
sum_val = 2020
data.sort()

print("Part 2")
for i in range(0, n - 2):
    j = i + 1
    k = n - 1
    target_val = sum_val - data[i]
    while(j < k):
        cur_val = data[j] + data[k]
        if cur_val == target_val:
            print("Found {}, {}, {}".format(data[i], data[j], data[k]))
            print("Ans: {}".format(data[i] * data[j] * data[k]))
            break
        elif cur_val < target_val:
            j = j + 1
        else:
            k = k - 1
