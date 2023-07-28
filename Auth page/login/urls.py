from django.urls import path 
from . import views

urlpatterns = [
    path('',views.base),
    path('home',views.home,name='home'),
    path('login',views.Login,name='login'),
    path('logout',views.logout_view,name='logout'),
    path('signup',views.signup,name='signup'),
]
