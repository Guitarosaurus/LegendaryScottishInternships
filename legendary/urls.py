from django.urls import path
from legendary import views
from django.conf.urls import url

app_name = 'legendary'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about,name='about'),
    path('about/<str:internship_name>/<str:email_content>/report/', views.report,name='report'),
    path('profile/',views.profile,name='profile'),
    path('change-checklist/',views.change_checklist,name='change-checklist'),
    path('update-profile/',views.update_profile,name='update-profile'),
    path('login/',views.user_login,name='login'),
    path('register/',views.register,name='register'),
    path('listings/',views.listings,name='listings'),
    path('logout/', views.user_logout, name='logout'),
    
]
