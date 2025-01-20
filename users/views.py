from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import login as django_login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def sign_up(request):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        form.save()
        return redirect(settings.LOGIN_URL)
    else:
        form = UserCreationForm()

    context = {"form": form}
    return render(request, 'registration/sign_up.html', context)


def login(request):
    form = AuthenticationForm(request.POST or None)
    if form.is_valid():
        django_login(request, form.get_user())
        return redirect('/todo_list/')
    else:
        context = {'form':form}
        return render(request, 'registration/login.html', context)


