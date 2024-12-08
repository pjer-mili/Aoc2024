from collections import defaultdict
from itertools import combinations


def main():
    with open("test_input.txt", "r") as file:
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
    origin_a, origin_b = pair

    a, b = origin_a, origin_b

    c, found_1 = calculate_coord(a, b, n, m)
    if found_1:
        antinodes_set.add(c)

    d, found_2 = calculate_coord(b, a, n, m)
    if found_2:
        antinodes_set.add(d)


def calculate_coord(a: tuple[int, int], b: tuple[int, int], n, m):
    x1, y1 = a
    x2, y2 = b

    new_x = x2 + (x2 - x1)
    new_y = y2 + (y2 - y1)
    if in_bounds(new_x, new_y, n, m):
        return (new_x, new_y), True

    return {}, False


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
