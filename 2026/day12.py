import sys


def get_next_to_wrap(to_wrap: list[int]) -> int:
    for i, v in enumerate(to_wrap):
        if v == 0:
            continue
        return i

    print("Should not go here")
    exit(1)


def flip_x(matrix: list[list[int]]) -> list[list[int]]:
    return matrix[::-1]


def flip_y(matrix: list[list[int]]) -> list[list[int]]:
    return [row[::-1] for row in matrix]


def flip_xy(matrix: list[list[int]]) -> list[list[int]]:
    return [row[::-1] for row in matrix[::-1]]


def rotate_90(matrix: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*matrix[::-1])]


def rotate_180(matrix: list[list[int]]) -> list[list[int]]:
    return [row[::-1] for row in matrix[::-1]]


def rotate_270(matrix: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*matrix)][::-1]


def all_orientations(matrix: list[list[int]]) -> list[list[list[int]]]:
    mats: list[list[list[int]]] = []

    r0 = matrix
    r90 = rotate_90(matrix)
    r180 = rotate_180(matrix)
    r270 = rotate_270(matrix)

    f0 = flip_x(matrix)
    f1 = flip_y(matrix)
    f2 = flip_x(r90)
    f3 = flip_y(r90)

    for m in [r0, r90, r180, r270, f0, f1, f2, f3]:
        if m not in mats:
            mats.append(m)

    return mats


def fits(present: list[list[int]], box: list[list[int]], y: int, x: int) -> bool:
    for dy in range(3):
        for dx in range(3):
            if present[dy][dx] == 1 and box[y + dy][x + dx] != 0:
                return False
    return True


def place(present: list[list[int]], box: list[list[int]], y: int, x: int):
    for dy in range(3):
        for dx in range(3):
            if present[dy][dx] == 1:
                box[y + dy][x + dx] = 1


def unplace(present: list[list[int]], box: list[list[int]], y: int, x: int):
    for dy in range(3):
        for dx in range(3):
            if present[dy][dx] == 1:
                box[y + dy][x + dx] = 0


def visit(
    presents: dict[int, list[list[list[int]]]],
    box_matrix: list[list[int]],
    to_wrap: list[int],
    min_size: int,
) -> bool:
    if sum(to_wrap) == 0:
        return True

    index = get_next_to_wrap(to_wrap)

    for orient in presents[index]:
        y_len = len(box_matrix)
        x_len = len(box_matrix[0])

        for y in range(y_len - 2):
            for x in range(x_len - 2):
                full_cells = (
                    box_matrix[y][x]
                    + box_matrix[y][x + 1]
                    + box_matrix[y][x + 2]
                    + box_matrix[y + 1][x]
                    + box_matrix[y + 1][x + 1]
                    + box_matrix[y + 1][x + 2]
                    + box_matrix[y + 2][x]
                    + box_matrix[y + 2][x + 1]
                    + box_matrix[y + 2][x + 2]
                )

                if 9 - full_cells < min_size:
                    continue

                if fits(orient, box_matrix, y, x):
                    place(orient, box_matrix, y, x)
                    to_wrap[index] -= 1

                    if visit(presents, box_matrix, to_wrap, min_size):
                        return True

                    unplace(orient, box_matrix, y, x)
                    to_wrap[index] += 1

    return False


def part_1(
    presents: list[list[list[int]]],
    boxes: list[tuple[tuple[int, int], list[int]]],
) -> int:
    count = 0

    presents_map: dict[int, list[list[list[int]]]] = {}
    presents_size = []
    min_size = sys.maxsize
    for i, present in enumerate(presents):
        presents_map[i] = all_orientations(present)
        p_size = sum([c for row in present for c in row])
        min_size = min(min_size, p_size)
        presents_size.append(p_size)

    for box in boxes:
        x_len = box[0][0]
        y_len = box[0][1]

        box_matrix = [[0 for _ in range(x_len)] for _ in range(y_len)]

        to_wrap = box[1]

        if x_len * y_len < sum(
            count * size for count, size in zip(presents_size, to_wrap)
        ):
            continue

        count += 1 if visit(presents_map, box_matrix, to_wrap, min_size) else 0

    return count


def part_2(banks: list[list[int]]):
    return -1


def main():
    filepath = sys.argv[1]

    f = open(filepath)

    input = f.readlines()

    presents: list[list[list[int]]] = []
    boxes: list[tuple[tuple[int, int], list[int]]] = []

    present: list[list[int]] = []
    for line in input:
        if len(line) == 1:
            presents.append(present)
            present = []
            continue

        if "#" in line or "." in line:
            present.append([1 if c == "#" else 0 for c in line.strip()])
            continue

        if len(line) == 3:
            continue

        line = line.replace("x", " ").replace(":", "").split(" ")
        boxes.append(((int(line[0]), int(line[1])), [int(c) for c in line[2:]]))

    print("Part_1:", part_1(presents, boxes))
    # print("Part_2:", part_2(input))


if __name__ == "__main__":
    main()
