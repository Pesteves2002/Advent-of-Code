import sys
from math import dist


def euclidean_distance(p: tuple[int, ...], q: tuple[int, ...]) -> float:
    return dist(p, q)


def part_1(junctions: list[tuple[int, ...]], num_connections: int):
    dist_matrix: list[list[float]] = []
    for y, q in enumerate(junctions):
        row: list[float] = []
        for p in junctions[y:]:
            dist = euclidean_distance(p, q)
            if dist == 0:
                dist = sys.maxsize
            row.append(dist)

        dist_matrix.append(row)

    circuits = [[j] for j in range(len(junctions))]

    num_conn = 0

    while num_conn < num_connections:
        min_dist = sys.maxsize
        coord_pair = (0, 0)

        for y, q in enumerate(dist_matrix):
            for x, dist in enumerate(q):
                if dist < min_dist:
                    min_dist = dist
                    coord_pair = (x, y)

        a = coord_pair[1]
        b = a + coord_pair[0]
        # print(a, b)

        orig = next(c for c in circuits if a in c)
        dest = next(c for c in circuits if b in c)

        i = min(a, b)
        j = max(a, b)

        r = i
        c = j - i

        dist_matrix[r][c] = sys.maxsize

        if orig != dest:
            dest.extend(orig)
            circuits.remove(orig)

        num_conn += 1

    circuits.sort(key=lambda e: len(e), reverse=True)

    res = 1
    for c in circuits[:3]:
        res *= len(c)

    return res


def part_2(junctions: list[tuple[int, ...]]):
    dist_matrix: list[list[float]] = []
    for y, q in enumerate(junctions):
        row: list[float] = []
        for p in junctions[y:]:
            dist = euclidean_distance(p, q)
            if dist == 0:
                dist = sys.maxsize
            row.append(dist)

        dist_matrix.append(row)

    circuits = [[j] for j in range(len(junctions))]

    last_connect: tuple[tuple[int, ...], ...] = ((0,0,0),(0,0,0))
    while len(circuits) > 1:
        min_dist = sys.maxsize
        coord_pair = (0, 0)

        for y, q in enumerate(dist_matrix):
            for x, dist in enumerate(q):
                if dist < min_dist:
                    min_dist = dist
                    coord_pair = (x, y)

        a = coord_pair[1]
        b = a + coord_pair[0]
        # print(a, b)

        orig = next(c for c in circuits if a in c)
        dest = next(c for c in circuits if b in c)

        i = min(a, b)
        j = max(a, b)

        r = i
        c = j - i

        dist_matrix[r][c] = sys.maxsize

        if orig != dest:
            dest.extend(orig)
            circuits.remove(orig)
            last_connect = (junctions[r], junctions[r + c])

    return last_connect[0][0] * last_connect[1][0]


def main():
    filepath = sys.argv[1]

    f = open(filepath)

    input = f.readlines()

    junctions = [list(map(int, s.replace("\n", "").split(","))) for s in input]

    junctions = [tuple(j[:3]) for j in junctions]

    num_connections = 1000 if "real" in filepath else 10

    print("Part_1:", part_1(junctions, num_connections))
    print("Part_2:", part_2(junctions))


if __name__ == "__main__":
    main()
