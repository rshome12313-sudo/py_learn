import re


price = input()

RUB_PATTERN = r"(\d+)\s?руб"
KOP_PATTERN = r"(\d+)\s?коп"


def parse_price(price: str) -> float | None:
    matches_rub = re.findall(RUB_PATTERN, price, re.IGNORECASE)
    if len(matches_rub) != 1:
        return None
    matches_kop = re.findall(KOP_PATTERN, price, re.IGNORECASE)
    rub = float(matches_rub[0])

    if len(matches_kop) >= 1:
        rub += float(matches_kop[0]) / 100
    return rub


def print_price(price: float | None) -> None:
    print(f"{price:.2f} ₽" if price is not None else "Некорректный формат суммы")


print_price(parse_price(price))
