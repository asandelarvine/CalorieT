from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name='home'),
    path('accounts/profile/', views.profile,name='home'),
    path('profile/',views.profile,name='profile'), 
    path('foods/',views.fooditem,name='fooditem'),
    path('createfooditem/',views.createfooditem,name='createfooditem'),
    path('addFooditem/',views.addFooditem,name='addFooditem'),
    path('update_profile/<int:id>',views.update_profile, name='update_profile'),
    path('about/',views.about,name='about'),
]