def input_int(phrase: str) :
    while True:
        try:
            number = int(input(f"{phrase}: "))
            return number
        except ValueError:
             print("Ошибка: Нужно вводить только цифры!") 
        except:
             print("Ошибка: повторите ввод!")
        continue