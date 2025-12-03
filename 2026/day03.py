import sys


def count_voltage(banks: list[list[int]], active_size: int) -> int:
    total: int = 0
    for bank in banks:
        active: list[int] = [0] * active_size
        for i, bat in enumerate(bank):
            for j, a in enumerate(active):
                if bat > a and active_size - j < len(bank) - i + 1:
                    active[j] = bat
                    for k in range(j + 1, len(active)):
                        active[k] = 0
                    break

        for i, val in enumerate(active):
            total += (10 ** (active_size - i - 1)) * val

    return total


def part_1(banks: list[list[int]]):
    return count_voltage(banks, 2)


def part_2(banks: list[list[int]]):
    return count_voltage(banks, 12)


def main():
    filepath = sys.argv[1]

    f = open(filepath)

    input = f.readlines()

    input = [list(map(int, s.replace("\n", ""))) for s in input]

    print("Part_1:", part_1(input))
    print("Part_2:", part_2(input))


if __name__ == "__main__":
    main()
