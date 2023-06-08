from solver import *

menu_options = {
    1: 'Пользовательский ввод',
    2: 'Ввод данных из файла',
    3: 'Генерация случайных матриц',
    4: 'Выход',
}


def print_menu():
    for key in menu_options.keys():
        print(key, '->', menu_options[key])


print('Лабораторная работа 1. Системы линейных алгебраических уравнений.\n')
print_menu()
choice_user = int(input('Выберите способ ввода данных в программу: ', ))


if choice_user == 1:
    size_input = checkSize()
    array_matrix = []
    inputMatrix(size_input, array_matrix)

elif choice_user == 2:
    array_matrix = checkFile()

elif choice_user == 3:
    size_input = checkSize()
    array_matrix = randomMatrix(size_input)

elif choice_user == 4:
    sys.exit()


def print_menu():
    for key in menu_options.keys():
        print(key, ' - ', menu_options[key])


printMatrix("Начальная матрица", array_matrix)
initial_matrix = copy.deepcopy(array_matrix)

count_swap = triangle(array_matrix)

printMatrix("Треугольная матрица", array_matrix)

determinant = Determinant(array_matrix, count_swap)
flag = checkByZero(determinant)
if flag:
    print("\nМатрица вырожденная. Определитель равен нулю.\n")
    exit(1)
print("Определитель: %5.5f" % determinant, '\n')
x = searchSolution(array_matrix)
printSolution(x)

vector_b = getVector_b(initial_matrix)
printVector("Вектор B (вектор свободных членов):", vector_b)
multiplication_ax = multiplicationAX(initial_matrix, x)
printVector("Результат перемножения матрицы A на вектор решения X:", multiplication_ax)
discrepancy = getDiscrepancy(multiplication_ax, vector_b)
printDiscrepancy(discrepancy)


