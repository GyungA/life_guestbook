from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('message/', views.messageboard, name='message_board'),
    path('message/create', views.createmessageboard, name='create_message_board'),
]
