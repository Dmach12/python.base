# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __
# init__()), который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.

class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __str__(self):
        return str('\n'.join(['\t'.join([str(m) for m in i]) for i in matr]))

    def __add__(self):
        matr = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.list_1)):

            for m in range(len(self.list_2[i])):
                matr[i][m] = self.list_1[i][m] + self.list_2[i][m]

        return str('\n'.join(['\t'.join([str(m) for m in i]) for i in matr]))


my_matrix = Matrix([[5, 18, 11],
                    [6, 17, 23],
                    [41, 50, 9]],
                   [[45, 8, 2],
                    [6, 7, 93],
                    [24, 5, 97]])


print(my_matrix.__add__())

