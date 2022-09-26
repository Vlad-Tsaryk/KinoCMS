from django.urls import path
from django.urls import path, include
from .views import statistic

urlpatterns = [

    path('', statistic, name='statistic'),
    path('', include('cinema.urls')),
    path('banners/', include('baners.urls')),
    path('pages/', include('pages.urls')),
    path('user/', include('users.urls')),
]
