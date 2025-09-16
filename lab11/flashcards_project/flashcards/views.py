from django.shortcuts import render, redirect, get_object_or_404
from .models import Flashcard
from .forms import FlashcardForm


def home(request):
    """Главная страница со списком карточек"""
    cards = Flashcard.objects.all().order_by("-created_at")
    return render(request, "home.html", {"cards": cards})


def add_card(request):
    """Добавление новой карточки"""
    if request.method == "POST":
        form = FlashcardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = FlashcardForm()

    return render(request, "add_card.html", {"form": form})


def study(request):
    """Режим изучения карточек"""
    cards = Flashcard.objects.all()
    return render(request, "study.html", {"cards": cards})


def delete_card(request, card_id):
    """Удаление карточки"""
    card = get_object_or_404(Flashcard, id=card_id)
    card.delete()
    return redirect("home")
