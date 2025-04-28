from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('message/', views.messageboard, name='messageboard'),
    path('message/create', views.createmessageboard, name='createmessageboard'),
]
