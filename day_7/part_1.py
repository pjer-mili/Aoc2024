def main():
    with open("./input.txt", "r") as lines:
        equations = lines.read().strip().split("\n")

    sum = 0
    for equation in equations:
        result, numbers = deserialize_equation(equation)
        if is_solvable(result, numbers):
            sum += result
    print(sum)


def deserialize_equation(equation: str):
    split_equasion = equation.split(":")
    return int(split_equasion[0]), [int(num) for num in split_equasion[1].split()]


def is_solvable(result: str, numbers: list[str]):
    return is_solvable_rec(result, numbers, numbers[0], 0)


def is_solvable_rec(result, numbers, current_value, current_index):
    next_index = current_index + 1

    if current_value >= result and len(numbers) < next_index:
        return False

    if len(numbers) == next_index:
        if current_value == result:
            return True
        else:
            return False

    if is_solvable_rec(
        result, numbers, current_value + numbers[next_index], next_index
    ):
        return True

    if is_solvable_rec(
        result, numbers, current_value * numbers[next_index], next_index
    ):
        return True

    return False


if __name__ == "__main__":
    main()
