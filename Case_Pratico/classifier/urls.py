from django.urls import path
from . import views

urlpatterns = [
    path('', views.renderHomePage, name='home_page'),
    path('ler/', views.renderSendEmail, name='read_email'),
    path('checar', views.receiveEmail, name='check_email'),
    path('enviar/', views.sendEmail, name='send_email'),
    path('ver/', views.renderAllEmails, name='see_email'),
    path('drop/', views.dropDataset, name='dropTable'),
    path('deletar/<int:email_id>/', views.deleteEmail , name='delete_email'),
    path('editar/<int:email_id>/', views.editEmail, name='edit_email')
]