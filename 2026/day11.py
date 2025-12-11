import sys


def visit(
    map: dict[str, list[str]],
    start: str,
    dac: bool,
    fft: bool,
    cache: dict[tuple[str, bool, bool], int],
) -> int:
    key = (start, dac, fft)
    if key in cache:
        return cache[key]

    if start == "out":
        cache[key] = 1 if dac and fft else 0
        return cache[key]

    dac |= start == "dac"
    fft |= start == "fft"

    count = 0
    for entry in map[start]:
        count += visit(map, entry, dac, fft, cache)

    cache[key] = count
    return count


def part_1(devices: dict[str, list[str]]):
    return visit(devices, "you", True, True, {})


def part_2(devices: dict[str, list[str]]):
    return visit(devices, "svr", False, False, {})


def main():
    filepath = sys.argv[1]

    f = open(filepath)

    input = f.readlines()

    devices: dict[str, list[str]] = {}
    for line in input:
        [orig, out] = line.split(":")
        devices[orig] = out.strip().split(" ")

    print("Part_1:", part_1(devices))

    if "example" in filepath:
        filepath_split = filepath.split(".")

        filepath = filepath_split[0] + "_2." + filepath_split[1]

        f = open(filepath)

        input = f.readlines()

        devices = {}
        for line in input:
            [orig, out] = line.split(":")
            devices[orig] = out.strip().split(" ")

    print("Part_2:", part_2(devices))


if __name__ == "__main__":
    main()
