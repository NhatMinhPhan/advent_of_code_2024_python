from typing import List

def adventofcode2():
    with open('adventofcode_input.txt', 'r') as file:
        num_of_safe = 0
        for report in file:
            levels = report.split(' ')
            if report_is_safe(levels):
                num_of_safe += 1
            elif safe_after_dampened(levels):
                num_of_safe += 1
    print(num_of_safe)


def report_is_safe(report: List[str]) -> bool:
    # Convert all elements into integers
    for index in range(len(report)):
        report[index] = int(report[index])
    # Compare indices 0 and 1
    is_increasing = False
    if report[0] < report[1]:
        is_increasing = True
    elif report[1] == report[0]:
        return False # Two adjacent levels must differ by at least one
    if (1 <= abs(report[1] - report[0]) <= 3) == False:
        return False

    for index in range(1, len(report) - 1):
        if (is_increasing and report[index] >= report[index + 1]) or \
                (is_increasing == False and report[index] <= report[index + 1]):
            return False

        if (1 <= abs(report[index] - report[index + 1]) <= 3) == False:
            return False

    return True

def safe_after_dampened(report: List[str]) -> bool:
    for index in range(len(report)):
        report_test = report.copy()

        report_test.pop(index)
        if report_is_safe(report_test):
            return True
    return False



adventofcode2()