def main():
    with open("./input.txt") as file:
        data = file.read().strip().split("\n")
    n = len(data)
    m = len(data[0])
    directions = generate_directions()

    count = 0
    for i in range(n):
        for j in range(m):
            if data[i][j] == "X":
                for direction in directions:
                    count += has_xmas(i, j, direction, n, m, data)

    print(count)


def generate_directions():
    directions = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0):
                directions.append((i, j))
    return directions


def has_xmas(i, j, direction, n, m, data) -> bool:
    dx, dy = direction

    for z, c in enumerate("XMAS"):
        next_i = i + z * dx
        next_j = j + z * dy
        if not (0 <= next_i < n and 0 <= next_j < m):
            return 0
        if data[next_i][next_j] != c:
            return 0
    return 1


if __name__ == "__main__":
    main()
