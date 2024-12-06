def main():
    with open("./input.txt", "r") as file:
        lab = file.read().strip().split("\n")
    n, m = len(lab), len(lab[0])
    start_i, start_j = find_start(lab, n, m)

    visited_positions = calculate_guard_path(lab, start_i, start_j, n, m)
    visited_positions.remove((start_i, start_j))
    loop_count = 0

    for candidate in visited_positions:
        obsticle_i, obsticle_j = candidate
        new_lab = create_copy_with_new_obsticle(lab, obsticle_i, obsticle_j, n, m)
        if calculate_guard_path(new_lab, start_i, start_j, n, m)[1]:
            loop_count += 1
    print(loop_count)


def calculate_guard_path(lab, start_i, start_j, n, m):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir_index = 0
    visited_positions = set()
    visited_cycle = set()

    i, j = start_i, start_j
    loop = False
    while True:
        if is_loop(visited_cycle, i, j, dir_index):
            loop = True
            break

        visited_cycle.add(f"[{dir_index}]({i},{j})")
        visited_positions.add((i, j))

        next_i, next_j = i + directions[dir_index][0], j + directions[dir_index][1]

        if not in_bounds(next_i, next_j, n, m):
            break

        while lab[next_i][next_j] == "#":
            dir_index = (dir_index + 1) % 4
            next_i, next_j = i + directions[dir_index][0], j + directions[dir_index][1]

        i, j = next_i, next_j

    return visited_positions, loop


def is_loop(cycle, i, j, dir_index):
    if f"[{dir_index}]({i},{j})" in cycle:
        return True
    return False


def in_bounds(i, j, n, m):
    return 0 <= i < n and 0 <= j < m


def find_start(data: list[list[str]], n, m) -> tuple:
    for i in range(n):
        for j in range(m):
            if data[i][j] == "^":
                return i, j
    raise ValueError("No starting position found")


def create_copy_with_new_obsticle(lab, obsticle_i, obsticle_j, n, m):
    new_lab = []
    for i in range(n):
        new_row = []
        for j in range(m):
            if (i, j) == (obsticle_i, obsticle_j):
                new_row.append("#")
            else:
                new_row.append(lab[i][j])
        new_lab.append("".join(new_row))
    return new_lab


if __name__ == "__main__":
    main()
