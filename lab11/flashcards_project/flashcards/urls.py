from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.add_card, name="add_card"),
    path("study/", views.study, name="study"),
    path(
        "delete/<int:card_id>/", views.delete_card, name="delete_card"
    ),  # ← ДОБАВЬТЕ ЭТУ СТРОЧКУ
]
