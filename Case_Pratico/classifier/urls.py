from django.urls import path
from . import views

urlpatterns = [
    path('', views.renderHomePage, name='home'),
    path('email/enviar/', views.receiveEmail, name='receive_email'),
]