from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('category/accessories', views.accessories, name='accessories'),
    path('category/apparel', views.apparel, name='apparel'),
    path('category/perfume', views.perfume, name='perfume'),
    path('category/shoes', views.shoes, name='shoes'),
]