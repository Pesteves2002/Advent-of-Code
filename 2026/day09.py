import sys

import shapely


def calculate_area(e1: tuple[int, int], e2: tuple[int, int]) -> int:
    x = max(e2[0] - e1[0], e1[0] - e2[0]) + 1
    y = max(e2[1] - e1[1], e1[1] - e2[1]) + 1
    return x * y


def part_1(tiles: list[tuple[int, int]]):
    area = 0
    for e1 in tiles:
        for e2 in tiles:
            a = calculate_area(e1, e2)
            if a > area:
                area = a

    return area


def part_2(tiles: list[tuple[int, int]]):
    poligon = shapely.Polygon(tiles)

    area = 0
    for e1 in tiles:
        for e2 in tiles:
            x1, y1 = e1
            x2, y2 = e2

            minx, maxx = sorted([x1, x2])
            miny, maxy = sorted([y1, y2])

            rect = shapely.Polygon(
                [(minx, miny), (minx, maxy), (maxx, maxy), (maxx, miny)]
            )

            a = calculate_area(e1, e2)
            if a > area and poligon.contains(rect):
                area = a

    return area


def main():
    filepath = sys.argv[1]

    f = open(filepath)

    input = f.readlines()

    tiles: list[tuple[int, int]] = []

    for line in input:
        values = list(map(int, line.replace("\n", "").split(",")))
        tiles.append((values[0], values[1]))

    print("Part_1:", part_1(tiles))
    print("Part_2:", part_2(tiles))


if __name__ == "__main__":
    main()
