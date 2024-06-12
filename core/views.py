from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


from django.core.paginator import Paginator

from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import QuestionForm

from tags.models import Tag
from questions.models import Question, Answer
from accounts.models import User

@login_required
def index(request):
    questions = Question.objects.all().only("id", "title","timestamp").order_by("timestamp").reverse()
    paginator = Paginator(questions, 5)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj":page_obj, "tags":Tag.objects.all()}
    return render(request, "core/index.html", context)

@login_required
def ask_question_view(request):
    form = QuestionForm()
    tags = Tag.objects.all()
    context = {"form": form, "tags":tags}
    return render(request, "core/ask.html", context)

@login_required
def question_view(request, ID):
    question = Question.objects.get(id = ID).order_by("timestamp")
    form = QuestionForm()

    if request.method == "POST":
        form = QuestionForm(request.POST)
        print(form.data)
        answer = Answer.objects.create(user = request.user, question = question, approved=True, content = form.data["content"])
        return HttpResponseRedirect(reverse("core:question_view", kwargs={"ID":ID}))

    answers = question.answers.all()
    context = {"question":question, "answers":answers, "form":form}
    return render(request,"core/question.html", context)

@login_required
def question_edit(request, ID):
    question = Question.objects.get(id = ID).order_by("timestamp")
    form = QuestionForm()
    context = {"question":question,"form":form, "tags":Tag.objects.all()}
    return render(request, "core/edit-question.html", context)

@login_required
def profile_view(request, username):
    user = User.objects.get(username = username)
    context = {"user":user}
    return render(request, "core/profile.html", context)

@login_required
def tags_view(request, tag):
    tag = Tag.objects.get(title = tag)
    questions = Question.objects.filter(tags = tag).order_by("timestamp")

    paginator = Paginator(questions, 5)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj":page_obj, "tags":Tag.objects.all()}
    return render(request,"core/index.html", context)

def login_view(request):
    return render(request, "core/login.html")

def signup_view(request):
    return render(request, "core/signup.html")

@staff_member_required
def staff_index_page(request):
    questions = Question.objects.filter(answered=False).order_by("timestamp")
    tags = Tag.objects.all()
    context = {"questions":questions, "tags":tags}
    return render(request, "core/staff-questions.html", context)

@staff_member_required
def staff_questions_view(request, tag):
    """
    This page is only for staff, 
    where they (the staff) 
    will see a list of questions related to their tag.
    """
    tag = Tag.objects.get(title = tag)
    questions = Question.objects.filter(answered=False).filter(tags = tag).order_by("timestamp")
    tags = Tag.objects.all()
    context = {"questions":questions, "tags":tags}
    return render(request, "core/staff-questions.html", context)