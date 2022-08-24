from django.urls import path
from .views import add_news_promo, news, delete_news_promo, news_promo_update, promos, add_main_page, update_main_page,\
    pages, add_page, update_page, delete_page, contact_page

urlpatterns = [
    path('add/<str:form_type>', add_news_promo, name='add_news_promo'),
    path('news/', news, name='news'),
    path('news/delete/<int:news_promo_id>', delete_news_promo, name='delete_news_promo'),
    path('newspromo/updete/<int:news_promo_id>', news_promo_update, name='update_news_promo'),
    path('promos/', promos, name='promos'),
    path('mainpage/add/', add_main_page, name='add_main_page'),
    path('mainpage/update/<int:main_page_id>', update_main_page, name='update_main_page'),
    path('', pages, name='pages'),
    path('page/add/', add_page, name='add_page'),
    path('page/update/<int:page_id>', update_page, name='update_page'),
    path('page/delete/<int:page_id>', delete_page, name='delete_page'),
    path('page/contact/', contact_page, name='contact_page'),
]
