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

class City(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'Название')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'Название')

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'Название')
    image = ResizedImageField(size=[500, 500], verbose_name=u'Картинка', blank=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, verbose_name=u'Имя')
    avatar = ResizedImageField(size=[360, 360], crop=['middle', 'center'], verbose_name=u'Аватар', blank=True)
    city = models.ForeignKey(City, verbose_name=u'Город')
    phone = models.CharField(max_length=20, verbose_name=u'Телефон', blank=True, null=True)
    email = models.EmailField(max_length=100, verbose_name=u'E-mail')

    def __str__(self):
        return self.user.username


class Advertisement(models.Model):
    author_id = models.IntegerField(verbose_name=u'ID автора')
    header = models.CharField(max_length=140, verbose_name=u'Заголовок')
    price = models.IntegerField(verbose_name=u'Цена', blank=True, null=True)
    photo = ResizedImageField(size=[500, 500], verbose_name=u'Фото', blank=True)
    description = models.TextField(verbose_name=u'Описание')
    objects_in_box = models.IntegerField(verbose_name=u'Колиество бонусов')
    boxes_count = models.IntegerField(verbose_name=u'Количество карточек/купонов')
    category = models.ForeignKey(Category, verbose_name=u'Категория')
    city = models.ForeignKey(City, verbose_name=u'Город')
    shop = models.ForeignKey(Shop, verbose_name=u'Магазин')
    public_date = models.DateField(auto_now=True, verbose_name=u'Дата публикации')
    begin_date = models.DateField(verbose_name=u'Дата начала действия', blank=True, null=True)
    end_date = models.DateField(verbose_name=u'Дата окончания действия', blank=True, null=True)
    active = models.BooleanField(default=True, verbose_name=u'Активное объявление')
    moderated = models.BooleanField(default=False, verbose_name=u'Прошел модерацию')

    def __str__(self):
        return self.header