def main():
    with open("input.txt") as file:
        data = file.read().strip()

    memory = generate_memory(data)

    i = 0
    j = len(memory) - 1
    while i < j:
        while memory[i] != ".":
            i += 1
        while memory[j] == ".":
            j -= 1
        memory[i] = memory[j]
        memory[j] = "."

    filtered = [e for e in memory if e != "."]
    check_sum = calculate_checksum(filtered)
    print(check_sum)


def generate_memory(data: str):
    memory = []
    current_index = 0

    for i, x in enumerate(data):
        blocks = int(x)
        if i % 2 == 0:
            memory.extend([current_index] * blocks)
            current_index += 1
        else:
            memory.extend(["."] * blocks)

    return memory


def calculate_checksum(defragmented):
    return sum(i * int(block) for i, block in enumerate(defragmented))


if __name__ == "__main__":
    main()
