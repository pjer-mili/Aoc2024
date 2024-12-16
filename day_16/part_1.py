import heapq


def main():
    with open("input.txt", "r") as file:
        maze = file.read().strip().split("\n")
    start, end = get_positions(maze)
    cost, came_from = find_shortest_path(start, end, maze)
    print(cost)


def find_shortest_path(start, end, maze):
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]  # right, down, up, left
    initial_facing = directions[0]

    frontier = [(0, start, initial_facing)]
    heapq.heapify(frontier)
    came_from: dict[tuple, tuple | None] = {}
    cost_so_far: dict[tuple, int] = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while frontier:
        current, facing = heapq.heappop(frontier)[1:]
        if current == end:
            break

        for direction in directions:
            dx, dy = direction
            n_i, n_j = current[0] + dx, current[1] + dy
            if maze[n_i][n_j] == "#":
                continue
            new_cost = get_cost(facing, direction) + cost_so_far[current]
            next = (n_i, n_j)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                heapq.heappush(frontier, (new_cost, next, direction))
                came_from[next] = current
    return (cost_so_far[end], came_from)


def get_cost(facing, next_direction):
    if facing != next_direction:
        return 1001
    return 1


def get_positions(maze):
    start = None
    end = None
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "E":
                end = (i, j)
            if maze[i][j] == "S":
                start = (i, j)
    if start is None or end is None:
        raise ValueError("Start or end missing")
    return (start, end)


def print_maze(maze):
    for row in maze:
        print("".join(row))


if __name__ == "__main__":
    main()
