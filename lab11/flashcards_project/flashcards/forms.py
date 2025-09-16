from django import forms
from .models import Flashcard  # ← ТОЛЬКО ЭТОТ ИМПОРТ


class FlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ["question", "answer"]
        widgets = {
            "question": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Введите вопрос"}
            ),
            "answer": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите ответ",
                    "rows": 3,
                }
            ),
        }
