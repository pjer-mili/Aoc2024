from heapq import heapify, heappop, heappush


def main():
    # (X, Y) -> (j ,i)

    with open("input.txt", "r") as file:
        positions = file.read().strip().split("\n")
    corrupted = get_corrupted_spaces(positions)
    grid = create_grid(corrupted, 1024, 70)
    start, end = (0, 0), (70, 70)
    cost = find_shorest_path(start, end, grid)
    print(cost)


def create_grid(corrupted: list[tuple[int, int]], corrupted_num, n):  # n + 1 positions
    grid = []
    subset = corrupted[:corrupted_num]
    for i in range(n + 1):
        row = []
        for j in range(n + 1):
            if (i, j) in subset:
                row.append("#")
            else:
                row.append(".")
        grid.append(row)
    return grid


def in_bounds(i, j, grid):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])


def print_grid(grid):
    for row in grid:
        print("".join(row))


def get_corrupted_spaces(positions_str: list[str]):
    return list(
        map(
            lambda pos_str: (int(pos_str.split(",")[1]), (int(pos_str.split(",")[0]))),
            positions_str,
        )
    )


def find_shorest_path(start, end, grid):
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    frontier = [(0, start)]
    heapify(frontier)

    cost_so_far: dict[tuple, int] = {}
    cost_so_far[start] = 0

    while frontier:
        popped = heappop(frontier)
        cost, current = popped

        if current == end:
            break

        for direction in directions:
            dx, dy = direction
            n_i, n_j = current[0] + dx, current[1] + dy

            if not in_bounds(n_i, n_j, grid):
                continue

            if grid[n_i][n_j] == "#":
                continue

            new_cost = cost + 1
            next = (n_i, n_j)

            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                heappush(frontier, (new_cost, next))

    return cost_so_far[end]


if __name__ == "__main__":
    main()
