import sys


def visit(x: int, tachyons: list[list[int]]) -> int:
    beams = {x}

    count = 0
    for bif in tachyons:
        next_beams: set[int] = set()

        for beam in beams:
            if beam in bif:
                next_beams.add(beam - 1)
                next_beams.add(beam + 1)

                count += 1
            else:
                next_beams.add(beam)

        beams = next_beams

    return count


def visit_quantum(x: int, tachyons: list[list[int]]) -> int:
    beams = {x: 1}

    for bif in tachyons:
        next_beams: dict[int, int] = {}
        for beam, count in beams.items():
            if beam in bif:
                next_beams[beam - 1] = next_beams.get(beam - 1, 0) + count
                next_beams[beam + 1] = next_beams.get(beam + 1, 0) + count
            else:
                next_beams[beam] = next_beams.get(beam, 0) + count

        beams = next_beams

    return sum(beams.values())


def part_1(start: int, tachyons: list[list[int]]) -> int:
    return visit(start, tachyons)


def part_2(start: int, tachyons: list[list[int]]) -> int:
    return visit_quantum(start, tachyons)


def main():
    filepath = sys.argv[1]

    f = open(filepath)

    input = f.readlines()

    start = input[0].find("S")

    tachyons: list[list[int]] = []
    for i, line in enumerate(input):
        if i == 0:
            continue

        t: list[int] = []
        for j, c in enumerate(line):
            if c == "^":
                t.append(j)

        # Ignore empty tachyon lines
        if t:
            tachyons.append(t)

    print("Part_1:", part_1(start, tachyons))
    print("Part_2:", part_2(start, tachyons))


if __name__ == "__main__":
    main()
