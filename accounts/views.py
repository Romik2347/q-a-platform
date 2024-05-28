from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages

def signup_view(request):
    pass

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
        messages.add_message(request, messages.INFO, "No other than POST request is allowed")
        return HttpResponseRedirect(reverse("core:login_view"))



def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("core:login_view"))