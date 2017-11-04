from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

from Board.views import home, signup

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'signup$', signup, name='signup'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)