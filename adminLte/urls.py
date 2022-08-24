from django.urls import path
from .views import statistic

urlpatterns = [
    path('', statistic, name='statistic')
]
