import sys
from math import dist


def euclidean_distance(p: tuple[int, ...], q: tuple[int, ...]) -> float:
    return dist(p, q)


def part_1(junctions: list[tuple[int, ...]], num_connections: int):
    dist_vector: list[tuple[int, int, float]] = []
    for y, q in enumerate(junctions):
        for x, p in enumerate(junctions[(y + 1) :], start=y + 1):
            dist = euclidean_distance(p, q)
            dist_vector.append((x, y, dist))

    dist_vector.sort(key=lambda e: e[2])

    circuits = [[j] for j in range(len(junctions))]

    for _ in range(num_connections):
        t = dist_vector[0]

        x = t[0]
        y = t[1]

        orig = next(c for c in circuits if x in c)
        dest = next(c for c in circuits if y in c)

        _ = dist_vector.pop(0)

        if orig != dest:
            dest.extend(orig)
            circuits.remove(orig)

    circuits.sort(key=lambda e: len(e), reverse=True)

    res = 1
    for c in circuits[:3]:
        res *= len(c)

    return res


def part_2(junctions: list[tuple[int, ...]]):
    dist_vector: list[tuple[int, int, float]] = []

    for y, q in enumerate(junctions):
        for x, p in enumerate(junctions[(y + 1) :], start=y + 1):
            dist = euclidean_distance(p, q)
            dist_vector.append((x, y, dist))

    dist_vector.sort(key=lambda e: e[2])

    circuits = [[j] for j in range(len(junctions))]

    last_connect: tuple[int, int, float] = (0, 0, 0)
    while len(circuits) > 1:
        t = dist_vector[0]

        x = t[0]
        y = t[1]

        orig = next(c for c in circuits if x in c)
        dest = next(c for c in circuits if y in c)

        _ = dist_vector.pop(0)

        if orig != dest:
            dest.extend(orig)
            circuits.remove(orig)
            last_connect = t

    return junctions[last_connect[0]][0] * junctions[last_connect[1]][0]


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
