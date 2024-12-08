from collections import defaultdict
from itertools import combinations


def main():
    with open("input.txt", "r") as file:
        matrix = file.read().strip().split("\n")

    pairs_dict = generate_pairs(matrix)
    antinodes_set = set()
    for pairs_array in pairs_dict.values():
        for pair in pairs_array:
            get_possible_antinodes(pair, len(matrix), len(matrix[0]), antinodes_set)
    print(len(antinodes_set))


def get_possible_antinodes(
    pair: tuple[tuple[int, int], tuple[int, int]], n, m, antinodes_set: set
):
    a, b = pair
    calculate_coord(a, b, n, m, antinodes_set)
    calculate_coord(b, a, n, m, antinodes_set)


def calculate_coord(a: tuple[int, int], b: tuple[int, int], n, m, antinodes_set: set):
    x1, y1 = a
    x2, y2 = b

    new_x = x2 + (x2 - x1)
    new_y = y2 + (y2 - y1)
    antinodes_set.add((x2, y2))

    while in_bounds(new_x, new_y, n, m):
        antinodes_set.add((new_x, new_y))
        new_x += x2 - x1
        new_y += y2 - y1


def in_bounds(i, j, n, m):
    return 0 <= i < n and 0 <= j < m


def generate_pairs(
    matrix: list[list[str]],
) -> dict[str, list[tuple[tuple[int, int], tuple[int, int]]]]:
    result = defaultdict(list)

    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value != ".":
                result[value].append((i, j))

    pairs = {key: list(combinations(values, 2)) for key, values in result.items()}
    return pairs


if __name__ == "__main__":
    main()
