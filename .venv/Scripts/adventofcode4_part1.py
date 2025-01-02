text = [] # List of strings

# Checks how many instances of 'XMAS' are in the word search.

def basic_search(line: str) -> int:
    """ Returns how many instances of 'XMAS' are in line """
    line = line.strip()
    return line.count('XMAS')

def horizontal_search() -> int:
    """ Searches left to right and right to left """
    total = 0
    for line in text:
        total += basic_search(line)
        total += basic_search(line[::-1])
    return total

def vertical_search() -> int:
    """ Searches top to bottom or bottom to top """
    columns = []
    total = 0

    for char in text[0]:
        columns.append('')
    for line in text:
        for i in range(len(line)):
            columns[i] += line[i]

    for col in columns:
        total += basic_search(col)
        total += basic_search(col[::-1])

    return total

def left_right_diagonal_search() -> int:
    total = 0
    width = len(text[0])
    height = len(text)

    x = 0
    y = height - 1
    diagonals = ['']
    while 0 <= x < width and 0 <= y < height:
        while y <= height - 1:
            diagonals[-1] += text[y][x]
            if y == height - 1:
                break
            else:
                x += 1
                y += 1

        y = height - 1 - (x + 1)
        x = 0
        diagonals.append('')

    x = width - 1
    y = 0
    while 0 <= x < width and 0 <= y < height:
        while y >= 0:
            diagonals[-1] += text[y][x]
            if y == 0:
                break
            else:
                x -= 1
                y -= 1

        y = width - x
        x = width - 1
        diagonals[-1] = diagonals[-1][::-1]
        diagonals.append('')
    diagonals = diagonals[:-2]  # Remove unnecessary position (empty and double counting)
    return diagonals

def right_left_diagonal_search() -> int:
    total = 0
    width = len(text[0])
    height = len(text)

    x = width - 1
    y = height - 1
    diagonals = ['']
    while 0 <= x < width and 0 <= y < height:
        while x <= width - 1:
            diagonals[-1] += text[y][x]
            if x == width - 1:
                break
            else:
                x += 1
                y -= 1

        x = width - (height - y + 1)
        y = height - 1
        diagonals.append('')

    x = 0
    y = 0
    while 0 <= x < width and 0 <= y < height:
        while x >= 0:
            diagonals[-1] += text[y][x]
            if x == 0:
                break
            else:
                x -= 1
                y += 1

        x = y + 1
        y = 0
        diagonals[-1] = diagonals[-1][::-1]
        diagonals.append('')
    diagonals = diagonals[:-2]  # Remove unnecessary position (empty and double counting)
    return diagonals

def diagonals_search() -> int:
    lr = left_right_diagonal_search()
    rl = right_left_diagonal_search()
    total = 0
    for line in lr:
        total += basic_search(line)
        total += basic_search(line[::-1])
    for line in rl:
        total += basic_search(line)
        total += basic_search(line[::-1])
    return total

from typing import List

def lrdiagonal(text: List[str]) -> int:
    """
    >>> lrdiagonal(["ABC", "BCD", "CDE"])
    ['C', 'BD', 'ACE', 'C', 'BD']
    >>> lrdiagonal(["123456", "234567", "000000", "123456", "234567", "000000"])
    ['0', '20', '130', '0240', '20350', '130460', '6', '57', '460', '3506', '24057']
    """
    total = 0
    width = len(text[0])
    height = len(text)

    x = 0
    y = height - 1
    diagonals = ['']
    while 0 <= x < width and 0 <= y < height:
        while y <= height - 1:
            diagonals[-1] += text[y][x]
            if y == height - 1:
                break
            else:
                x += 1
                y += 1

        y = height - 1 - (x + 1)
        x = 0
        diagonals.append('')

    x = width - 1
    y = 0
    while 0 <= x < width and 0 <= y < height:
        while y >= 0:
            diagonals[-1] += text[y][x]
            if y == 0:
                break
            else:
                x -= 1
                y -= 1

        y = width - x
        x = width - 1
        diagonals[-1] = diagonals[-1][::-1]
        diagonals.append('')
    diagonals = diagonals[:-2] # Remove unnecessary position (empty and double counting)
    return diagonals

def rldiagonal(text: List[str]) -> int:
    """
    >>> rldiagonal(["ABC", "BCD", "CDE"])
    ['E', 'DD', 'CCC', 'A', 'BB']
    >>> rldiagonal(["123456", "234567", "000000", "123456", "234567", "000000"])
    ['0', '07', '066', '0550', '04407', '033066', '1', '22', '033', '1044', '22055']
    """
    total = 0
    width = len(text[0])
    height = len(text)

    x = width - 1
    y = height - 1
    diagonals = ['']
    while 0 <= x < width and 0 <= y < height:
        while x <= width - 1:
            diagonals[-1] += text[y][x]
            if x == width - 1:
                break
            else:
                x += 1
                y -= 1

        x = width - (height - y + 1)
        y = height - 1
        diagonals.append('')

    x = 0
    y = 0
    while 0 <= x < width and 0 <= y < height:
        while x >= 0:
            diagonals[-1] += text[y][x]
            if x == 0:
                break
            else:
                x -= 1
                y += 1

        x = y + 1
        y = 0
        diagonals[-1] = diagonals[-1][::-1]
        diagonals.append('')
    diagonals = diagonals[:-2] # Remove unnecessary position (empty and double counting)
    return diagonals


with open('adventofcode_input.txt', 'r') as file:
    for line in file:
        text.append(line.strip())
    total = horizontal_search() + vertical_search() + diagonals_search()
    print(total)
