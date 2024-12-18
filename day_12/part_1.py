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

    def dfs_util(i, j, area, perimiter):
        visited.add((i, j))
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        area = 1
        perimiter = 4

        for dx, dy in directions:
            n_i, n_j = i + dx, j + dy
            if in_range(n_i, n_j) and matrix[n_i][n_j] == matrix[i][j]:
                perimiter -= 1
                if (n_i, n_j) not in visited:
                    sub_area, sub_perimiter = dfs_util(n_i, n_j, area + 1, perimiter)
                    area += sub_area
                    perimiter += sub_perimiter
        return area, perimiter

    result_dict = {}

    for i in range(n):
        for j in range(m):
            if (i, j) not in visited:
                area, perimiter = dfs_util(i, j, 0, 0)
                if (matrix[i][j], (i, j)) not in result_dict:
                    result_dict[(matrix[i][j], (i, j))] = [0, 0]
                result_dict[(matrix[i][j], (i, j))][0] += area
                result_dict[(matrix[i][j], (i, j))][1] += perimiter

    result = 0
    for key, value in result_dict.items():
        result += value[0] * value[1]
    print(result)


if __name__ == "__main__":
    main()
