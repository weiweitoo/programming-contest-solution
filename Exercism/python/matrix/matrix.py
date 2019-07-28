class Matrix(object):
    def __init__(self, matrix_string):
        matrix_string_split = matrix_string.split('\n')
        self.matrix = []
        for row in matrix_string_split:
            self.matrix.append([int(i) for i in row.split(' ')])
        self.transpose_matrix = [list(i) for i in zip(*self.matrix)]

    def row(self, index):
        return self.matrix[int(index-1)]

    def column(self, index):
        return self.transpose_matrix[int(index-1)]
