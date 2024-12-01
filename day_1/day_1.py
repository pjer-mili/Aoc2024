def main():
    (arr1, arr2) = transformInput("./input.txt")
    arr1.sort()
    arr2.sort()
    sum = 0
    for i in range(len(arr1)):
        diff = abs(arr1[i] - arr2[i])
        sum += diff
    print(sum)


def transformInput(file: str) -> tuple[list[int], list[int]]:
    arr1 = []
    arr2 = []
    with open(file, "r") as txt:
        for line in txt:
            values = line.split()
            if len(values) > 2:
                raise Exception("Input invalid!")
            arr1.append(int(values[0]))
            arr2.append(int(values[1]))
        if len(arr1) != len(arr2):
            raise Exception("Array lengths do not match")
        return (arr1, arr2)


if __name__ == "__main__":
    main()
