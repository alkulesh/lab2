def Input():
    try:
        x = True
        while (x):
            n = input("Введите количество строк матрицы ")
            if n.isdigit():
                if int(n) > 0:
                    break
            else:
                print("Введите целое число больше нуля! ")
        while (x):
            m = input("Введите количество столбцов матрицы ")
            if m.isdigit():
                if int(m) > 0:
                    break
            else:
                print("Введите целое число больше нуля! ")
        n = int(n)
        m= int(m)
        matrix = []
        for i in range(n):
            s = []
            for j in range(m):
                element = float(input(f"Введите элемент матрицы [{i + 1}][{j + 1}] "))
                s.append(element)
            matrix.append(s)
        return matrix
    except ValueError:
        print("Ошибка! Введены неверные данные! ")


def Check(matrix):
    try:
        x = True
        for s in matrix:
            y = False
            for element in s:
                if element > 0:
                    y = True
                    break
                if y == False:
                    x = False
                    break
            if x:
                for i in range(len(matrix)):
                    for j in range(len(matrix)):
                        matrix[i][j] = 1 / matrix[i][j]
            return matrix
    except ZeroDivisionError:
        print("Ошибка! Деление на ноль невозможно!")


try:
    matrix = Input()
    result = Check(matrix)
    print(result)
except Exception as e:
    print("Произошла ошибка:", e)
