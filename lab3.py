"""Лабораторная работа №3
РАБОТА С ИТЕРАТОРАМИ, ГЕНЕРАТОРАМИ.
РАБОТА С ГЕНЕРАТОРНЫМИ ВЫРАЖЕНИЯМИ.
Написать функцию, которая принимает три целых чис-
ла x, a, b и с помощью генераторного выражения создает и воз-
вращает новый список длинной x случайных чисел от a до b.
Для решения данного задания рекомендуется использовать
функцию random.randint().
"""

import random


def generate_random_list(x, a, b):
    """
    Создает список из x случайных чисел в диапазоне от a до b включительно.

    Args:
        x: количество случайных чисел (длина списка)
        a: нижняя граница диапазона
        b: верхняя граница диапазона

    Returns:
        list: список случайных чисел
    """
    # Генераторное выражение для создания x случайных чисел от a до b
    random_list = [random.randint(a, b) for _ in range(x)]

    return random_list


# Дополнительные функции с разными подходами:


def generate_with_generator(x, a, b):
    """
    Создает генератор случайных чисел (не список).
    """
    return (random.randint(a, b) for _ in range(x))


def generate_with_map(x, a, b):
    """
    Альтернативное решение с использованием map.
    """
    return list(map(lambda _: random.randint(a, b), range(x)))


def generate_with_while(x, a, b):
    """
    Решение с использованием цикла while (без генераторного выражения).
    """
    result = []
    count = 0
    while count < x:
        result.append(random.randint(a, b))
        count += 1
    return result


# Тестирование функций
if __name__ == "__main__":
    # Параметры для тестирования
    x = 10
    a = 1
    b = 100

    print("=" * 50)
    print("ГЕНЕРАТОРНОЕ ВЫРАЖЕНИЕ:")
    print("=" * 50)
    result1 = generate_random_list(x, a, b)
    print(f"Список из {x} случайных чисел от {a} до {b}:")
    print(result1)

    print("\n" + "=" * 50)
    print("ГЕНЕРАТОР (не список):")
    print("=" * 50)
    result2 = generate_with_generator(x, a, b)
    print("Генератор создан. Преобразуем в список:")
    print(list(result2))

    print("\n" + "=" * 50)
    print("РЕШЕНИЕ С MAP:")
    print("=" * 50)
    result3 = generate_with_map(x, a, b)
    print(f"Список через map: {result3}")

    print("\n" + "=" * 50)
    print("РЕШЕНИЕ С WHILE:")
    print("=" * 50)
    result4 = generate_with_while(x, a, b)
    print(f"Список через while: {result4}")

    # Тест с разными параметрами
    print("\n" + "=" * 50)
    print("ТЕСТ С РАЗНЫМИ ПАРАМЕТРАМИ:")
    print("=" * 50)

    # Маленький диапазон
    small_range = generate_random_list(5, 1, 3)
    print(f"5 чисел от 1 до 3: {small_range}")

    # Отрицательные числа
    negative_range = generate_random_list(8, -10, 10)
    print(f"8 чисел от -10 до 10: {negative_range}")

    # Один элемент
    single_element = generate_random_list(1, 42, 42)
    print(f"1 число от 42 до 42: {single_element}")

    # Большой список
    big_list = generate_random_list(3, 1000, 2000)
    print(f"3 числа от 1000 до 2000: {big_list}")


# Дополнительная функция для демонстрации работы с генератором
def demonstrate_generator_usage():
    """
    Демонстрирует разницу между списком и генератором.
    """
    print("\n" + "=" * 50)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ ГЕНЕРАТОРА:")
    print("=" * 50)

    # Создаем генератор
    gen = generate_with_generator(5, 1, 10)
    print("Генератор создан. Можно итерироваться:")

    for i, num in enumerate(gen):
        print(f"Элемент {i + 1}: {num}")

    # Генератор можно использовать только один раз
    print("Попытка использовать генератор повторно (пустой):")
    print(f"Остаток: {list(gen)}")


# Запуск демонстрации
demonstrate_generator_usage()
