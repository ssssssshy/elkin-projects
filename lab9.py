"""Лабораторная работа №9
РАЗРАБОТКА GUI ПРИЛОЖЕНИЯ С ПОМОЩЬЮ
ГРАФИЧЕСКИХ БИБЛИОТЕК.
Написать GUI приложение, которые позволяет про-
сматривать PDF файлы."""

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import os


class SimplePDFViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Простой PDF Просмотрщик")
        self.root.geometry("900x600")

        self.create_widgets()

    def create_widgets(self):
        # Создаем меню
        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Открыть", command=self.open_file)
        file_menu.add_separator()
        file_menu.add_command(label="Выход", command=self.root.quit)
        menubar.add_cascade(label="Файл", menu=file_menu)
        self.root.config(menu=menubar)

        # Панель с кнопками
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        self.open_btn = tk.Button(
            button_frame,
            text="📁 Открыть PDF",
            command=self.open_file,
            font=("Arial", 12),
        )
        self.open_btn.pack(pady=5)

        # Информация о файле
        self.info_label = tk.Label(self.root, text="Файл не выбран", font=("Arial", 10))
        self.info_label.pack(pady=5)

        # Область для текста
        self.text_area = scrolledtext.ScrolledText(
            self.root, wrap=tk.WORD, font=("Courier", 10), bg="white", height=30
        )
        self.text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Статус бар
        self.status_bar = tk.Label(
            self.root, text="Готов", relief=tk.SUNKEN, anchor=tk.W
        )
        self.status_bar.pack(fill=tk.X, side=tk.BOTTOM)

    def open_file(self):
        """Открывает диалог выбора файла"""
        file_path = filedialog.askopenfilename(
            title="Выберите PDF файл",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")],
        )

        if file_path:
            self.display_file_info(file_path)

    def display_file_info(self, file_path):
        """Отображает информацию о файле"""
        try:
            file_name = os.path.basename(file_path)
            file_size = os.path.getsize(file_path)
            file_size_mb = file_size / (1024 * 1024)

            self.info_label.config(
                text=f"Файл: {file_name} | Размер: {file_size_mb:.2f} MB"
            )
            self.status_bar.config(text=f"Загружен: {file_name}")

            # Очищаем текстовую область
            self.text_area.delete(1.0, tk.END)

            # Добавляем информацию о файле
            self.text_area.insert(tk.END, f"Информация о PDF файле:\n")
            self.text_area.insert(tk.END, f"{'=' * 50}\n")
            self.text_area.insert(tk.END, f"Имя файла: {file_name}\n")
            self.text_area.insert(tk.END, f"Размер: {file_size_mb:.2f} MB\n")
            self.text_area.insert(tk.END, f"Полный путь: {file_path}\n")
            self.text_area.insert(tk.END, f"{'=' * 50}\n\n")

            # Проверяем, установлен ли PyMuPDF
            try:
                import fitz

                self.display_pdf_content(file_path)
            except ImportError:
                self.text_area.insert(tk.END, "Библиотека PyMuPDF не установлена!\n\n")
                self.text_area.insert(tk.END, "Чтобы просматривать содержимое PDF:\n")
                self.text_area.insert(tk.END, "1. Установите: uv pip install PyMuPDF\n")
                self.text_area.insert(tk.END, "2. Перезапустите программу\n")

        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось обработать файл: {e}")

    def display_pdf_content(self, file_path):
        """Отображает содержимое PDF если установлен PyMuPDF"""
        try:
            import fitz

            self.text_area.insert(tk.END, "Содержимое PDF:\n")
            self.text_area.insert(tk.END, f"{'=' * 50}\n\n")

            # Открываем PDF и извлекаем текст
            doc = fitz.open(file_path)
            total_pages = len(doc)

            self.text_area.insert(tk.END, f"Всего страниц: {total_pages}\n\n")

            # Показываем текст с первых 3 страниц (чтобы не перегружать)
            for page_num in range(min(3, total_pages)):
                page = doc.load_page(page_num)
                text = page.get_text()

                self.text_area.insert(tk.END, f"--- Страница {page_num + 1} ---\n")
                self.text_area.insert(tk.END, text)
                self.text_area.insert(tk.END, "\n\n")

            if total_pages > 3:
                self.text_area.insert(tk.END, f"... и еще {total_pages - 3} страниц\n")

            doc.close()

        except Exception as e:
            self.text_area.insert(tk.END, f"Ошибка при чтении PDF: {e}\n")


def main():
    root = tk.Tk()
    app = SimplePDFViewer(root)
    root.mainloop()


if __name__ == "__main__":
    main()
