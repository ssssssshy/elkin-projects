"""Лабораторная работа №4
РАБОТА С ОСНОВНЫМИ МОДУЛЯМИ
Написать функцию, которая принимает строку и воз-
вращает объект datetime из этой строки. Формат даты и време-
ни можно использовать любой."""

from datetime import datetime
import dateutil.parser


def parse_datetime_from_string(date_string):
    """
    Преобразует строку в объект datetime.
    Пытается автоматически определить формат даты.

    Args:
        date_string: строка с датой и временем

    Returns:
        datetime: объект datetime
    """
    try:
        # Попытка автоматического определения формата
        return dateutil.parser.parse(date_string)
    except:
        raise ValueError(f"Не удалось распознать дату из строки: {date_string}")


def parse_datetime_with_formats(date_string, formats=None):
    """
    Преобразует строку в объект datetime с использованием
    конкретных форматов.

    Args:
        date_string: строка с датой и временем
        formats: список форматов для попытки парсинга

    Returns:
        datetime: объект datetime
    """
    if formats is None:
        formats = [
            "%Y-%m-%d %H:%M:%S",
            "%d.%m.%Y %H:%M:%S",
            "%m/%d/%Y %H:%M:%S",
            "%Y-%m-%d",
            "%d.%m.%Y",
            "%m/%d/%Y",
            "%H:%M:%S",
            "%Y-%m-%d %H:%M",
            "%d.%m.%Y %H:%M",
        ]

    for fmt in formats:
        try:
            return datetime.strptime(date_string, fmt)
        except ValueError:
            continue

    raise ValueError(
        f"Не удалось распознать дату '{date_string}' с предоставленными форматами"
    )


# Дополнительные полезные функции для работы с датами
def get_current_datetime():
    """Возвращает текущую дату и время"""
    return datetime.now()


def format_datetime(dt_obj, format_str="%Y-%m-%d %H:%M:%S"):
    """
    Форматирует объект datetime в строку

    Args:
        dt_obj: объект datetime
        format_str: строка формата

    Returns:
        str: отформатированная строка даты
    """
    return dt_obj.strftime(format_str)


def datetime_demo():
    """Демонстрация работы с datetime"""
    print("=" * 60)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ С ДАТАМИ И ВРЕМЕНЕМ")
    print("=" * 60)

    # Текущая дата и время
    current = get_current_datetime()
    print(f"Текущая дата и время: {current}")
    print(f"Отформатированно: {format_datetime(current)}")
    print(f"Только дата: {format_datetime(current, '%d.%m.%Y')}")
    print(f"Только время: {format_datetime(current, '%H:%M:%S')}")

    print("\n" + "-" * 40)
    print("ПАРСИНГ РАЗЛИЧНЫХ ФОРМАТОВ ДАТ:")
    print("-" * 40)

    # Примеры различных форматов дат
    date_examples = [
        "2024-03-15 14:30:25",
        "15.03.2024 14:30:25",
        "03/15/2024 14:30:25",
        "2024-03-15",
        "15.03.2024",
        "14:30:25",
        "2024-03-15 14:30",
    ]

    for date_str in date_examples:
        try:
            dt_obj = parse_datetime_from_string(date_str)
            print(f"'{date_str}' -> {dt_obj}")
        except Exception as e:
            print(f"'{date_str}' -> Ошибка: {e}")

    print("\n" + "-" * 40)
    print("РАБОТА С КОНКРЕТНЫМИ ФОРМАТАМИ:")
    print("-" * 40)

    # Пример с конкретными форматами
    custom_date = "15-03-2024 14:30"
    custom_formats = ["%d-%m-%Y %H:%M", "%Y-%m-%d %H:%M"]

    try:
        dt_obj = parse_datetime_with_formats(custom_date, custom_formats)
        print(f"'{custom_date}' -> {dt_obj} (распознано с первым форматом)")
    except Exception as e:
        print(f"'{custom_date}' -> Ошибка: {e}")


# Тестирование функций
if __name__ == "__main__":
    # Основное тестирование
    test_dates = [
        "2024-03-15 14:30:25",
        "15.03.2024",
        "14:30:25",
        "invalid-date-string",
    ]

    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ФУНКЦИИ ПАРСИНГА ДАТ")
    print("=" * 60)

    for date_str in test_dates:
        try:
            result = parse_datetime_from_string(date_str)
            print(f"✓ '{date_str}' -> {result}")
        except Exception as e:
            print(f"✗ '{date_str}' -> Ошибка: {e}")

    # Демонстрация
    datetime_demo()

    # Дополнительная информация
    print("\n" + "=" * 60)
    print("ДОПОЛНИТЕЛЬНАЯ ИНФОРМАЦИЯ")
    print("=" * 60)
    print("Для использования автоматического парсинга установите:")
    print("pip install python-dateutil")
    print("Или используйте parse_datetime_with_formats() с явными форматами")
