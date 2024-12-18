from operator import xor


class Computer:
    def __init__(self, a: int, b: int, c: int, instructions: list[int]):
        self.a = a
        self.b = b
        self.c = c
        self.instructions = instructions  # (opcode, operand)
        self.instr_dict = self.create_instr_dict()
        self.output = []

    def __repr__(self) -> str:
        return f"A: {self.a} B:{self.b} C:{self.c}, Instructions: {self.instructions}"

    def create_instr_dict(self):
        return {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv,
        }

    def get_combo_dict(self) -> dict[int, int]:
        return {
            0: 0,
            1: 1,
            2: 2,
            3: 3,
            4: self.a,
            5: self.b,
            6: self.c,
            7: None,
        }

    def adv(self, combo: int, ip: int):
        self.a = self.a // (2 ** self.get_combo_dict()[combo])
        return ip + 2

    def bxl(self, literal: int, ip: int):
        self.b = xor(self.b, literal)
        return ip + 2

    def bst(self, combo: int, ip: int):
        self.b = self.get_combo_dict()[combo] % 8
        return ip + 2

    def jnz(self, literal: int, ip: int):
        if self.a == 0:
            return ip + 2
        return literal

    def bxc(self, operand: int, ip: int):
        self.b = xor(self.b, self.c)
        return ip + 2

    def out(self, combo: int, ip: int):
        self.output.append(self.get_combo_dict()[combo] % 8)
        return ip + 2

    def bdv(self, combo: int, ip: int):
        self.b = self.a // (2 ** self.get_combo_dict()[combo])
        return ip + 2

    def cdv(self, combo: int, ip: int):
        self.c = self.a // (2 ** self.get_combo_dict()[combo])
        return ip + 2

    def run(self):
        ip = 0
        while ip < len(self.instructions):
            opcode = self.instructions[ip]
            operand = self.instructions[ip + 1]
            ip = self.instr_dict[opcode](operand, ip)

        return ",".join(map(str, self.output))

    def calculate_a(self, power):
        solutions = []
        target = ",".join(map(str, self.instructions[::-1]))
        self.backtrack(0, power, solutions, target)
        return solutions

    def backtrack(self, sum, power, solutions, target):
        if power < 0:
            return

        for i in range(8):
            partial_sum = sum + (8**power) * i
            partial_computer = Computer(partial_sum, 0, 0, self.instructions)
            partial_computer.run()
            partial_output = ",".join(map(str, partial_computer.output))

            print(partial_output)

            if partial_output == target:
                solutions.append(partial_sum)
                return

            elif target.startswith(partial_output[: len(target) - power]):
                self.backtrack(partial_sum, power - 1, solutions, target)


def create_computer(data) -> Computer:
    a, b, c = map(lambda x: int(x.split(":")[1].strip()), data[:3])
    instructions = list(map(int, data[4].split()[1].split(",")))
    return Computer(a, b, c, instructions)


def main():
    with open("test_input.txt", "r") as file:
        data = file.read().strip().split("\n")
    computer = create_computer(data)
    solutions = computer.calculate_a(15)
    print(solutions)


if __name__ == "__main__":
    main()
