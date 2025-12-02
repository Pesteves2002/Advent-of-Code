import sys


def part_1(ids: list[list[int]]):
    sum = 0

    for id in ids:
        start = id[0]
        end = id[1]

        for i in range(start, end + 1):
            i_str = str(i)

            firstpart, secondpart = i_str[: len(i_str) // 2], i_str[len(i_str) // 2 :]

            if firstpart == secondpart:
                sum += i

    return sum


def part_2(ids: list[list[int]]):
    sum = 0

    for id in ids:
        start = id[0]
        end = id[1]

        for i in range(start, end + 1):
            i_str = str(i)

            for p in range(1, (len(i_str) // 2) + 1):
                sub_str = i_str[:p]

                if i_str.replace(sub_str, '') == '':
                    sum += i
                    break

    return sum


def main():
    filepath = sys.argv[1]

    f = open(filepath)

    input = f.readline().replace("\n", "").split(",")

    input = [list(map(int, s.split("-"))) for s in input]

    print("Part_1:", part_1(input))
    print("Part_2:", part_2(input))


if __name__ == "__main__":
    main()
