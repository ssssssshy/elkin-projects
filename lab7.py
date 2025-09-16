"""Лабораторная работа №7
РАЗРАБОТКА ПРИЛОЖЕНИЯ С ИСПОЛЬЗОВАНИЕМ
ООП.
Написать класс Exception с возможностью передачи в
него сообщения и реализовать класс, в котором будет пробра-
сываться данный Exception."""


class MyException(Exception):
    """Пользовательское исключение с возможностью передачи сообщения."""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class Calculator:
    """Класс калькулятора, который бросает MyException при ошибках."""

    def divide(self, a, b):
        """Деление двух чисел."""
        if b == 0:
            raise MyException("Ошибка: деление на ноль!")
        return a / b

    def square_root(self, x):
        """Вычисление квадратного корня."""
        if x < 0:
            raise MyException("Ошибка: нельзя извлечь корень из отрицательного числа!")
        return x**0.5


# Пример использования
if __name__ == "__main__":
    calc = Calculator()

    # Тестирование нормальных операций
    try:
        result = calc.divide(10, 2)
        print(f"10 / 2 = {result}")
    except MyException as e:
        print(e.message)

    # Тестирование исключения при делении на ноль
    try:
        calc.divide(10, 0)
    except MyException as e:
        print(e.message)

    # Тестирование нормального извлечения корня
    try:
        result = calc.square_root(16)
        print(f"√16 = {result}")
    except MyException as e:
        print(e.message)

    # Тестирование исключения при извлечении корня из отрицательного числа
    try:
        calc.square_root(-4)
    except MyException as e:
        print(e.message)

    # Дополнительные примеры
    print("\nДополнительные тесты:")

    # Пример с передачей разных сообщений
    try:
        raise MyException("Это кастомное сообщение об ошибке!")
    except MyException as e:
        print(e.message)

    # Пример наследования
    try:
        raise MyException("Еще одно сообщение")
    except Exception as e:  # MyException наследуется от Exception
        print(f"Поймано исключение: {e}")
