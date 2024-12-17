import heapq
from collections import defaultdict
from itertools import chain


def main():
    with open("input.txt", "r") as file:
        maze = file.read().strip().split("\n")
    start, end = get_positions(maze)
    cost = find_shortest_path(start, end, maze)
    end_paths = get_end_paths(start, end, maze, cost)
    best_paths = set()

    for p in end_paths:
        best_paths.update(p)

    print(len(best_paths))


def get_end_paths(start, end, maze, cost_limit):
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]  # right, down, up, left
    initial_facing = directions[0]
    frontier = [(0, start, initial_facing, [start])]
    heapq.heapify(frontier)

    cost_so_far: defaultdict[tuple[tuple, tuple], int | float] = defaultdict(
        lambda: float("inf")
    )
    cost_so_far[(start, initial_facing)] = 0

    paths: defaultdict[tuple[tuple, tuple], list[tuple[tuple, ...]]] = defaultdict(list)
    paths[(start, initial_facing)].append((start,))

    while frontier:
        current_dist, current, facing, path = heapq.heappop(frontier)

        for direction in directions:
            next = (current[0] + direction[0], current[1] + direction[1])
            if maze[next[0]][next[1]] == "#":
                continue

            new_cost = current_dist + get_cost(facing, direction)
            known_cost = float("inf")

            if paths[(next, facing)]:
                known_cost = cost_so_far[(next, facing)]

            if new_cost < known_cost:
                paths[(next, facing)] = [(*path, next)]
                cost_so_far[(next, facing)] = new_cost
                if new_cost <= cost_limit:
                    heapq.heappush(frontier, (new_cost, next, direction, path + [next]))
            elif new_cost == known_cost:
                if new_cost <= cost_limit:
                    paths[(next, facing)].append((*path, next))
                    heapq.heappush(frontier, (new_cost, next, direction, path + [next]))

    return list(chain(*(paths[(end, d)] for d in directions)))


def find_shortest_path(start, end, maze):
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]  # right, down, up, left
    initial_facing = directions[0]

    frontier = [(0, start, initial_facing)]
    heapq.heapify(frontier)
    cost_so_far: dict[tuple, int] = {}
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
    return cost_so_far[end]


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
