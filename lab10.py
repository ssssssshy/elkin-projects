"""Лабораторная работа №10
ВИЗУАЛИЗАЦИЯ РЕЗУЛЬТАТОВ РАБОТЫ
МАТЕМАТИЧЕСКИХ АЛГОРИТМОВ
С ИСПОЛЬЗОВАНИЕМ NUMPY И MATPLOTLIB.
.Написать функцию, которая создает массивы из десяти
нулей, единиц и пятерок."""

import numpy as np


def create_arrays():
    """
    Создает массивы из десяти нулей, единиц и пятерок.

    Returns:
        tuple: три массива (zeros, ones, fives)
    """
    zeros = np.zeros(10)
    ones = np.ones(10)
    fives = np.full(10, 5)

    return zeros, ones, fives


# Простой вывод результатов
if __name__ == "__main__":
    zeros, ones, fives = create_arrays()

    print("Массив из 10 нулей:")
    print(zeros)
    print("\nМассив из 10 единиц:")
    print(ones)
    print("\nМассив из 10 пятерок:")
    print(fives)
