from django.urls import path
from .views import baners
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('edit/', baners, name='banners')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)