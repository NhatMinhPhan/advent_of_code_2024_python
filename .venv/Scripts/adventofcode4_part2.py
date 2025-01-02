text = [] # List of strings

class Matrix:
    """ 3x3 matrix found in the word search

    Follows this format:

    A B C
    D E F
    G H I

    """
    def __init__(self, a, b, c, d, e, f, g, h, i):
        self.matrix = [[a, b, c], [d, e, f], [g, h, i]]

    def __copy__(self):
        matrix_copy = Matrix(self.a, self.b, self.c, self.d, self.e, \
                             self.f, self.g, self.h, self.i)
        return matrix_copy

    def get_matrix(self):
        return self.matrix

    def __str__(self):
        return self.matrix

    def get(self, letter: str):
        """
        Returns the entry corresponding to the given letter for its position.

        Parameters:
            letter (int): The letter for the position of the entry to return
        """
        assert isinstance(letter, str), "letter is not a string"
        match letter.lower():
            case 'a':
                return self.matrix[0][0]
            case 'b':
                return self.matrix[0][1]
            case 'c':
                return self.matrix[0][2]
            case 'd':
                return self.matrix[1][0]
            case 'e':
                return self.matrix[1][1]
            case 'f':
                return self.matrix[1][2]
            case 'g':
                return self.matrix[2][0]
            case 'h':
                return self.matrix[2][1]
            case 'i':
                return self.matrix[2][2]
            case _:
                raise ValueError(f'"{letter}" is not a valid input.')
        return None

    def center(self):
        return self.get('e')

    pass

def is_x_mas(matrix: Matrix) -> bool:
    """ Indicates if matrix is an X-MAS """
    assert isinstance(matrix, Matrix), "matrix is not a Matrix object"

    if matrix.center() != 'A':
        return False

    if ((matrix.get('a') == 'M' and matrix.get('i') == 'S') \
        or (matrix.get('a') == 'S' and matrix.get('i') == 'M')) \
        and ((matrix.get('c') == 'M' and matrix.get('g') == 'S') \
        or (matrix.get('c') == 'S' and matrix.get('g') == 'M')):
        return True

    return False


with open('adventofcode_input.txt', 'r') as file:
    for line in file:
        text.append(line.strip())

    xmases = 0
    width = len(text[0])
    height = len(text)

    for i in range(1, height - 1):
        for j in range(1, width - 1):
            if text[i][j] == 'A':
                mat = Matrix(
                    text[i - 1][j - 1], text[i - 1][j], text[i - 1][j + 1],
                    text[i][j - 1], text[i][j], text[i][j + 1],
                    text[i + 1][j - 1], text[i + 1][j], text[i + 1][j + 1]
                    )
                if is_x_mas(mat):
                    xmases += 1

    print(xmases)