from django.contrib.auth.models import User
from django.db import models
from django_resized import ResizedImageField
import datetime


class City(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'Название')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'Название')
    units = models.CharField(max_length=15, verbose_name=u'Единицы измерения')

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'Название')
    image = ResizedImageField(size=[473, 297], crop=['middle', 'center'], verbose_name=u'Фото')

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=13, verbose_name=u'Имя')
    avatar = ResizedImageField(size=[360, 360], crop=['middle', 'center'], verbose_name=u'Аватар', blank=True)
    city = models.ForeignKey(City, verbose_name=u'Город')
    phone = models.CharField(max_length=20, verbose_name=u'Телефон', blank=True, null=True, unique=True)
    email = models.EmailField(max_length=100, verbose_name=u'E-mail', unique=True)
    lastLogin = models.DateTimeField(verbose_name=u'Последний вход', blank=True, null=True)
    lastIP = models.GenericIPAddressField(verbose_name=u'Последний IP входа', blank=True, null=True)
    currentIP = models.GenericIPAddressField(verbose_name=u'Текущий IP входа', blank=True, null=True)

    def __str__(self):
        return self.user.username


class Advertisement(models.Model):
    author_id = models.IntegerField(verbose_name=u'ID автора')
    header = models.CharField(max_length=140, verbose_name=u'Заголовок')
    price = models.PositiveIntegerField(verbose_name=u'Цена', blank=True, null=True)
    photo = ResizedImageField(size=[473, 297], crop=['middle', 'center'], verbose_name=u'Фото', blank=True)
    description = models.TextField(verbose_name=u'Описание')
    objects_in_box = models.IntegerField(verbose_name=u'Количество бонусов')
    category = models.ForeignKey(Category, verbose_name=u'Категория')
    other_category = models.CharField(max_length=40, verbose_name=u'Другая категория', blank=True, null=True)
    city = models.ForeignKey(City, verbose_name=u'Город')
    other_city = models.CharField(max_length=40, verbose_name=u'Другой город', blank=True, null=True)
    shop = models.ForeignKey(Shop, verbose_name=u'Магазин')
    other_shop = models.CharField(max_length=40, verbose_name=u'Другой магазин', blank=True, null=True)
    public_date = models.DateTimeField(verbose_name=u'Дата публикации')
    begin_date = models.DateField(verbose_name=u'Дата начала действия', blank=True, null=True)
    end_date = models.DateField(verbose_name=u'Дата окончания действия', blank=True, null=True)
    views = models.IntegerField(verbose_name=u'Просмотры', default=0)
    moderated = models.BooleanField(default=False, verbose_name=u'Прошел модерацию')


class Search(models.Model):
    category = models.ForeignKey(Category, verbose_name=u'Категория', blank=True, null=True)
    city = models.ForeignKey(City, verbose_name=u'Город', blank=True, null=True)
    shop = models.ForeignKey(Shop, verbose_name=u'Магазин', blank=True, null=True)
    date = models.DateField(verbose_name=u'Дата', blank=True, null=True)


class Feedback(models.Model):
    header = models.CharField(max_length=200, verbose_name=u'Заголовок')
    name = models.CharField(max_length=100, verbose_name=u'Имя')
    email = models.EmailField(max_length=100, verbose_name=u'E-mail')
    phone = models.CharField(max_length=20, verbose_name=u'Телефон', blank=True, null=True)
    message = models.TextField(verbose_name=u'Сообщение')
    screenshot = models.ImageField(verbose_name=u'Скриншот', blank=True, null=True)

    def __str__(self):
        return self.header