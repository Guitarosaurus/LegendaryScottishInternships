from django.urls import path
from legendary import views

app_name = 'legendary'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about,name='about'),
    path('about/report/', views.report,name='report'),
    path('profile/',views.profile,name='profile'),
    path('profile/change-checklist',views.change_checklist,name='change_checklist'),
    path('profile/update-profile',views.update_profile,name='update_profile'),
    path('login/',views.user_login,name='login'),
    path('register/',views.register,name='register'),
    path('listings/',views.listings,name='listings'),


    
]
