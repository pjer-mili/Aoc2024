def main():
    with open("input.txt", "r") as file:
        data = list(map(int, file.read().strip().split("\n")[0].split(" ")))
    sum = 0
    for stone in data:
        sum += calculate_with_depth(stone, 25)
    print(sum)


def calculate_single(value: int):
    digit_num = len(str(value))

    if value == 0:
        return (1, None)
    elif digit_num % 2 == 0:
        middle = digit_num // 2
        tens = 10**middle
        left = value // tens
        right = value % tens

        return (left, right)
    else:
        return (value * 2024, None)


def calculate_with_depth(value, depth):
    left, right = calculate_single(value)
    if depth == 1:
        if right is None:
            return 1
        else:
            return 2

    else:
        count = calculate_with_depth(left, depth - 1)

        if right is not None:
            count += calculate_with_depth(right, depth - 1)

        return count


if __name__ == "__main__":
    main()
