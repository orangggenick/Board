from django.contrib.auth.models import User
from django.forms import ModelForm

from Board.models import Profile, Advertisement


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password']


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'city', 'phone', 'first_name', 'email']


class AdvertisementForm(ModelForm):
    class Meta:
        model = Advertisement
        exclude = ['author_id', 'public_date', 'active', 'moderated']
