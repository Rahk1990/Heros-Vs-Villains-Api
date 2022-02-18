
from django.urls import path
from . import views

urlpatterns = [
    path('', views.supers),
    path('villains/', views.get_all_villains),
    path('heros/', views.get_all_hero),
] 
    