import itertools as it
import timeit


def main():
    data = getDataFromFile("./input.txt")
    safeCount = 0
    for report in data:
        if isReportSafe(report) or any(
            isReportSafe(report[:i] + report[i + 1 :]) for i in range(len(report))
        ):
            safeCount += 1

    print(safeCount)


def getDataFromFile(file: str) -> list[int]:
    with open(file, "r") as txt:
        return [list(map(int, line.split())) for line in txt]


def isReportSafe(report: list[int]) -> bool:
    diffs = [b - a for a, b in it.pairwise(report)]
    return all(1 <= d <= 3 for d in diffs) or all(-3 <= d <= -1 for d in diffs)


def benchmark():
    execution_time = timeit.timeit("main()", globals=globals(), number=1)
    print(f"Benchmark: {execution_time:.6f} seconds")


if __name__ == "__main__":
    benchmark()
