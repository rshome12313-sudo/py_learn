from utils.input_int import input_int


eat_expense = input_int('Введите сумму трат на еду')
car_expense = input_int('Введите сумму трат на транспорт')
entertainment_expense = input_int('Введите сумму трат на развлечения')

sum_expense = eat_expense + car_expense + entertainment_expense
mean_expense = sum_expense / 3


print(f"Общая сумма трат: {sum_expense}, средняя сумма {mean_expense}")