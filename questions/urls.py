from django.urls import path

from . import views

app_name = "questions"

urlpatterns = [
    path("", views.QuestionView.as_view()),
    path("<int:ID>", views.QuestionView.as_view())
]
