from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
 path("", views.index, name = "index"),
 path("ask-question/", views.ask_question_view, name = "ask_question_view"),
 path("question/<int:ID>", views.question_view, name = "question_view"),
 path("profile/<str:username>", views.profile_view, name ="profile_view")
]
