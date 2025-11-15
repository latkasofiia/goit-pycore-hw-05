
import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[float, None, None]:
    # Шукаємо тільки числа, які мають пробіли з обох боків
    numbers = re.findall(r" (\d+(?:\.\d+)?) ", text)

    for num in numbers:
        yield float(num)


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    return sum(func(text))


if __name__ == "__main__":
    text = (
        " Загальний дохід складається з 1000.01 i ще 27.45 a також 324.00 "
    )

    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
