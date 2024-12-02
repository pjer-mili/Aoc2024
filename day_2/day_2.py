def main():
    data = getDataFromFile("./input.txt")
    safeCount = 0
    for report in data:
        if isReportSafe(report):
            safeCount += 1

    print(safeCount)


def getDataFromFile(file: str) -> list[int]:
    with open(file, "r") as txt:
        return [list(map(int, line.split())) for line in txt]


def isReportSafe(report: list[int]) -> bool:
    return all(
        (isDiffInRange(report[i], report[i + 1])) and report[i] < report[i + 1]
        for i in range(len(report) - 1)
    ) or all(
        (isDiffInRange(report[i], report[i + 1])) and report[i] > report[i + 1]
        for i in range(len(report) - 1)
    )


def isDiffInRange(a: int, b: int) -> bool:
    return abs(a - b) >= 1 and abs(a - b) <= 3


if __name__ == "__main__":
    main()
