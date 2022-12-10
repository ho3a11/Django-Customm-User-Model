from . import views
from django.urls import path

urlpatterns = [
    path('',views.index, name='index'),
    path('create_user/', views.create_user, name='create_user'),
    path('change_password/', views.change_password, name='change_password'),
    path('register_user/', views.register_user, name='register_user'),
]
