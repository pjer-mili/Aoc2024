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

    x1, y1 = a
    x2, y2 = b
    antinodes_count = 0

    c_x = x2 + (x2 - x1)
    c_y = y2 + (y2 - y1)
    if in_bounds(c_x, c_y, n, m):
        antinodes_set.add((c_x, c_y))

    d_x = x1 + (x1 - x2)
    d_y = y1 + (y1 - y2)
    if in_bounds(d_x, d_y, n, m):
        antinodes_set.add((d_x, d_y))

    return antinodes_count


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
