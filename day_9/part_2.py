def main():
    with open("input.txt") as file:
        data = file.read().strip()

    memory = generate_memory(data)
    occupied, empty = generate_block_positions(memory)

    for i in range(len(occupied) - 1, -1, -1):
        o_idx, o_size = occupied[i]
        for e_idx, e_size in empty:
            if e_size >= o_size and o_idx > e_idx:
                for j in range(o_size):
                    memory[e_idx + j] = memory[o_idx + j]
                    memory[o_idx + j] = "."

                occupied[i] = (e_idx, o_size)
                empty.remove((e_idx, e_size))
                if e_size > o_size:
                    empty.append((e_idx + o_size, e_size - o_size))
                empty.append((o_idx, o_size))
                empty.sort()
                break

    print(calculate_checksum(memory))


def generate_block_positions(memory):
    i = 0
    empty = []
    occupied = []
    while i < len(memory):
        block_size = 0
        start_index = i
        if memory[i] == ".":
            while i < len(memory) and memory[i] == ".":
                block_size += 1
                i += 1
            empty.append((start_index, block_size))
        else:
            current_id = memory[i]
            while i < len(memory) and memory[i] == current_id:
                block_size += 1
                i += 1
            occupied.append((start_index, block_size))
    return occupied, empty


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
    return sum(i * int(block) for i, block in enumerate(defragmented) if block != ".")


if __name__ == "__main__":
    main()
