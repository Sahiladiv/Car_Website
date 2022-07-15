from django.shortcuts import render

def sell_my_car(request):
    return render(request,'sellcar.html')

