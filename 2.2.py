def Data(data):
    try:
        if isinstance(data,list):
            number = [num for num in data if num > 0]
            if number:
                last_index = len(data) - data[::-1].index(number[-1]) - 1
                Sum_ = sum(data[last_index+1:])
                print("Сумма всех элементов после последнего положительного числа равна ", Sum_)
            else:
                print("Нет положительных элементов в списке")
            data = [num for num in data if num != 0]
            print("Список без нулевых элементов имеет вид:", data)
        elif isinstance(data, dict):
            min_el = min(data.values())
            min_el_key = [key for key, value in data.items() if value == min_el][0]
            print("Элемент с минимальным значением: ", min_el_key)
        elif isinstance(data, int):
            number_= int(str(data)[::-1])
            print("Число в обратном порядке: ", number_)
        elif isinstance(data, str):
            word = len(data.split())
            print("Количество слов в строке: ", word)
        else:
            print("Неподдерживаемый тип данных")
    except Exception as e:
        print("Произошла ошибка:", e)

try:
    x = True
    while(x):
        x = input("Выберите действие:\n1. Ввести список\n2. Ввести словарь\n3. Ввести число\n4. Ввести строка\n")
        if x.isdigit():
            x = int(x)
            if x > 0 and x < 5:
                if x == 1:
                    while True:
                        data = list(map(int, input("Введите данные ").split()))
                elif x == 2:
                    my_dict = {}
                    while True:
                        key = input("Введите ключ или 'стоп' для завершения " )
                        if key == "стоп":
                            break
                        while True:
                            value = input("Введите значение: ")
                            if value.isdigit():
                                my_dict[key] = value
                                break
                            else:
                                print("Введите целое число! ")
                    data = my_dict
                elif x == 3:
                    while True:
                        data = input("Введите данные ")
                        if data.isdigit():
                            data = int(data)
                            break
                        else:
                            print("Ошибка! Введите целое число! ")
                elif x == 4:
                    while True:
                        data = input("Введите данные ")
                        if isinstance(data, str):
                            data = str(data)
                            break
                        else:
                            print("Ошибка! Введите строку!")

                else:
                    print("Ошибка! Введите ещё раз!")
                break
        else:
            print("Ошибка! Введите ещё раз! ")
except Exception as e:
        print("Произошла ошибка:", e)
finally:
    result = Data(data)