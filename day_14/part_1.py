import re


class Robot:
    def __init__(self, p, v):
        self.p = p
        self.v = v

    def __repr__(self):
        return f"P: {self.p}\n V: {self.v} \n"


def parse_data(data: list[str]) -> list[Robot]:
    robots: list[Robot] = []
    for block in data:
        match = re.search(r"p=(\d+),(\d+) v=(\-?\d+),(\-?\d+)", block)

        if match:
            p = int(match.group(1)), int(match.group(2))
            v = int(match.group(3)), int(match.group(4))
            robots.append(Robot(p, v))
    return robots


def generate_matrix(robots: list[Robot], width, height):
    matrix = [["." for _ in range(width)] for _ in range(height)]
    for robot in robots:
        i, j = calculate_robot_position(robot, width, height)

        if matrix[i][j] == ".":
            matrix[i][j] = "1"
        else:
            current = matrix[i][j]
            matrix[i][j] = str(int(current) + 1)
    return matrix


def calculate_robot_position(robot: Robot, cols, rows):
    x = (robot.p[0] + robot.v[0] * 100) % cols  # from left wall (j)
    y = (robot.p[1] + robot.v[1] * 100) % rows  # from top wall (i)
    return y, x


def print_matrix(matrix):
    for row in matrix:
        print("".join(row))


def calculate_safety_factor(matrix):
    quadrants = get_quadrants(matrix)
    safety = 1
    for quadrant in quadrants:
        sum = 0
        for row in quadrant:
            for cell in row:
                if cell != ".":
                    sum += int(cell)
        safety *= sum
    return safety


def get_quadrants(matrix):
    rows, cols = len(matrix), len(matrix[0])
    mid_row = rows // 2
    mid_col = cols // 2

    top_left = [row[:mid_col] for row in matrix[:mid_row]]
    top_right = [row[mid_col + 1 :] for row in matrix[:mid_row]]
    bottom_left = [row[:mid_col] for row in matrix[mid_row + 1 :]]
    bottom_right = [row[mid_col + 1 :] for row in matrix[mid_row + 1 :]]

    return top_left, top_right, bottom_left, bottom_right


def main():
    with open("input.txt", "r") as file:
        data = file.read().strip().split("\n")
    robots = parse_data(data)

    matrix = generate_matrix(robots, 101, 103)
    factor = calculate_safety_factor(matrix)
    print(factor)


if __name__ == "__main__":
    main()
