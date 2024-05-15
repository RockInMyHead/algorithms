import numpy as np

def define_main_diagonal_sum(matrix):
    return np.trace(matrix)

def define_secondary_diagonal_sum(matrix):
    return np.trace(np.fliplr(matrix))

def main_diagonal_sum_1():
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("Матрица:")
    print(matrix)
    print("Сумма элементов на главной диагонали:", define_main_diagonal_sum(matrix))
    print("Сумма элементов на побочной диагонали:", define_secondary_diagonal_sum(matrix))

if __name__ == "__main__":
    main_diagonal_sum_1()