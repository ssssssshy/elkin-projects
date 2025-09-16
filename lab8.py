"""Лабораторная работа №8
ОБРАБОТКА ИЗОБРАЖЕНИЙ С ПРИМЕНЕНИЕМ
БИБЛИОТЕКИ PIL.
Написать функцию, которая принимает путь к изобра-
жению и конвертирует его в формат .ICO, сохраняя её по тому
же пути, что и исходное изображение."""

import os
from PIL import Image


def convert_to_ico(image_path):
    """
    Конвертирует изображение в формат .ICO

    Args:
        image_path: путь к исходному изображению
    """
    try:
        # Открываем изображение
        with Image.open(image_path) as img:
            # Создаем путь для сохранения .ico файла
            base_name = os.path.splitext(image_path)[0]
            ico_path = base_name + ".ico"

            # Конвертируем и сохраняем в .ico
            img.save(ico_path, format="ICO")

            print(f"Изображение успешно конвертировано: {ico_path}")

    except Exception as e:
        print(f"Ошибка при конвертации: {e}")


# Пример использования
if __name__ == "__main__":
    # Укажите путь к вашему изображению
    image_path = "example.png"  # Можно изменить на свой путь

    # Проверяем, существует ли файл
    if os.path.exists(image_path):
        convert_to_ico(image_path)
    else:
        print(f"Файл {image_path} не найден!")
        print("Создайте файл example.png или укажите правильный путь")
