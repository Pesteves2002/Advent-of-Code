import sys


def calculate(numbers: list[list[int]], operations: list[str]):
    sum = 0
    for column in range(len(numbers)):
        op = operations[column]
        val = 1 if op == "*" else 0
        for entry in numbers[column]:
            if op == "*":
                val *= entry
            else:
                val += entry
        sum += val

    return sum


def part_1(input: list[str]):
    numbers: list[list[int]] = []
    operations: list[str] = []

    for line in input:
        old = ""
        new = line.strip()
        while old != new:
            old = new
            new = new.replace("  ", " ")

        for i, entry in enumerate(new.split(" ")):
            if entry == "*" or entry == "+":
                operations.append(entry)

            else:
                if i >= len(numbers):
                    numbers.append([])

                numbers[i].append(int(entry))

    return calculate(numbers, operations)


def part_2(input: list[str]):
    operations: list[str] = []

    group: list[str] = []
    for line in input:
        new = line.replace("\n", "").replace(" ", "0")

        if "*" in new:
            operations = [c for c in new.replace("0", "")]
        else:
            group.append(new)

    numbers: list[list[int]] = []
    temp: list[int] = []
    for x in range(len(group[0])):
        sum = 0
        for y in range(len(group)):
            val = int(group[y][x])

            if val != 0:
                sum = sum * 10 + val

        if sum == 0:
            numbers.append(temp)
            temp = []
        else:
            temp.append(sum)

    numbers.append(temp)

    return calculate(numbers, operations)


def main():
    filepath = sys.argv[1]

    f = open(filepath)

    input = f.readlines()

    print("Part_1:", part_1(input))
    print("Part_2:", part_2(input))


if __name__ == "__main__":
    main()
