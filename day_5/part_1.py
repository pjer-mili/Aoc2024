def main():
    with open("./test_input.txt") as lines:
        data = lines.read().strip().split("\n")
        rules, updates = deserialize_data(data)

    result = 0
    for update in updates:
        result += is_update_correct(update, rules)

    print(result)


def deserialize_data(data: list[str]):
    rules = {}
    updates = []

    for i, line in enumerate(data):
        if line == "":
            updates = [
                [int(num) for num in group.split(",")] for group in data[i + 1 :]
            ]
            break
        x, y = map(int, line.split("|"))
        if x not in rules:
            rules[x] = [y]
        else:
            rules[x].append(y)

    return rules, updates


def is_update_correct(update: list[int], rules: dict):
    for i in range(len(update) - 1):
        current_value = update[i]
        rest = update[i + 1 :]

        for next in rest:
            rule_values = rules.get(next, [])
            if current_value in rule_values:
                return 0

    return update[len(update) // 2]


if __name__ == "__main__":
    main()
