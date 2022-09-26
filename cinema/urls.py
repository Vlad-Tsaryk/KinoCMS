from django.urls import path
from .views import films, add_film, film_update, add_cinema, cinemas, cinema_update, add_hall, delete_hall,\
    hall_update, delete_cinema

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('films/', films, name='films'),
    path('films/addfilm/', add_film, name='add_film'),
    path('films/edit/<int:film_id>/', film_update, name='film_update'),
    path('cinemas/', cinemas, name='cinemas'),
    path('cinemas/addcinema/', add_cinema, name='add_cinema'),
    path('cinemas/edit/<int:cinema_id>', cinema_update, name='cinema_update'),
    path('cinemas/addhall/<int:cinema_id>', add_hall, name='add_hall'),
    path('cinemas/updatehall/<int:cinema_id>/<int:hall_id>', hall_update, name='hall_update'),
    path('cinemas/deletehall/<int:cinema_id>/<int:hall_id>', delete_hall, name='delete_hall'),
    path('cinemas/deletecinema/<int:cinema_id>', delete_cinema, name='delete_cinema'),

]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
