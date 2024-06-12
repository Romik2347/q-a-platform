from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
 path("", views.index, name = "index"),
 path("ask/", views.ask_question_view, name = "ask_question_view"),
 path("edit/<int:ID>", views.question_edit, name = "edit_question_view"),
 path("question/<int:ID>", views.question_view, name = "question_view"),
 path("tag/<str:tag>", views.tags_view, name ="tags_view"),
 path("profile/<str:username>", views.profile_view, name ="profile_view"),
 path("login/", views.login_view, name = "login_view"),
 path("signup/", views.signup_view, name = "signup_view"),
 path("questions-staff/", views.staff_index_page, name = "staff_questions")
]
