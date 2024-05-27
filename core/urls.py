from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
 path("", views.index, name = "index"),
 path("ask-question/", views.ask_question_view, name = "ask_question"),
 path("question/<int:ID>", views.question_view, name = "question_view")
]
