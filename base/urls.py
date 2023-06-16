from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('', views.home, name='home'),
    path('rent/', views.rent, name='rent'),
    path('return-book/', views.return_book, name='return-book'),
    path('add-book/', views.add_book, name='add-book'),

]