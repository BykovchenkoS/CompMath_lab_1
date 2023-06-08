import copy
import numpy
import sys


def inputMatrix(size, input_args):
    def do_input(i_arg, input_arg, size):
        user_input = input(f'Введите {i_arg}-е уравнение через пробел: ').strip()
        user_input = user_input.replace(',,', ',').replace(',', '.').replace('- ', '-')
        while '  ' in user_input:
            user_input = user_input.replace('  ', ' ')

        s = user_input.split(' ')
        if len(s) != (size + 1):
            print('Неверное количество коэффициентов')
            do_input(i, input_args, size)

        else:
            s = [float(each) for each in s]
            input_arg.append(s)

    i = 1
    while i <= size:
        try:
            do_input(i, input_args, size)

        except ValueError:
            print('Ошибка! Вы вввели не число!')
            continue
        i += 1


def checkSize():
    while True:
        size_arg = int(input('Введите размерность матрицы: '))

        if size_arg <= 0:
            flag = 0
        else:
            break

        if flag == 0:
            print('Упс...Похоже матрица такого размер не может существовать. Попробуйте снова!')
    return size_arg


def checkFile():
    try:
        with open('input.txt', 'r') as f:

            input_arg = []

            content = f.readlines()
            for line in content:
                line = line.replace(',,', ',').replace(',', '.').replace('- ', '-')

                while '  ' in line:
                    line = line.replace('  ', ' ')

                s = line.split(' ')
                s = [float(each) for each in s]

                input_arg.append(s)
        return input_arg

    except ValueError:
        print('Ошибка! В файле содержатся не только цифры.')
        sys.exit(1)


def randomMatrix(size):
    array_matrix = numpy.random.uniform(low=2, high=20, size=(size, size+1))
    return array_matrix


def printMatrix(message, input_args):
    print(message)
    size_str = len(input_args)

    for i in range(size_str):
        line = ""
        for j in range(size_str + 1):
            line += str("%10.5f" % input_args[i][j]) + "      "
            if j == size_str - 1:
                line += "| "
        print(line)
    print("")


def printSolution(x):
    print("Корни системы:")
    for i, solution in enumerate(x):
        print(f"x{i + 1}",  " = ", solution)
    print()


def printVector(info, vector):
    print(info)
    size = len(vector)
    for i in range(size):
        print(vector[i], end="    ")
    print("")


def searchMax(a, column, count_swap):
    size = len(a)
    max_el = a[column][column]
    max_row = column
    for i in range(column + 1, size):
        if max_el < abs(a[i][column]):
            max_el = abs(a[i][column])
            max_row = i
    if column != max_row:
        swap(a, max_row, column)
        count_swap += 1
    return count_swap


error = 1e-10


def checkByZero(arg):
    return abs(arg) < error


def Determinant(matrix, count_swap):
    det = 1
    size = len(matrix)
    if count_swap is None:
        sys.exit()
    elif count_swap % 2:
        count_swap = -1
    else:
        count_swap = 1

    for i in range(size):
        det *= matrix[i][i]

    det *= count_swap
    return det


def swap(a, row_1, row_2=0):
    n = len(a)
    for i in range(n + 1):
        tmp = a[row_1][i]
        a[row_1][i] = a[row_2][i]
        a[row_2][i] = tmp


def sub(a, row_1, row_2, c=1):
    size = len(a)
    for i in range(size + 1):
        a[row_1][i] -= a[row_2][i] * c
    return a


def triangle(a):
    try:
        size = len(a)
        count_swap = 0
        for i in range(size):
            count_swap = searchMax(a, i, count_swap)
            for j in range(i + 1, size):
                c = a[j][i] / a[i][i]
                sub(a, j, i, c)
        return count_swap
    except ZeroDivisionError:
        print('Система уравнений не имеет решений.')
        sys.exit()


def searchSolution(a):
    size_a = len(a)
    solution = [0 for i in range(size_a)]
    for i in range(size_a - 1, -1, -1):
        solution[i] = a[i][size_a] / a[i][i]
        for j in range(i - 1, -1, -1):
            a[j][size_a] -= a[j][i] * solution[i]
    return solution


def gauss(a):
    count_swap = triangle(a)
    det = Determinant(a, count_swap)
    zero = checkByZero(det)
    if zero:
        print("\nМатрица вырожденная. Определитель равен нулю\n")
        exit(1)
    x = searchSolution(a)
    return x


def multiplicationAX(a, x):
    size_a = len(a)
    size_x = len(x)
    result = []
    for i in range(size_a):
        s = 0
        for j in range(size_x):
            s += x[j] * a[i][j]
        result.append(s)
    return result


def getVector_b(a):
    n = len(a)
    vector_b = []
    for i in range(n):
        vector_b.append(a[i][n])
    return vector_b


def getVector_a(a):
    vector_a = a[:]
    return vector_a


def getDiscrepancy(res, b):
    for i in range(len(b)):
        res[i] = b[i] - res[i]
    return res


def printDiscrepancy(x):
    print("\nНевязка:")
    for i, solution in enumerate(x):
        print(f"f{i + 1}",  " = ", solution)
    print()
