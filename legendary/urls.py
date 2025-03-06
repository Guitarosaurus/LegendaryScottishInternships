from django.urls import path
from legendary import views

app_name = 'legendary'

urlpatterns = [
    path('', views.index, name='index'),
]