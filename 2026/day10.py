import sys
import pulp


def part_1(machines: list[tuple[set[int], list[set[int]], list[int]]]):
    count = 0

    for i, (lights, buttons, _) in enumerate(machines):
        states = buttons
        iteration = 2

        finished = False
        for s in states:
            if s == lights:
                count += 1
                finished = True
                break

        if finished:
            continue

        while True:
            new_states: list[set[int]] = []
            finished = False

            for s in states:
                for b in buttons:
                    new_state = s.copy()

                    for d in b:
                        if d in new_state:
                            new_state.remove(d)
                        else:
                            new_state.add(d)

                    if new_state == lights:
                        finished = True
                        break

                    new_states.append(new_state)

                if finished:
                    break

            if finished:
                break

            states = new_states
            iteration += 1

        count += iteration

    return count


def part_2(machines: list[tuple[set[int], list[set[int]], list[int]]]):
    total_count = 0

    for i, (_, buttons, joltages) in enumerate(machines):
        prob = pulp.LpProblem(f"Machine_{i}", pulp.LpMinimize)

        x = [
            pulp.LpVariable(f"x_{j}", lowBound=0, cat="Integer")
            for j in range(len(buttons))
        ]

        prob += pulp.lpSum(x)

        for pos in range(len(joltages)):
            prob += (
                pulp.lpSum(x[j] for j, b in enumerate(buttons) if pos in b)
                == joltages[pos]
            )

        prob.solve(pulp.PULP_CBC_CMD(msg=False))

        if prob.status != pulp.LpStatusOptimal:
            raise ValueError(f"No solution found for machine {i}")

        total_count += sum(var.varValue for var in x)

    return int(total_count)


def main():
    filepath = sys.argv[1]

    f = open(filepath)

    input = f.readlines()

    machines: list[tuple[set[int], list[set[int]], list[int]]] = []
    for line in input:
        elems = line.strip().split(" ")

        lights = elems.pop(0)
        lights_on = {i - 1 for i, c in enumerate(lights) if c == "#"}

        joltages = elems.pop()[1:-1]
        joltages = [int(s) for s in joltages.split(",")]

        buttons = [{int(x) for x in b[1:-1].split(",")} for b in elems]

        machines.append((lights_on, buttons, joltages))

    print("Part_1:", part_1(machines))
    print("Part_2:", part_2(machines))


if __name__ == "__main__":
    main()
