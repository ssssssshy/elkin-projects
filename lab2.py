""" "Лабораторная работа №2
РАБОТА С ОСНОВНЫМИ ВСТРОЕННЫМИ
ФУНКЦИЯМИ.
Написать функцию, которая принимает список, кото-
рый содержит строки и выводит на экран новые списки из вхо-
дящих строк.
"""


def process_strings(input_list):
    """
    Обрабатывает список строк и выводит новые списки.

    Args:
        input_list: список, содержащий строки
    """
    # Проверяем, что список не пустой
    if not input_list:
        print("Входной список пуст!")
        return

    # 1. Список строк в верхнем регистре
    upper_list = [s.upper() for s in input_list]
    print(f"Список в верхнем регистре: {upper_list}")

    # 2. Список строк в нижнем регистре
    lower_list = [s.lower() for s in input_list]
    print(f"Список в нижнем регистре: {lower_list}")

    # 3. Список длин строк
    length_list = [len(s) for s in input_list]
    print(f"Список длин строк: {length_list}")

    # 4. Список строк, отсортированный по алфавиту
    sorted_list = sorted(input_list)
    print(f"Отсортированный список: {sorted_list}")

    # 5. Список строк в обратном порядке
    reversed_list = list(reversed(input_list))
    print(f"Список в обратном порядке: {reversed_list}")

    # 6. Список уникальных строк (без повторений)
    unique_list = list(set(input_list))
    print(f"Список уникальных строк: {unique_list}")


# Тестирование функций
if __name__ == "__main__":
    # Пример входного списка
    test_list = ["Hello", "world", "Python", "programming", "hello", "World"]

    print("=" * 50)
    print("ОСНОВНАЯ ОБРАБОТКА СТРОК:")
    print("=" * 50)
    process_strings(test_list)

    print("\n" + "=" * 50)
    print("РАСШИРЕННАЯ ОБРАБОТКА СТРОК:")
    print("=" * 50)

    # Тест с пустым списком
    print("\n" + "=" * 50)
    print("ТЕСТ С ПУСТЫМ СПИСКОМ:")
    print("=" * 50)
    process_strings([])

    # Тест со списком, содержащим пробелы
    print("\n" + "=" * 50)
    print("ТЕСТ СО СПИСКОМ С ПРОБЕЛАМИ:")
    print("=" * 50)
    space_list = ["  hello  ", "world ", " python", "123", "abc def"]
    process_strings(space_list)
