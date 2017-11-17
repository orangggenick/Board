import datetime
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, render_to_response
from django.template.context_processors import csrf
from django.db.models import Q

from Board.forms import ProfileForm, AdvertisementForm, SearchForm
from Board.models import Advertisement, City, Category, Shop


def home(request):
    advertisements = Advertisement.objects.filter(moderated=True).filter(Q(end_date__gt=datetime.datetime.now()) | Q(end_date=None))
    return render(request, 'Board/home.html', {'advertisements': advertisements, 'form': SearchForm()})


def signup(request):
    if auth.get_user(request).id is not None:
        return redirect('/profile/' + str(auth.get_user(request).id))
    else:
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
                    return render(request, 'Board/signup.html', {'user_form': user_form, 'profile_form': profile_form})
            else:
                return render(request, 'Board/signup.html', {'user_form': user_form, 'profile_form': profile_form, 'cities':City.objects.all()})
        else:
            return render(request, 'Board/signup.html', {'user_form': user_form, 'profile_form': profile_form, 'cities':City.objects.all()})


def login(request):
    if auth.get_user(request).id is not None:
        return redirect('/profile/' + str(auth.get_user(request).id))
    else:
        args = {}
        args.update(csrf(request))
        if request.POST:
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                args['login_error'] = "Пользователь не найден!"
                return render_to_response('Board/login.html', args)
        else:
            return render_to_response('Board/login.html', args)


def logout(request):
    if auth.get_user(request).id is not None:
        auth.logout(request)
        return redirect("/")
    else:
        return redirect("/")


def profile(request, user_id):
    if auth.get_user(request).id is not None:
        if int(user_id) == int(request.user.id):
            advertisements = Advertisement.objects.filter(author_id=user_id)
            active = advertisements.filter(moderated=True).filter(Q(end_date__gt=datetime.datetime.now()) | Q(end_date=None))
            end = advertisements.filter(end_date__lte = datetime.datetime.now())
            waiting = advertisements.filter(moderated=False)
            categories = Category.objects.all()
            form = AdvertisementForm()
            return render(request, 'Board/profile.html', {'user': User.objects.get(id=user_id), 'active': active, 'end': end, 'waiting': waiting, 'form': form, 'categories': categories})
        else:
            active = Advertisement.objects.filter(author_id=user_id).filter(moderated=True).filter(Q(end_date__gt=datetime.datetime.now()) | Q(end_date=None))
            return render(request, 'Board/profile.html', {'user': User.objects.get(id=user_id), 'active': active})
    else:
        active = Advertisement.objects.filter(author_id=user_id).filter(moderated=True).filter(Q(end_date__gt=datetime.datetime.now()) | Q(end_date=None))
        return render(request, 'Board/profile.html', {'user': User.objects.get(id=user_id), 'active': active})


def add(request):
    if auth.get_user(request).id is not None:
        form = AdvertisementForm()
        if request.POST:
            form = AdvertisementForm(request.POST, request.FILES)
            if form.is_valid():
                buffer = form.save(commit=False)
                if buffer.begin_date is not None and buffer.end_date is not None:
                    if buffer.begin_date < buffer.end_date:
                        buffer.author_id = auth.get_user(request).id
                        form.save()
                        return redirect('/profile/'+str(auth.get_user(request).id))
                    else:
                        form.add_error('end_date', 'Некорректная дата окончания')
                        return render(request, 'Board/add.html', {'form': form, 'categories': Category.objects.all()})
                else:
                    buffer = form.save(commit=False)
                    buffer.author_id = auth.get_user(request).id
                    form.save()
                    return redirect('/profile/' + str(auth.get_user(request).id))
            else:
                return render(request, 'Board/add.html', {'form': form, 'categories': Category.objects.all()})
        else:
            return render(request, 'Board/add.html', {'form': form, 'categories': Category.objects.all()})
    else:
        return redirect("/login")


def advertisement(request, advertisement_id):
    advertisement = Advertisement.objects.get(id=advertisement_id)
    user =  User.objects.get(id=advertisement.author_id)
    return render(request, 'Board/advertisement.html', {'advertisement': advertisement, 'user': user})


def edit(request, advertisement_id):
    if auth.get_user(request).id is not None:
        advertisement = Advertisement.objects.get(id=advertisement_id)
        categories = Category.objects.all()
        cities = City.objects.all()
        shops = Shop.objects.all()
        if advertisement.author_id == auth.get_user(request).id:
            if request.POST:
                form = AdvertisementForm(request.POST, request.FILES)
                if form.is_valid():
                    buffer = form.save(commit=False)
                    advertisement.header = buffer.header
                    advertisement.description = buffer.description
                    advertisement.objects_in_box = buffer.objects_in_box
                    advertisement.boxes_count = buffer.boxes_count
                    advertisement.price = buffer.price
                    advertisement.city = buffer.city
                    advertisement.category = buffer.category
                    advertisement.shop = buffer.shop
                    advertisement.begin_date = buffer.begin_date
                    advertisement.end_date = buffer.end_date
                    if buffer.photo != '':
                        advertisement.photo = buffer.photo
                    advertisement.moderated = False
                    advertisement.save()
                    return redirect('/profile/' + str(auth.get_user(request).id))
                else:
                    return render(request, 'Board/edit.html',{'advertisement': advertisement, 'categories': categories, 'cities': cities, 'shops': shops, 'form': form})
            else:
                form = AdvertisementForm()
                return render(request, 'Board/edit.html', {'advertisement': advertisement, 'categories': categories, 'cities': cities, 'shops': shops, 'form': form})
        else:
            raise PermissionDenied
    else:
        return redirect("/login")


def search(request):
    if request.POST:
        form = SearchForm(request.POST)
        if form.is_valid():
            buffer = form.save(commit=False)
            print(buffer.city)
            advertisements = Advertisement.objects.filter(moderated=True).filter(Q(end_date__gt=datetime.datetime.now()) | Q(end_date=None))
            if buffer.city is not None:
                advertisements = advertisements.filter(city=buffer.city)
            if buffer.category is not None:
                advertisements = advertisements.filter(category=buffer.category)
            if buffer.shop is not None:
                advertisements = advertisements.filter(shop=buffer.shop)
            return render(request, 'Board/search.html', {'advertisements': advertisements, 'form': form})
        return redirect('/')
    return redirect('/')