from django.contrib.auth.models import User
from django.forms import ModelForm

from Board.models import Profile


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar', 'city', 'phone')
