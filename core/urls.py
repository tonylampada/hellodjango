from core import views
from django.urls import path

urlpatterns = [
    path('api/login', views.login),
    path('api/logout', views.logout),
    path('api/whoami', views.whoami),
]