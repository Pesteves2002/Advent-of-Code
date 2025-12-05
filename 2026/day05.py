import sys


def part_1(ranges: list[tuple[int, int]], ids: list[int]):
    count = 0
    for id in ids:
        for range in ranges:
            if id >= range[0] and id <= range[1]:
                count += 1
                break

    return count


def union(a: int, b: int, c: int, d: int) -> tuple[int, int]:
    if b < c or d < a:
        return (-1, -1)

    return (min(a, c), max(b, d))


def part_2(ranges: list[tuple[int, int]]):
    ranges = sorted(ranges, key=lambda x: x[0])

    merged_ranges: list[tuple[int, int]] = [ranges[0]]

    for a, b in ranges:
        c, d = merged_ranges[-1]

        u = union(a, b, c, d)

        if u == (-1, -1):
            merged_ranges.append((a, b))
        else:
            merged_ranges[-1] = u

    count = 0
    for r in merged_ranges:
        count += r[1] - r[0] + 1

    return count


def main():
    filepath = sys.argv[1]

    f = open(filepath)

    input = f.readlines()

    ranges: list[tuple[int, int]] = []
    ids: list[int] = []

    for line in input:
        line = line.replace("\n", "")
        if line == "":
            continue

        if "-" in line:
            values = line.split("-")
            ranges.append((int(values[0]), int(values[1])))
        else:
            ids.append(int(line))

    print("Part_1:", part_1(ranges, ids))
    print("Part_2:", part_2(ranges))


if __name__ == "__main__":
    main()
