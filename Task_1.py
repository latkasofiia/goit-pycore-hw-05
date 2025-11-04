
def caching_fibonacci():
    # Ініціалізуємо порожній словник для кешу
    cache = {}

    def fibonacci(n):
    
        # Перевірка базових випадків
        if n <= 0:
            return 0
        elif n == 1:
            return 1

        # Якщо результат уже є у кеші — повертаємо його
        if n in cache:
            return cache[n]

        # Інакше обчислюємо рекурсивно і зберігаємо у кеш
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

        # Повертаємо обчислене значення
        return cache[n]

    # Повертаємо внутрішню функцію fibonacci — вона має доступ до змінної cache
    return fibonacci


# Приклад використання:
if __name__ == "__main__":
    # Отримуємо функцію fibonacci з кешем
    fib = caching_fibonacci()

    # Обчислюємо кілька чисел Фібоначчі
    print(fib(10))  # Виведе 55
    print(fib(15))  # Виведе 610
    print(fib(20))  # Виведе 6765


