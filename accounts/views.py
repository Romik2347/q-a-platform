from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.db import IntegrityError
from django.contrib import messages
from .models import User

#from .utils import parse_fullname

def signup_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            return HttpResponseRedirect(reverse("core:login_view"))
        except IntegrityError:
            messages.add_message(request, messages.INFO, "Username already taken.")
            return HttpResponseRedirect(reverse("core:signup_view"))

    messages.add_message(request, messages.INFO, "No other than POST method is allowed.")
    return HttpResponseRedirect(reverse("core:signup_view"))


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        
        
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("core:index"))

        #return HttpResponseRedirect(reverse("core:login_view", kwargs={"message":"Invalid Credentials."}))
        messages.add_message(request, messages.INFO, "Invalid Credentials.")
        return HttpResponseRedirect(reverse("core:login_view"))

        
    else:
        messages.add_message(request, messages.INFO, "No other than POST method is allowed.")
        return HttpResponseRedirect(reverse("core:login_view"))



def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("core:login_view"))