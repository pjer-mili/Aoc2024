def main():
    with open("./input.txt") as file:
        data = file.read().strip().split("\n")
    n = len(data)
    m = len(data[0])

    count = 0
    for i in range(n):
        for j in range(m):
            if data[i][j] == "A":
                count += has_xmas(i, j, n, m, data)

    print(count)


def has_xmas(i, j, n, m, data) -> bool:
    if not in_range(i, j, n, m):
        return 0

    matches = ["MS", "SM"]

    diag_1 = f"{data[i-1][j-1]}{data[i+1][j+1]}"
    diag_2 = f"{data[i-1][j+1]}{data[i+1][j-1]}"

    if diag_1 in matches and diag_2 in matches:
        return 1

    return 0


def in_range(i, j, n, m):
    if 1 <= i < n - 1 and 1 <= j < m - 1:
        return True
    return False


if __name__ == "__main__":
    main()
