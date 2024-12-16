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


def print_matrix(matrix):
    for row in matrix:
        print("".join(row))


def calculate_gps(matrix):
    gps = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "O":
                gps += (100 * i) + j
    return gps


def main():
    with open("input.txt", "r") as file:
        m_data, dir_string = file.read().split("\n\n")
        matrix = [list(row) for row in m_data.strip().split("\n")]
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

        peek_i, peek_j = n_i + dx, n_j + dy
        while matrix[peek_i][peek_j] != "." and matrix[peek_i][peek_j] != "#":
            peek_i, peek_j = peek_i + dx, peek_j + dy

        if matrix[peek_i][peek_j] == ".":
            matrix[peek_i][peek_j] = "O"
            matrix[robot_i][robot_j] = "."
            matrix[n_i][n_j] = "@"
            robot_i, robot_j = n_i, n_j

    print_matrix(matrix)
    gps = calculate_gps(matrix)
    print(gps)


if __name__ == "__main__":
    main()
