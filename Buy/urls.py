from django.contrib import admin
from django.urls import path
import account.views
from . import views

urlpatterns = [
    path('',views.buy_car,name="All Cars"),
    path('New',views.buy_new_car,name="Buy New Car"),
    path('Used',views.buy_used_car,name="Buy Used Car"),

]