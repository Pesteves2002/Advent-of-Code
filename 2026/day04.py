import sys


def print_grid(grid: list[list[int]]):
    for line in grid:
        disp = ""
        for elem in line:
            disp += "@" if elem == 1 else "."
        print(disp)


def roll_paper_locations(grid: list[int], x_size: int, y_size: int) -> list[int]:
    changed_pos: list[int] = []

    for y in range(1, y_size - 1):
        for x in range(1, x_size - 1):
            idx = y * x_size + x

            if grid[idx] == 0:
                continue

            s = (
                grid[idx - x_size - 1]
                + grid[idx - x_size]
                + grid[idx - x_size + 1]
                + grid[idx - 1]
                + grid[idx + 1]
                + grid[idx + x_size - 1]
                + grid[idx + x_size]
                + grid[idx + x_size + 1]
            )

            if s < 4:
                changed_pos.append(idx)

    return changed_pos


def part_1(grid: list[int], x_size: int, y_size: int):
    return len(roll_paper_locations(grid, x_size, y_size))


def part_2(grid: list[int], x_size: int, y_size: int):
    count = 0
    while True:
        roll_papers = roll_paper_locations(grid, x_size, y_size)
        num_roll_papers = len(roll_papers)
        if num_roll_papers == 0:
            break

        count += num_roll_papers
        for index in roll_papers:
            grid[index] = 0

    return count


def main():
    filepath = sys.argv[1]

    f = open(filepath)

    input = f.readlines()

    input = [list(s.replace("\n", "")) for s in input]
    input = [list(map(lambda c: 1 if c == "@" else 0, line)) for line in input]

    x_size = len(input[0])
    # add buffer in y direction
    input.insert(0, [0] * x_size)
    input.append([0] * x_size)

    # add buffer in x direction
    for line in input:
        line.insert(0, 0)
        line.append(0)

    input_flattened: list[int] = []
    for line in input:
        input_flattened.extend(line)

    x_size = len(input[0])
    y_size = len(input)

    print(
        "Part_1:",
        part_1(input_flattened, x_size, y_size),
    )
    print("Part_2:", part_2(input_flattened, x_size, y_size))


if __name__ == "__main__":
    main()
