from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^peserta/', views.peserta)
]