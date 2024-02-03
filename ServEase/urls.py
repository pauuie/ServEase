from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('bookings/', views.bookings, name='bookings'),
    path('about/', views.about, name='about'),
    path('login/', views.login_view, name='login'),
    path('bookingform/', views.bookingform, name='bookingform'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]
