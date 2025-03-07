from django.urls import path
from legendary import views

app_name = 'legendary'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about,name='about'),
    path('profile/',views.profile,name='profile'),
]