def main():
    try:
        arr1, arr2 = transform_input("./input.txt")
        arr1.sort()
        arr2.sort()

        total_difference = sum(abs(a - b) for a, b in zip(arr1, arr2))
        print(total_difference)
    except Exception as e:
        print(f"An error occurred: {e}")


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
