"""KinoCMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from cinema.views import kino_cms, movies, soon, cinemas_page, showtimes, film_card
from pages.views import site_promos, promo_card, site_news, site_contact, site_vip, site_advertiser, site_children_room
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
    path('adminlte/', include('adminLte.urls')),
    path('', kino_cms, name='kino_cms'),
    path('movies/', movies, name='movies'),
    path('soon/', soon, name='soon'),
    path('cinemas/', cinemas_page, name='cinemas_page'),
    path('showtimes/', showtimes, name='showtimes'),
    path('film/<int:film_id>', film_card, name='film_card'),
    path('promos/', site_promos, name='site_promos'),
    path('promo/<int:promo_id>', promo_card, name='promo_card'),
    path('news/', site_news, name='site_news'),
    path('contacts/', site_contact, name='site_contact'),
    path('vip_hall/', site_vip, name='site_vip'),
    path('advertiser/', site_advertiser, name='site_advertiser'),
    path('children_room/', site_children_room, name='site_children_room'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)