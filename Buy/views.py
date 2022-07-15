from django.shortcuts import render



def buy_car(request):
    return render(request,'buy_car.html')


def buy_new_car(request):
    return render(request,'buy_new_car.html')

def buy_used_car(request):
    return render(request,'buy_used_car.html')

