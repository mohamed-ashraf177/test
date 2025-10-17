from django.urls import path
from .views import users_list, create_user



urlpatterns = [
    path('users/', users_list, name='users_list'),
    path('users/create/', create_user, name='create_user'),
]