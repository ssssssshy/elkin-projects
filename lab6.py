"""Лабораторная работа №6
РАЗРАБОТКА ПРИЛОЖЕНИЯ РАБОТЫ С БАЗОЙ
ДАННЫХ.
Написать функцию, которая принимает наименование
таблицы и выводит количество одинаковых значений в её по-
лях и наиболее часто повторяющееся значение полей."""

import sqlite3


def count_values(table_name):
    """
    Подсчитывает количество одинаковых значений в полях таблицы
    и находит наиболее часто повторяющиеся значения.

    Args:
        table_name: наименование таблицы
    """
    try:
        # Подключаемся к базе данных
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        # Получаем информацию о столбцах таблицы
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = [column[1] for column in cursor.fetchall()]

        print(f"Таблица: {table_name}")
        print("=" * 50)

        # Для каждого столбца считаем повторяющиеся значения
        for column in columns:
            # Запрос для подсчета повторяющихся значений
            query = f"""
            SELECT {column}, COUNT(*) as count 
            FROM {table_name} 
            GROUP BY {column} 
            ORDER BY count DESC
            """

            cursor.execute(query)
            results = cursor.fetchall()

            print(f"\nСтолбец: {column}")
            print("-" * 30)

            if results:
                # Выводим все значения и их количество
                for value, count in results:
                    print(f"{value}: {count} раз")

                # Наиболее часто повторяющееся значение
                most_common_value, most_common_count = results[0]
                print(
                    f"Наиболее частое значение: '{most_common_value}' ({most_common_count} раз)"
                )
            else:
                print("Нет данных")

            print()

        # Закрываем соединение
        conn.close()

    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
    except Exception as e:
        print(f"Ошибка: {e}")


# Создаем тестовую базу данных и таблицу
def create_test_database():
    """
    Создает тестовую базу данных с примером таблицы.
    """
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        # Создаем таблицу
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            grade TEXT,
            city TEXT
        )
        """)

        # Очищаем таблицу перед добавлением новых данных
        cursor.execute("DELETE FROM students")

        # Добавляем тестовые данные
        students_data = [
            ("Иван", 20, "A", "Москва"),
            ("Мария", 21, "B", "Санкт-Петербург"),
            ("Алексей", 20, "A", "Москва"),
            ("Елена", 22, "C", "Казань"),
            ("Иван", 19, "B", "Москва"),
            ("Ольга", 20, "A", "Санкт-Петербург"),
            ("Дмитрий", 21, "B", "Москва"),
            ("Мария", 20, "C", "Казань"),
            ("Алексей", 22, "A", "Москва"),
            ("Иван", 21, "B", "Санкт-Петербург"),
        ]

        cursor.executemany(
            "INSERT INTO students (name, age, grade, city) VALUES (?, ?, ?, ?)",
            students_data,
        )

        conn.commit()
        conn.close()
        print("Тестовая база данных создана успешно!")

    except sqlite3.Error as e:
        print(f"Ошибка при создании базы данных: {e}")


# Основная программа
if __name__ == "__main__":
    # Создаем тестовую базу данных
    create_test_database()

    # Анализируем таблицу
    count_values("students")
