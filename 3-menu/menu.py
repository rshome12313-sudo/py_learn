from typing import Mapping

category = input("Выберете категорию: ")

soup = {"борщ": 50, "щи": 20, "суп-пюре": 100}
drink = {"чай": 12, "кофе": 12, "сок": 10}
desert = {"торт": 100, "мороженое": 23, "фрукты": 32}


def get_dish_price(dish: str, prices: Mapping[str, int]) -> int | None:
    normalized = dish.strip().lower()
    return prices.get(normalized)


def print_dish_price(dish: str, price: int | None) -> None:
    if price is not None:
        print(f"Цена на {dish}: {price} руб.")
    else:
        print(f"Блюдо \"{dish}\" не найдено")


match category.strip().lower():
    case "напиток":
        dish = input("Выберете напиток: ")
        price = get_dish_price(dish, drink)
        print_dish_price(dish, price)
    case "суп":
        dish = input("Выберете суп: ")
        price = get_dish_price(dish, soup)
        print_dish_price(dish, price)
    case "десерт":
        dish = input("Выберете десерт: ")
        price = get_dish_price(dish, desert)
        print_dish_price(dish, price)
    case _:
        print("Не известная категория")
