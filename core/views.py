from django.shortcuts import render

from .forms import QuestionForm
from tags.models import Tag

# Create your views here.
def index(request):
    return render(request, "core/homepage.html")

def questionForm_view(request):
    form = QuestionForm()
    tags = Tag.objects.all()
    context = {"form": form, "tags":tags}
    return render(request, "core/ask.html", context)