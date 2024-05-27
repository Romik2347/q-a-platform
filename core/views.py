from django.shortcuts import render

from .forms import QuestionForm
from tags.models import Tag
from questions.models import Question

def index(request):
    questions = Question.objects.all().only("id", "title","timestamp")
    context = {"questions":questions}
    return render(request, "core/index.html", context)

def ask_question_view(request):
    form = QuestionForm()
    tags = Tag.objects.all()
    context = {"form": form, "tags":tags}
    return render(request, "core/ask.html", context)

def question_view(request, ID):
    question = Question.objects.get(id = ID)
    answers = question.answers.all()
    context = {"question":question, "answers":answers}
    return render(request,"core/question.html", context)

def profile_view(request, username):
    pass