from enum import Enum


class Direction(Enum):
    LEFT = ("<", (0, -1))
    RIGHT = (">", (0, 1))
    UP = ("^", (-1, 0))
    DOWN = ("v", (1, 0))

    def __init__(self, symbol, delta):
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


def out_of_bounds(i, j, matrix):
    return i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0])


def objects_num_to_move(i, j, direction: Direction, matrix: list[str]):
    k = 1
    dx, dy = direction.delta

    while True:
        new_i = i + k * dx
        new_j = j + k * dy

        if out_of_bounds(new_i, new_j, matrix):
            return 0

        current_cell = matrix[new_i][new_j]
        if current_cell == "#":
            return 0
        if current_cell == ".":
            return k

        k += 1


def print_matrix(matrix):
    for row in matrix:
        print("".join(row))


def main():
    with open("test_input.txt", "r") as file:
        m_data, dir_string = file.read().split("\n\n")
        matrix = m_data.strip().split("\n")
    directions = map_directions(dir_string)
    robot_i, robot_j = get_robot_coordinates(matrix)


if __name__ == "__main__":
    main()
