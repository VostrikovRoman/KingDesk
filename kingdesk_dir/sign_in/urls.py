from django.urls import path
from . import views

urlpatterns = [
    path('', views.sign_in, name='sign_in'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout')
]