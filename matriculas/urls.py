#url de matriculas

from django.urls import path

from . import views

app_name = 'matriculas'
urlpatterns = [
path('', views.inicio, name='inicio'),
]