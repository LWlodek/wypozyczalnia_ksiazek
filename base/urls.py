from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('', views.home, name='home'),
    path('borrow/', views.borrow, name='borrow'),
    path('return-book/', views.return_book, name='return-book'),
    path('add-book/', views.add_book, name='add-book'),
    path('book-list/', views.book_list, name='book-list'),

]