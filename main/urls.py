from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),

    path('list/', views.carList),
    path('create/', views.createCar),
    path('delete/<slug:pk>', views.deleteCar),
    # path('register/', views.RegisterUser.as_view()),
]
