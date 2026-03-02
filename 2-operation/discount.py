from utils.input_int import input_int


price = input_int('Введите цену')
discount = input_int('Введите размер скидки')



discount_price =  price -(price / 100 * discount) 

print(f"Цена со скидкой {discount_price}")