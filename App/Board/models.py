from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_resized import ResizedImageField

CITY_SELECT = (

)

CATEGORY_SELECT = (
    ('Категория 1', 'Категория 1'),
    ('Категория 2', 'Категория 2'),
    ('Категория 3', 'Категория 3'),
    ('Категория 4', 'Категория 4'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, verbose_name=u'Имя')
    avatar = ResizedImageField(size=[360, 360], crop=['middle', 'center'], verbose_name=u'Аватар', blank=True)
    city = models.CharField(max_length=20, choices=CITY_SELECT, default='Не выбрано', verbose_name=u'Город')
    phone = models.CharField(max_length=20, verbose_name=u'Телефон', blank=True)
    email = models.EmailField(max_length=100, verbose_name=u'E-mail')

    def __str__(self):
        return self.user.username


class Advertisement(models.Model):
    author_id = models.IntegerField(verbose_name=u'ID автора')
    header = models.CharField(max_length=140, verbose_name=u'Заголовок')
    price = models.IntegerField(verbose_name=u'Цена', blank=True)
    photo = ResizedImageField(size=[500, 500], verbose_name=u'Фото', blank=True)
    description = models.TextField(verbose_name=u'Описание')
    objects_in_box = models.IntegerField(verbose_name=u'Колиество товара в коробке')
    boxes_count = models.IntegerField(verbose_name=u'Колиество коробок')
    category = models.CharField(max_length=100, choices=CATEGORY_SELECT, default='Не выбрано', verbose_name=u'Категория')
    city = models.CharField(max_length=20, choices=CITY_SELECT, default='Не выбрано', verbose_name=u'Город')
    public_date = models.DateField(auto_now=True, verbose_name=u'Дата публикации')
    end_date = models.DateField(verbose_name=u'Дата окончания', blank=True)
    active = models.BooleanField(default=True, verbose_name=u'Активное объявление')
    moderated = models.BooleanField(default=False, verbose_name=u'Прошел модерацию')

    def __str__(self):
        return self.header


class City(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'Название')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'Название')

    def __str__(self):
        return self.name