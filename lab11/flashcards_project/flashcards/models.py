from django.db import models


class Flashcard(models.Model):
    question = models.CharField(max_length=200, verbose_name="Вопрос")
    answer = models.TextField(verbose_name="Ответ")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question[:50]  # Показываем первые 50 символов вопроса
