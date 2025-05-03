from django.urls import path
from . import views
from User import views as user_views
from django.contrib.auth import views as auth_view
urlpatterns=[
    path('',views.home,name="homepage"),
    path('about/',views.about,name="about"),
    path('register/',user_views.register,name="register"),
    path('login/',user_views.loginview,name="login"),
    path('logout/',user_views.logoutt,name="logout"),

]