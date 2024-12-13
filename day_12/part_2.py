def main():
    with open("input.txt", "r") as file:
        matrix = file.read().strip().split("\n")
    dfs(matrix)


def dfs(matrix: list[list[str]]):
    n = len(matrix)
    m = len(matrix[0])

    visited = set()

    def in_range(i, j):
        return 0 <= i < n and 0 <= j < m

    def get_corners(i, j):
        t = []

        for dx in range(-1, 2):
            row = []
            for dy in range(-1, 2):
                if in_range(i + dx, j + dy):
                    row.append(matrix[i + dx][j + dy])
                else:
                    row.append(".")
            t.append("".join(row))

        if is_surrounded(1, 1, t):
            return 4

        count = set()
        for k in range(4):
            if is_outside_corner(1, 1, t) or is_inside_corner(1, 1, t):
                count.add(k)

            t = rotate_matrix(t)

        return len(count)

    def rotate_matrix(matrix):
        matrix = [list(row) for row in zip(*matrix)]
        matrix.reverse()
        return matrix

    def is_outside_corner(i, j, rotated):
        return rotated[i - 1][j] != rotated[i][j] and rotated[i][j - 1] != rotated[i][j]

    def is_inside_corner(i, j, rotated):
        return (
            rotated[i][j - 1] == rotated[i - 1][j]
            and rotated[i - 1][j - 1] != rotated[i][j]
        )

    def is_surrounded(i, j, rotated):
        return (
            rotated[i - 1][j] != rotated[i][j]
            and rotated[i][j - 1] != rotated[i][j]
            and rotated[i + 1][j] != rotated[i][j]
            and rotated[i][j + 1] != rotated[i][j]
        )

    def dfs_util(i, j, area, corners):
        visited.add((i, j))
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        area = 1

        corners = get_corners(i, j)

        for dx, dy in directions:
            n_i, n_j = i + dx, j + dy
            if in_range(n_i, n_j) and matrix[n_i][n_j] == matrix[i][j]:
                if (n_i, n_j) not in visited:
                    sub_area, sub_perimiter = dfs_util(n_i, n_j, area + 1, corners)
                    area += sub_area
                    corners += sub_perimiter
        return area, corners

    result_dict = {}

    for i in range(n):
        for j in range(m):
            if (i, j) not in visited:
                area, side = dfs_util(i, j, 0, 0)
                if (matrix[i][j], (i, j)) not in result_dict:
                    result_dict[(matrix[i][j], (i, j))] = [0, 0]
                result_dict[(matrix[i][j], (i, j))][0] += area
                result_dict[(matrix[i][j], (i, j))][1] += side

    result = 0
    for area, sides in result_dict.values():
        result += area * sides

    print(result)


if __name__ == "__main__":
    main()
