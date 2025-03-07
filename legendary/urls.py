from django.urls import path
from legendary import views

app_name = 'legendary'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about,name='about'),
    path('about/report/', views.report,name='report'),
    path('profile/',views.profile,name='profile'),
    path('profile/login/',views.login,name='login'),
    path('profile/login/register/',views.register,name='register'),
    path('listings/',views.listings,name='listings'),
    
]