from typing import List

# 0 for multiplication, 1 for addition, 2 for concatenation
# This algorithm takes a while, but still does the job.

def generate_n_tuples(n: int):
    assert isinstance(n, int) and n >= 1, "n must be an integer and at least 1"
    current_trit_str = '0' * n
    tuples = [tuple(['0'] * n)]

    while current_trit_str != '2' * n:
        current_trit_str = get_next_trit_string(current_trit_str)
        new_tuple = []
        for trit in current_trit_str:
            new_tuple.append(trit)
        tuples.append(tuple(new_tuple))

    return tuples


def get_next_trit_string(str1: str):
    """
    >>> get_next_trit_string('0012')
    '0020'
    >>> get_next_trit_string('11')
    '12'
    >>> get_next_trit_string('1001')
    '1002'
    >>> get_next_trit_string('0')
    '1'
    >>> get_next_trit_string('101010101')
    '101010102'
    """

    assert isinstance(str1, str), "str1 is not a string"
    assert str1.count('0') + str1.count('1') + str1.count('2') == len(str1),\
        "There is a foreign character (not 0, 1, or 2) in str1"

    i = -1
    while i > -len(str1) - 1:
        if str1[i] == '0':
            if i == -1:
                str1 = str1[:i] + '1'
            else:
                str1 = str1[:i] + '1' + str1[i + 1:]
            break
        if str1[i] == '1':
            if i == -1:
                str1 = str1[:i] + '2'
            else:
                str1 = str1[:i] + '2' + str1[i + 1:]
            break
        elif str1[i] == '2':
            if i == -len(str1):
                str1 = '10' + str1[i + 1:]
                break
            elif i == -1:
                str1 = str1[:i] + '0'
            else:
                str1 = str1[:i] + '0' + str1[i + 1:]
        i -= 1

    return str1

def can_be_true(numbers: List[str], goal: str):
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    goal = int(goal)

    operation_tuples = generate_n_tuples(len(numbers) - 1)

    # 0 for multiplication, 1 for addition, 2 for concatenation
    for op_tuple in operation_tuples:
        test_numbers = numbers.copy()
        for i in range(0, len(test_numbers) - 1):
            if op_tuple[i] == '0': # Multiplication
                test_numbers[i + 1] = test_numbers[i] * test_numbers[i + 1]
            elif op_tuple[i] == '1': # Addition
                test_numbers[i + 1] = test_numbers[i] + test_numbers[i + 1]
            elif op_tuple[i] == '2': # Concatenation
                test_numbers[i + 1] = int(str(test_numbers[i]) + str(test_numbers[i + 1]))
        # After this loop, the last element of test_numbers is the result
        if test_numbers[-1] == goal:
            return True
    return False

with open('adventofcode_input.txt', 'r') as file:
    sum = 0

    for line in file:
        line_elements = line.strip().split(': ')
        goal = line_elements[0]
        numbers = line_elements[1].split(' ')
        if can_be_true(numbers, goal):
            sum += int(goal)

    print(sum)