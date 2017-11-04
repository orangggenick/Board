from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from Board.forms import UserForm, ProfileForm


def home(request):
    return render(request, 'Board/home.html')


def signup(request):
    user_form = UserCreationForm()
    profile_form = ProfileForm()
    if request.POST:
        user_form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            user = auth.authenticate(username=user_form.cleaned_data['username'], password=user_form.cleaned_data['password2'])
            auth.login(request, user)
            if profile_form.is_valid():
                buffer = profile_form.save(commit=False)
                buffer.user = auth.get_user(request)
                profile_form.save()
                return redirect('/')
        else:
            return render(request, 'Board/signup.html', {'user_form': user_form, 'profile_form': profile_form})
    else:
        return render(request, 'Board/signup.html', {'user_form': user_form, 'profile_form': profile_form})
