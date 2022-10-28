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
from cinema.views import kino_cms, movies, soon, cinemas_page, showtimes, film_card, seat_reservation, hall_card, \
    cinema_card, search
from pages.views import site_promos, news_promo_card, site_news, site_contact, site_other_page, site_mobile_app
from users.views import login_page, create_user, logout_user, update_user
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
                  path('__debug__/', include('debug_toolbar.urls')),
                  path('admin/', admin.site.urls),
              ] + i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('adminlte/', include('adminLte.urls')),
    path('', kino_cms, name='kino_cms'),
    path('movies/', movies, name='movies'),
    path('soon/', soon, name='soon'),
    path('cinemas/', cinemas_page, name='cinemas_page'),
    path('showtimes/', showtimes, name='showtimes'),
    path('reservation/<int:session_id>', seat_reservation, name='reservation'),
    path('film/<int:film_id>', film_card, name='film_card'),
    path('hall/<int:hall_id>', hall_card, name='hall_card'),
    path('cinema/<int:cinema_id>', cinema_card, name='cinema_card'),
    path('promos/', site_promos, name='site_promos'),
    path('news_promo/<int:news_promo_id>', news_promo_card, name='news_promo_card'),
    path('other_page/<int:page_id>', site_other_page, name='other_page'),
    path('news/', site_news, name='site_news'),
    path('contacts/', site_contact, name='site_contact'),
    path('mobile_app/', site_mobile_app, name='site_mobile_app'),
    path('register/', create_user, name='register'),
    path('update/<int:user_id>', update_user, {'admin': False}, name='site_user_update'),
    path('logout/', logout_user, name='logout'),
    path('login/', login_page, name='login_page'),
    path('search/', search, name='search'),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
