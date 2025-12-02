import sys


def part_1(start: int, window_size: int, actions: list[str]):
    count = 0
    pointer = start
    for action in actions:
        dir = action[0]
        num = int(action[1:-1])

        if dir == "L":
            pointer = (pointer - num) % window_size

        if dir == "R":
            pointer = (pointer + num) % window_size

        if pointer == 0:
            count += 1

    return count


def part_2(start:int , window_size: int, actions: list[str]):
    count = 0
    pointer = start
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

    return count

def main():

    filepath = sys.argv[1]

    f = open(filepath)

    actions = f.readlines()

    start = 50
    window_size = 100

    print("Part_1:", part_1(start, window_size, actions))
    print("Part_2:", part_2(start, window_size, actions))

if __name__ == "__main__":
    main()
