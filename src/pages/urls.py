from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('contact/', views.contact_view ),
    path('about/', views.about_view ),
]
