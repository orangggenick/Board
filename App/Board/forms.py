from django.contrib.auth.models import User
from django.forms import ModelForm, forms
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget

from Board.models import Profile, Advertisement, Search, Feedback


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
        exclude = ['author_id', 'public_date', 'moderated', 'views']


class SearchForm(ModelForm):
    class Meta:
        model = Search
        fields = '__all__'


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'


class CaptchaForm(forms.Form):
    captcha = ReCaptchaField(widget=ReCaptchaWidget())