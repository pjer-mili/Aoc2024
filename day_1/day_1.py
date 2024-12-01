from collections import defaultdict


def main():
    try:
        arr1, arr2 = transform_input("./input.txt")
        num_map = defaultdict(int)

        for num in arr2:
            num_map[num] += 1

        result = sum(num * num_map[num] for num in arr1 if num in num_map)

        print(result)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def transform_input(file: str) -> tuple[list[int], list[int]]:
    with open(file, "r") as txt:
        data = [line.split() for line in txt]

    if any(len(values) != 2 for values in data):
        raise ValueError("Each line must contain exactly two integers")

    try:
        arr1, arr2 = zip(*(map(int, values) for values in data))
    except ValueError:
        raise ValueError("File contains non-integer values")

    return list(arr1), list(arr2)


if __name__ == "__main__":
    main()
