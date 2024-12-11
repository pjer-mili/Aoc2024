from collections import defaultdict


def main():
    with open("input.txt", "r") as file:
        data = list(map(int, file.read().strip().split("\n")[0].split(" ")))
    sum = 0
    cache = defaultdict(tuple)
    for stone in data:
        sum += calculate_with_depth(stone, 75, cache)
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


def calculate_with_depth(value, depth, cache):
    if (depth, value) in cache:
        return cache[(depth, value)]

    left, right = calculate_single(value)
    if depth == 1:
        result = 1 if right is None else 2
    else:
        result = calculate_with_depth(left, depth - 1, cache)

        if right is not None:
            result += calculate_with_depth(right, depth - 1, cache)

    cache[(depth, value)] = result
    return result


if __name__ == "__main__":
    main()
