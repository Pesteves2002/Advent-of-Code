import sys

filepath = sys.argv[1]

f = open(filepath)

part_2 = len(sys.argv) >= 3

actions = f.readlines()

pointer = 50
window_size = 100

count = 0
for action in actions:
    dir = action[0]
    num = int(action[1:-1])

    if dir == "L":
        if (pointer - num) < 0:
            count += abs((window_size + pointer - num) // window_size)
            if pointer != 0:
                count += 1

        pointer = (pointer - num) % window_size

        if pointer == 0:
            count += 1

    if dir == "R":
        count += (pointer + num) // window_size
        pointer = (pointer + num) % window_size

print("count:", count)
