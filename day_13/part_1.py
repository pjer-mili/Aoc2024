import re


class Machine:
    def __init__(self, A, B, result):
        self.A = A
        self.B = B
        self.result = result

    def __repr__(self):
        return f"A:{self.A}, B:{self.B}, result:{self.result}"

    def solve(self):
        ax, ay = self.A
        bx, by = self.B
        px, py = self.result

        solution_a, solution_b = None, None

        if (bx * py - by * px) / (bx * ay - by * ax) == (bx * py - by * px) // (
            bx * ay - by * ax
        ):
            solution_a = (bx * py - by * px) // (bx * ay - by * ax)

            if (py - solution_a * ay) / by == (py - solution_a * ay) // by:
                solution_b = (py - solution_a * ay) // by

        if solution_a is not None and solution_b is not None:
            return solution_a * 3 + solution_b

        return 0


def parse_file(filename):
    machines = []

    with open(filename, "r") as file:
        blocks = file.read().strip().split("\n\n")

    for block in blocks:
        match = re.search(
            r"Button A: X\+(\d+), Y\+(\d+)\n"
            r"Button B: X\+(\d+), Y\+(\d+)\n"
            r"Prize: X=(\d+), Y=(\d+)",
            block,
        )
        if match:
            A = int(match.group(1)), int(match.group(2))
            B = int(match.group(3)), int(match.group(4))
            result = int(match.group(5)), int(match.group(6))
            machines.append(Machine(A, B, result))

    return machines


def main():
    filename = "input.txt"
    machines: list[Machine] = parse_file(filename)

    sum = 0
    for machine in machines:
        sum += machine.solve()
    print(sum)


if __name__ == "__main__":
    main()
