from django.urls import path

from core import views


urlpatterns = [
    path('', views.Main.as_view(), name='main'),
    path('offline/', views.offline, name='offline'),
    path('serviceworker.js', views.service_worker, name='serviceworker'),
    path('manifest.json', views.manifest, name='manifest'),
    path('favicon.ico', views.favicon_ico, name='favicon'),
]