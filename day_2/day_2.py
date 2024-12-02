def main():
    data = getDataFromFile("./test_input.txt")
    safeCount = 0
    for report in data:
        if isReportSafe(report):
            safeCount += 1

    print(safeCount)


def getDataFromFile(file: str) -> list[int]:
    with open(file, "r") as txt:
        return [list(map(int, line.split())) for line in txt]


def isReportSafe(report: list[int]) -> bool:
    ascending = report[0] < report[1]
    compare = (lambda x, y: x < y) if ascending else (lambda x, y: x > y)
    for i in range(len(report) - 1):
        if not (
            compare(report[i], report[i + 1])
            and isDiffInRange(report[i], report[i + 1])
        ):
            return False
    return True


def isDiffInRange(a: int, b: int) -> bool:
    return abs(a - b) >= 1 and abs(a - b) <= 3


if __name__ == "__main__":
    main()
