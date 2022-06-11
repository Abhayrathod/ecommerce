from django.urls import path
from . import views

urlpatterns = [
     path('profile/', views.index, name='profile-index'),
     path('profile/faq', views.faq, name='faq'),
     path('profile/about', views.about, name='about'),
     path('profile/contact', views.contact, name='contact'),
     path('profile/blog', views.blog, name='blog'),
]