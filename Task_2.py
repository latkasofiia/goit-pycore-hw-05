
import re
from typing import Callable, Generator

# Функція generator_numbers приймає текст і повертає генератор,
def generator_numbers(text: str) -> Generator[float, None, None]:

    # Знаходимо всі числа з плаваючою крапкою або цілі числа.
    # \b — означає "межу слова", щоб не знаходити числа всередині слів.
    numbers = re.findall(r"\b\d+\.\d+|\b\d+\b", text)

    # Перетворюємо кожен знайдений рядок у число з плаваючою крапкою і повертаємо його 
    for num in numbers:
        yield float(num)


# Функція sum_profit приймає текст і функцію (generator_numbers),
# викликає генератор та обчислює суму всіх знайдених чисел.
def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
 
    # Генеруємо всі числа і підсумовуємо їх
    return sum(func(text))


# Приклад використання:
if __name__ == "__main__":
    text = (
        "Загальний дохід працівника складається з декількох частин: "
        "1000.01 як основний дохід, доповнений додатковими надходженнями "
        "27.45 i 324.00 доларів."
    )

    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")  # Очікуване виведення: 1351.46
