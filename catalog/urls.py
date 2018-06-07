from django.urls import path
from . import views


urlpatterns = [
    path('', views.dFogIT, name='dFogIT'),
    path('dfogit/', views.dFogIT, name='dFogIT'),
]
