from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

from Board.views import home, signup, logout, login, profile, add, advertisement, edit, search, editProfile, end, \
    feedback, deleteProfile

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'signup$', signup, name='signup'),
    url(r'logout$', logout, name='logout'),
    url(r'login$', login, name='login'),
    url(r'profile/(?P<user_id>\d+)$', profile, name='profile'),
    url(r'profile/(?P<user_id>\d+)/edit$', editProfile, name='editProfile'),
    url(r'profile/(?P<user_id>\d+)/delete$', deleteProfile, name='deleteProfile'),
    url(r'add$', add, name='add'),
    url(r'advertisement/(?P<advertisement_id>\d+)$', advertisement, name='advertisement'),
    url(r'advertisement/(?P<advertisement_id>\d+)/edit$', edit, name='edit'),
    url(r'advertisement/(?P<advertisement_id>\d+)/end$', end, name='edit'),
    url(r'search$', search, name='search'),
    url(r'feedback$', feedback, name='feedback'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)