from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inicio/', views.index, name='inicio'),
    path('registro/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout')
]