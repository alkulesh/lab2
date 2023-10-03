def A():
    try:
        num1 = int(input("Введите первое число "))
        num2 = int(input("Введите второе число "))
        result = num1/num2
        print("Результат деления", result)
    except ValueError:
        print("Ошибка! Введены некорректные данные")
    except ZeroDivisionError:
        print("Деление на ноль невозможно!")
    return result

try:
    result = A()
except Exception as e:
    print("Произошла ошибка:", e)
finally:
    print("Программа выполнена!")