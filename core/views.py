from django.shortcuts import render

from .forms import QuestionForm

# Create your views here.
def index(request):
    return render(request, "core/homepage.html")

def questionForm_view(request):
    form = QuestionForm()
    context = {"form": form}
    return render(request, "core/ask.html", context)