from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('guestbook_messages.urls')),
    path('', views.dashboard, name='dashboard'),
]
