from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('login',views.login,name="Login"),
    path('signup',views.signup,name="Sign Up"),
    path('logout',views.logout,name="Logout"),
    path('details/<user_email>',views.details,name="User Details")
]
