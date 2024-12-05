def main():
    with open("./input.txt") as lines:
        data = lines.read().strip().split("\n")
        rules, updates = deserialize_data(data)

    incorrect = filter_incorrect(updates, rules)
    corrected_updates = apply_correction(incorrect, rules)

    sum = 0
    for update in corrected_updates:
        sum += update[len(update) // 2]

    print(sum)


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


def filter_incorrect(updates: list[list[int]], rules: dict):
    array = []
    for update in updates:
        if not is_update_correct(update, rules):
            array.append(update)
    return array


def is_update_correct(update: list[int], rules: dict):
    for i in range(len(update) - 1):
        current_value = update[i]
        rest = update[i + 1 :]

        for next in rest:
            rule_values = rules.get(next, [])
            if current_value in rule_values:
                return False

    return True


def apply_correction(updates: list[list[int]], rules: dict):
    corrected = []

    for update in updates:
        for i in range(len(update)):
            current_idx = i
            current_value = update[i]

            for j, next in enumerate(update[:i][::-1]):
                rule_values = rules.get(current_value, [])
                if next in rule_values:
                    original_idx = i - 1 - j
                    temp_value = next
                    update[original_idx] = current_value
                    update[current_idx] = temp_value
                    current_idx = original_idx

        corrected.append(update)

    return corrected


if __name__ == "__main__":
    main()
