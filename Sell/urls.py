from django.contrib import admin
from django.urls import path
import account.views
from . import views

urlpatterns = [
    path('',views.sell_my_car,name="All Cars"),

]