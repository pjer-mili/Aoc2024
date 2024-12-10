from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def get_graph(self):
        return dict(self.graph)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_util(self, v, result: dict, path: list, steps: int):
        new_path = path + [v[1]]

        if steps == 9 and v[0] == 9:
            result[tuple(new_path)] = new_path
            return

        for n in self.graph[v]:
            if n[0] == steps + 1:
                self.dfs_util(n, result, new_path, steps + 1)

    def dfs(self, v):
        result = {}
        self.dfs_util(v, result, [], 0)
        return result

    def create_graph(self, data: list[list[str]]):
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        n = len(data)
        m = len(data[0])
        for i in range(n):
            for j in range(m):
                for dir in directions:
                    n_i, n_j = i + dir[0], j + dir[1]
                    if self.in_bounds(n_i, n_j, n, m):
                        self.add_edge(
                            (int(data[i][j]), (i, j)), (int(data[n_i][n_j]), (n_i, n_j))
                        )

    def in_bounds(self, i, j, n, m):
        return 0 <= i < n and 0 <= j < m

    def sum_trailheads(self):
        sum = 0
        for v in self.graph:
            if v[0] == 0:
                score = self.dfs(v)
                sum += len(score)
        print(sum)


def main():
    with open("test_input.txt", "r") as file:
        data = file.read().strip().split("\n")

    graph = Graph()
    graph.create_graph(data)
    graph.sum_trailheads()


if __name__ == "__main__":
    main()
