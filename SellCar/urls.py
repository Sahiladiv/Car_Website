from django.contrib import admin
from django.urls import path
import account.views
from . import views

urlpatterns = [
    path('', views.index,name="Home Page"),
    # path('sendmessage',views.message,name="Send Message"),
    path('sellcar',views.firstLoginAndThenSellCar,name="Sell Car"),
    path('sell/car',views.sellCar,name="Sell Car"),
    path('sell/sellmycar',views.sellMyCar,name="Sell Car"),
    path('morecars',views.morecars,name="More Cars"),
    
    path('buy/<car_id>/',views.buyCar,name="Buy Car"),
    path('buy/<car_id>/login',views.firstLogin,name="Login"),
    path('buy/<car_id>/<user_id>',views.buyNewCar,name="Buy Cars"),
    
   
    path('buy/used/<car_id>/login',views.firstLogin,name="Buy A  Car"),
    path('buy/used/car/<car_id>',views.buyUsedCar,name="Buy A Used Car"),
    path('buy/used/car/<car_id>/<user_id>',views.buyNewCar,name="Bought A Used Car"),
    
    path('usedcars',views.getUsedCars,name="Used Cars"),

    path('SellCar/sendmessage',views.getMessage,name="User Message"),
    path('SellCar/account/logout',account.views.logout,name="Logout"),
    path('SellCar/account/login',account.views.login,name="Login"),
    path('SellCar/account/signup',account.views.signup,name="Signup"),




    


]