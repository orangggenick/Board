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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = ResizedImageField(size=[360, 360], verbose_name=u'Аватар', blank=True)
    city = models.CharField(max_length=20, choices=CITY_SELECT, default='Не выбрано', blank=True)
    phone = models.CharField(max_length=20, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
