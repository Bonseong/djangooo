from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), ## url 분리
]
