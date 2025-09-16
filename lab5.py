"""Лабораторная работа №5
РАБОТА С ФАЙЛАМИ. РАЗРАБОТКА
СИНТАКСИЧЕСКОГО АНАЛИЗАТОРА. ВЫВОД
ФОРМАТИРОВАННЫХ ДАННЫХ В ФОРМАТЕ JSON.
Написать функцию, которая принимает путь к файлу и
количество строк, которые требуется прочитать и возвращает
считанные строки в файле.
"""


def read_file_lines(file_path, num_lines):
    """
    Читает указанное количество строк из файла.

    Args:
        file_path: путь к файлу
        num_lines: количество строк для чтения

    Returns:
        list: список прочитанных строк
    """
    lines = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for i in range(num_lines):
                line = file.readline()
                if not line:
                    break
                lines.append(line.strip())
    except FileNotFoundError:
        print(f"Ошибка: файл {file_path} не найден")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")

    return lines


# Пример использования
if __name__ == "__main__":
    # Читаем 5 строк из файла
    result = read_file_lines("test.txt", 5)

    # Выводим результат
    print("Прочитанные строки:")
    for i, line in enumerate(result, 1):
        print(f"{i}: {line}")
