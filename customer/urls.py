from django.urls import path, include
from rest_framework import routers
from .views import *
from . import views


router = routers.DefaultRouter()
router.register(r'new', Serializers_viewsets)
urlpatterns = [
     path('',include(router.urls)),
     path('',views.index, name='index'),
     path('profile/', views.index, name='profile-index'),
     path('profile/faq', views.faq, name='faq'),
     path('profile/about', views.about, name='about'),
     path('profile/contact', views.contact, name='contact'),
     path('profile/blog', views.blog, name='blog'),
     path('api-auth/',include('rest_framework.urls'))
]