from django.urls import path

from core import views


urlpatterns = [
    path('', views.Main.as_view(), name='main')
]