from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
 path("", views.index, name = "index"),
 path("ask-question/", views.questionForm_view, name = "ask_question")
]
