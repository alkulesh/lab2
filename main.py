def anogram():
    try:
        x = True
        while (x):
            word1 = input("Введите первое слово ")
            word2 = input("Введите второе слово ")
            word1 = word1.lower().replace(" ", "")
            word2 = word2.lower().replace(" ", "")
            if not word1.isalpha() or not word2.isalpha():
                print("Введены некоректные символы! Введите только буквы! ")
            else:
                x = False
        if sorted(word1) == sorted(word2):
            return True
        else:
            return False
    except Exception as e:
        print("Произошла ошибка:", e)


try:
    if anogram():
        print("Слова являются анограммами! ")
    else:
        print("Слова не являются анаграммами! ")
except Exception as e:
    print("Произошла ошибка:", e)
finally:
    print("Программа выполнена!")
