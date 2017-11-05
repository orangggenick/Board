from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, render_to_response
from django.template.context_processors import csrf

from Board.forms import UserForm, ProfileForm
from Board.models import Advertisement, City


def home(request):
    return render(request, 'Board/home.html')


def signup(request):
    user_form = UserCreationForm()
    profile_form = ProfileForm()
    if request.POST:
        user_form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
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
            return render(request, 'Board/signup.html', {'user_form': user_form, 'profile_form': profile_form, 'cities':City.objects.all()})
    else:
        return render(request, 'Board/signup.html', {'user_form': user_form, 'profile_form': profile_form, 'cities':City.objects.all()})


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            args['login_error'] = "Пользователь не найден!"
            return render_to_response('Board/login.html', args)
    else:

        return render_to_response('Board/login.html', args)


def logout(request):
    auth.logout(request)
    return redirect("/")


def profile(request, user_id):
    return render(request, 'Board/profile.html', {'user':User.objects.get(id=user_id), 'advertisements': Advertisement.objects.filter(author_id=user_id)})