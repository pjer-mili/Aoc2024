from enum import Enum


class Direction(Enum):
    LEFT = ("<", (0, -1))
    RIGHT = (">", (0, 1))
    UP = ("^", (-1, 0))
    DOWN = ("v", (1, 0))

    def __init__(self, symbol: str, delta: tuple):
        self.symbol = symbol
        self.delta = delta


def map_directions(input_str) -> list[Direction]:
    directions: list[Direction] = []
    for symbol in input_str:
        for direction in Direction:
            if symbol == direction.symbol:
                directions.append(direction)
                break
    return directions


def get_robot_coordinates(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "@":
                return i, j
    return None


def in_bounds(i, j, matrix):
    return 0 <= i < len(matrix) and 0 <= j < len(matrix[0])


def calculate_gps(matrix):
    gps = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "O" or matrix[i][j] == "[":
                gps += (100 * i) + j
    return gps


def print_matrix(matrix):
    for row in matrix:
        print("".join(row))


def expand_matrix(grid_str):
    new_matrix = []
    for row in grid_str.strip().split("\n"):
        expanded_row = []
        for char in row:
            if char == "#":
                expanded_row.extend(["#", "#"])
            elif char == "O":
                expanded_row.extend(["[", "]"])
            elif char == ".":
                expanded_row.extend([".", "."])
            elif char == "@":
                expanded_row.extend(["@", "."])
            else:
                expanded_row.append(char)
        new_matrix.append(expanded_row)

    return new_matrix


def get_shift_chain(robot_i, robot_j, n_i, n_j, dx, dy, matrix):
    queue = []
    queue.append((robot_i, robot_j))
    visited = {}
    visited[(n_i, n_j)] = matrix[n_i][n_j]

    while queue:
        curr_i, curr_j = queue.pop(0)
        peek_i, peek_j = curr_i + dx, curr_j + dy

        if matrix[peek_i][peek_j] == "#":
            return None
        if matrix[peek_i][peek_j] == ".":
            continue

        visited[(peek_i, peek_j)] = matrix[peek_i][peek_j]
        if matrix[peek_i][peek_j] == "[":
            queue.append((peek_i, peek_j))
            queue.append((peek_i, peek_j + 1))
            visited[(peek_i, peek_j + 1)] = matrix[peek_i][peek_j + 1]
        elif matrix[peek_i][peek_j] == "]":
            queue.append((peek_i, peek_j))
            queue.append((peek_i, peek_j - 1))
            visited[(peek_i, peek_j - 1)] = matrix[peek_i][peek_j - 1]
    return visited


def main():
    with open("test_input.txt", "r") as file:
        m_string, dir_string = file.read().split("\n\n")
        matrix = expand_matrix(m_string)

    robot_i, robot_j = get_robot_coordinates(matrix)
    directions = map_directions(dir_string)
    for direction in directions:
        dx, dy = direction.delta
        n_i, n_j = robot_i + dx, robot_j + dy

        if matrix[n_i][n_j] == "#":
            continue

        if matrix[n_i][n_j] == ".":
            matrix[robot_i][robot_j] = "."
            matrix[n_i][n_j] = "@"
            robot_i, robot_j = n_i, n_j
            continue

        if dy != 0:
            peek_j = n_j

            while matrix[robot_i][peek_j] != "." and matrix[robot_i][peek_j] != "#":
                peek_j += dy

            if matrix[robot_i][peek_j] == "#":
                continue

            shift_j = peek_j
            while shift_j != robot_j - dy:
                matrix[robot_i][shift_j] = matrix[robot_i][shift_j - dy]
                shift_j -= dy
            matrix[robot_i][robot_j] = "."
            robot_j = n_j
        else:
            shifting_chain = get_shift_chain(robot_i, robot_j, n_i, n_j, dx, dy, matrix)
            if shifting_chain:
                for p, cell in shifting_chain.items():
                    matrix[p[0]][p[1]] = "."
                for p, cell in shifting_chain.items():
                    matrix[p[0] + dx][p[1] + dy] = cell

                matrix[robot_i][robot_j] = "."
                matrix[n_i][robot_j] = "@"
                robot_i, robot_j = n_i, n_j

    gps = calculate_gps(matrix)
    print(gps)


if __name__ == "__main__":
    main()
