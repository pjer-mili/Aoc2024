import math


def main():
    with open("./input.txt", "r") as lines:
        equations = lines.read().strip().split("\n")

    sum = 0
    for equation in equations:
        result, numbers = deserialize_equation(equation)
        if is_solvable(result, numbers):
            sum += result
    print(sum)


def digits(x):
    return int(math.log10(x)) + 1


def ends_with(a, b):
    return (a - b) % 10 ** digits(b) == 0


def deserialize_equation(equation: str):
    split_equasion = equation.split(":")
    return int(split_equasion[0]), [int(num) for num in split_equasion[1].split()]


def is_solvable(result: str, numbers: list[str]) -> bool:
    *rest, x = numbers
    if not rest:
        return x == result

    q, r = divmod(result, x)
    if r == 0 and is_solvable(q, rest):
        return True

    if ends_with(result, x) and is_solvable(result // (10 ** digits(x)), rest):
        return True

    if result - x > 0 and is_solvable(result - x, rest):
        return True

    return False


if __name__ == "__main__":
    main()
