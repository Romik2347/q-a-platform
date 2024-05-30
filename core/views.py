from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator

from .forms import QuestionForm

from tags.models import Tag
from questions.models import Question
from accounts.models import User

@login_required
def index(request):
    questions = Question.objects.all().only("id", "title","timestamp")
    paginator = Paginator(questions, 5)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"questions":questions}
    return render(request, "core/index.html", context)

@login_required
def ask_question_view(request):
    form = QuestionForm()
    tags = Tag.objects.all()
    context = {"form": form, "tags":tags}
    return render(request, "core/ask.html", context)

@login_required
def question_view(request, ID):
    question = Question.objects.get(id = ID)
    answers = question.answers.all()
    context = {"question":question, "answers":answers}
    return render(request,"core/question.html", context)

@login_required
def profile_view(request, username):
    user = User.objects.get(username = username)
    context = {"user":user}
    return render(request, "core/profile.html", context)

def login_view(request):
    return render(request, "core/login.html")

def signup_view(request):
    return render(request, "core/signup.html")