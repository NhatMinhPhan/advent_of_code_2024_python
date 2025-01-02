from typing import List

# True for multiplication, False for addition

def generate_boolean_n_tuples(n: int):
    assert isinstance(n, int) and n >= 1, "n must be an integer and at least 1"
    current_bit_str = '0' * n
    tuples = [tuple([False] * n)]

    while current_bit_str != '1' * n:
        current_bit_str = get_next_bit_string(current_bit_str)
        new_tuple = []
        for bit in current_bit_str:
            match bit:
                case '0':
                    new_tuple.append(False)
                case '1':
                    new_tuple.append(True)
        tuples.append(tuple(new_tuple))

    return tuples


def get_next_bit_string(str1: str):
    """
    >>> get_next_bit_string('0011')
    '0100'
    >>> get_next_bit_string('11')
    '100'
    >>> get_next_bit_string('1001')
    '1010'
    >>> get_next_bit_string('0')
    '1'
    >>> get_next_bit_string('101010101')
    '101010110'
    """

    assert isinstance(str1, str), "str1 is not a string"
    assert str1.count('0') + str1.count('1') == len(str1), "There is a foreign character (not 1 or 0) in str1"

    i = -1
    while i > -len(str1) - 1:
        if str1[i] == '0':
            if i == -1:
                str1 = str1[:i] + '1'
            else:
                str1 = str1[:i] + '1' + str1[i + 1:]
            break
        elif str1[i] == '1':
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

    operation_tuples = generate_boolean_n_tuples(len(numbers) - 1)

    # True for multiplication, False for addition
    for op_tuple in operation_tuples:
        test_numbers = numbers.copy()
        for i in range(0, len(test_numbers) - 1):
            if op_tuple[i] == True:
                test_numbers[i + 1] = test_numbers[i] * test_numbers[i + 1]
            else:
                test_numbers[i + 1] = test_numbers[i] + test_numbers[i + 1]
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