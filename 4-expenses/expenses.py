menu = (
    "1. ➕ Добавить расход\n"
    "2. 📜 Показать все расходы\n"
    "3. 📊 Сумма и средний расход\n"
    "4. ❌ Удалить расход по номеру\n"
    "5. 👋 Выход\n"
)


def input_int(phrase: str, min_index: int = 0, max_index: int = 10, stop: str = "exit"):
    while True:
        try:
            print(phrase)
            user_input = input(f"({min_index}-{max_index}): ")
            if user_input == stop:
                print("До свидания!")
                exit()
            count = int(user_input)
            if count > max_index:
                print(f"{count} слишком большое! Максимальное число {max_index}")
                continue
            if count < min_index:
                print(f"{count} слишком маленькое! Минимальной число {max_index}")
            return count
        except KeyboardInterrupt:
            print("\nДо свидания!")
            exit()
        except Exception:
            print(
                f"Не корректный ввод допустимые значения {min_index}-{max_index}")


def run():
    # print_menu()
    user_input = input_int(menu, min_index=1, max_index=5)
    if user_input == 5:
        exit()


run()
