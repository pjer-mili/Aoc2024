def main():
    # Read input file
    with open("./input.txt", "r") as file:
        data = file.read().strip().split("\n")

    n, m = len(data), len(data[0])
    i, j = find_start(data, n, m)

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir_index = 0
    visited_positions = set()

    while True:
        visited_positions.add((i, j))
        next_i, next_j = i + directions[dir_index][0], j + directions[dir_index][1]

        if not in_bounds(next_i, next_j, n, m):
            break

        while data[next_i][next_j] == "#":
            dir_index = (dir_index + 1) % 4
            next_i, next_j = i + directions[dir_index][0], j + directions[dir_index][1]

        i, j = next_i, next_j

    print(len(visited_positions))


def in_bounds(i, j, n, m):
    return 0 <= i < n and 0 <= j < m


def find_start(data: list[list[str]], n, m) -> tuple:
    for i in range(n):
        for j in range(m):
            if data[i][j] == "^":
                return i, j
    raise ValueError("No starting position found")


if __name__ == "__main__":
    main()
