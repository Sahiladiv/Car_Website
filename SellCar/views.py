from django.shortcuts import *
from django.http import HttpResponse
from django.contrib import auth
from firebase_admin import *
from .models import *


from django.contrib.auth.decorators import login_required


import pyrebase
# Create your views here.
import pyrebase
from django.contrib import auth

config = {
    'apiKey': "AIzaSyBRb3sJmZp6-zDfXCkdPkaZR0geOLq_5NQ",
    'authDomain': "car-websi.firebaseapp.com",
    'databaseURL': "https://car-websi-default-rtdb.firebaseio.com",
    'projectId': "car-websi",
    'storageBucket': "car-websi.appspot.com",
    'messagingSenderId': "260072109013",
    'appId': "1:260072109013:web:9a1f00833be9058be6835c",
    'measurementId': "G-DF9DGY7YR3"
}

firebaseDb = pyrebase.initialize_app(config)
authUser = firebaseDb.auth()
userDb = firebaseDb.database()


cred = credentials.Certificate("serviceAccountKey.json")
# firebase_admin.initialize_app(cred)
db = firestore.client()


docs = db.collection('Cars').get()

#Show landing page
def index(request):
    listOfCars = []
    dictionaryOfCars = {}
    numberOfCars = len(docs)
    for i in range(0,6):
        carId = docs[i].id
        carDetails = db.collection('Cars').document(docs[i].id).get().to_dict()
        dictionaryOfCars['ID'] = carId
        carDetails['ID'] = carId
        listOfCars.append(carDetails)

    return render(request,'index.html',{'t':listOfCars})


def getUsedCars(request):
    usedDocs = db.collection('Used cars for sale').get()
    listOfCars = []
    dictionaryOfCars = {}
    numberOfCars = len(usedDocs)
    for i in range(numberOfCars):
        carId = usedDocs[i].id
        # print(carId)
        carDetails = db.collection('Used cars for sale').document(carId).get().to_dict()
        dictionaryOfCars['ID'] = carId
        carDetails['ID'] = carId
        listOfCars.append(carDetails)


   

    return render(request,'usedcars.html',{'t':listOfCars})


#Show more cars
def morecars(request):
    listOfCars = []
    dictionaryOfCars = {}
    numberOfCars = len(docs)
    for i in range(numberOfCars):
        carId = docs[i].id
        carDetails = db.collection('Cars').document(docs[i].id).get().to_dict()
        dictionaryOfCars['ID'] = carId
        carDetails['ID'] = carId
        listOfCars.append(carDetails)


    

    return render(request,'morecars.html',{'t':listOfCars})



def firstLoginAndThenSellCar(request):
    return HttpResponseRedirect('account/login')

def sellCar(request):
    return render(request,'sellcar.html')



def buyUsedCar(request,car_id):
    listOfCar = []
    carDetails = db.collection('Used cars for sale').document(car_id).get().to_dict()
    carDetails['ID'] = car_id
    listOfCar.append(carDetails) 
    return render(request,'buyusedcar.html',{'t':listOfCar})





#Show details of the car to be bought
def buyCar(request,car_id):
    
    listOfCar = []
    carDetails = db.collection('Cars').document(car_id).get().to_dict()
    carDetails['ID'] = car_id
    listOfCar.append(carDetails) 
    print(listOfCar)
    return render(request,'details_of_new_car.html',{'t':listOfCar})


# Sell car add data to database
def sellMyCar(request):

    if request.method == 'POST':

        docs = db.collection('Used cars for sale')
        car_model     = request.POST.get('car_model')
        car_brand     = request.POST.get('car_brand')
        car_type      = request.POST.get('car_type')
        car_condition = request.POST.get('car_condition')
        car_location  = request.POST.get('car_location')
        car_price1    = request.POST.get('car_price1')
        car_price2    = request.POST.get('car_price2')
        photo     =     request.POST.get('url')
        print("Image url:",photo)
        car_price = '₹'+car_price1 + '-' + car_price2 +" Lakhs"
        
        sell_car_dict = {
            'car_model':car_model,
            'car_brand':car_brand,
            'car_type':car_type,
            'car_condition':car_condition,
            'car_location':car_location,
            'car_price':car_price,
            'image_url':photo,
        }
        docs.add(sell_car_dict)
        return redirect("/")





def buyNewCar(request,car_id,user_id):
    request.session['carid'] = car_id
    return render(request,'payment.html')
    # return redirect('account/login')


def buyNewCarAfterLogin(request,user_id,car_id):
        return render(request,'payment.html')




def sellCarFirstLogin(request):
    return redirect('account/login')



def getMessage(request):
    if request.method == 'GET':
        # return redirect('/')
        pass
    else:
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        Message = request.POST.get('message')

        Data = {
            'Name' : Name,
            'Email' : Email,
            'phone_number' : phone_number,
            'Message' : Message
        }
        userDb.child('Message').child(Data['Email']).set(Data)
    
    return redirect('/')
    
        


def firstLogin(request,car_id):

    return HttpResponseRedirect('/account/login')
