from django.urls import path
from .views import add_news_promo, news, delete_news_promo, news_promo_update, promos

urlpatterns = [
    path('addnewspromo/<str:form_type>', add_news_promo, name='add_news_promo'),
    path('news/', news, name='news'),
    path('deletenews/<int:news_promo_id>', delete_news_promo, name='delete_news_promo'),
    path('updetenewspromo/<int:news_promo_id>', news_promo_update, name='update_news_promo'),
    path('promos/', promos, name='promos')
]
