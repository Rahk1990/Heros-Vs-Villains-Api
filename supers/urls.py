
from django.urls import path
from . import views

urlpatterns = [
    path('', views.supers),  # Gettting and Adding
    path('<int:pk>/', views.supers_detail),  # Update, delete
] 
    