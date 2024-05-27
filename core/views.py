from django.shortcuts import render

from .forms import QuestionForm
from tags.models import Tag
from questions.models import Question

# Create your views here.
def index(request):
    return render(request, "core/homepage.html")

def ask_question_view(request):
    form = QuestionForm()
    tags = Tag.objects.all()
    context = {"form": form, "tags":tags}
    return render(request, "core/ask.html", context)

def question_view(request, ID):
    question = Question.objects.get(id = ID)
    #answers = 
    context = {"question":question}
    return render(request,"core/question.html", context)
