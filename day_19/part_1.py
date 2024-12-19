def main():
    with open("test_input.txt", "r") as file:
        data = file.read().strip().split("\n\n")

    patterns = data[0].split(", ")
    designs = data[1].split("\n")
    count = 0

    for design in designs:
        if is_valid_design(design, patterns):
            count += 1

    print(count)


def is_valid_design(current: str, patterns: tuple[str]) -> bool:
    if not current:
        return True
    for pattern in patterns:
        if current.startswith(pattern):
            if is_valid_design(current.removeprefix(pattern), patterns):
                return True
    return False


if __name__ == "__main__":
    main()
