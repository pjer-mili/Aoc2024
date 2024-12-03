import re


def main():
    sum = 0
    pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)")

    with open("./input.txt", "r") as file:
        data = file.read()
        iterator = pattern.finditer(data)
        do = True
        for match in iterator:
            command = match.group()
            if "do()" in command:
                do = True
                continue
            if "don't()" in command:
                do = False
                continue
            if do:
                mul_tuple = eval(match.group()[3:])
                sum += mul_tuple[0] * mul_tuple[1]

    print(sum)


if __name__ == "__main__":
    main()
