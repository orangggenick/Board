from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_resized import ResizedImageField

CITY_SELECT = (
    ('Омск', 'Омск'),
    ('Тара', 'Тара'),
    ('Тюмень', 'Тюмень'),
    ('Новосибирск', 'Новосибирск'),
)

CATEGORY_SELECT = (
    ('Категория 1', 'Категория 1'),
    ('Категория 2', 'Категория 2'),
    ('Категория 3', 'Категория 3'),
    ('Категория 4', 'Категория 4'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = ResizedImageField(size=[360, 360], verbose_name=u'Аватар', blank=True)
    city = models.CharField(max_length=20, choices=CITY_SELECT, default='Не выбрано', verbose_name=u'Город')
    phone = models.CharField(max_length=20, verbose_name=u'Телефон', blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Advertisement(models.Model):
    author_id = models.IntegerField(verbose_name=u'ID автора')
    header = models.CharField(max_length=140, verbose_name=u'Заголовок')
    price = models.IntegerField(verbose_name=u'Цена', blank=True)
    photo = ResizedImageField(size=[500, 500], verbose_name=u'Фото', blank=True)
    description = models.TextField(verbose_name=u'Описание')
    category = models.TextField(max_length=100, choices=CATEGORY_SELECT, default='Не выбрано', verbose_name=u'Категория')
    city = models.CharField(max_length=20, choices=CITY_SELECT, default='Не выбрано', verbose_name=u'Город')
    public_date = models.DateField(auto_now=True, verbose_name=u'Дата публикации')
    active = models.BooleanField(default=True, verbose_name=u'Активное объявление')
    moderated = models.BooleanField(default=False, verbose_name=u'Прошел модерацию')

