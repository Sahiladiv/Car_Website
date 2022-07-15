from django.shortcuts import *
import pyrebase
from django.contrib import auth
from django.conf.urls import url
import socket
from . import send_mail
from SellCar import views
# from . import firebase_db
# Create your views here

app_name = 'account'

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



data = {}
firebaseDb = pyrebase.initialize_app(config)
authUser = firebaseDb.auth()
userDb = firebaseDb.database()

def getIpAddress():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address


def login(request):
    
    if request.method == 'GET':
        return render(request,'login.html')
    else:

        email = request.POST.get('email')
        password = request.POST.get('pass')
        # carurl = request.POST.get('carurl')

        try:
            user = authUser.sign_in_with_email_and_password(email,password)
            temp = str(user['localId'])
            session_id = user['idToken']
            session_email = user['email']
            request.session['email'] = str(session_email)
            request.session['uid'] = str(session_id)

        except Exception as ex:
            print(type(ex))
            return render(request,'login.html')
        
        ip_address = getIpAddress()


        t = user['localId']

        ip = {
            'IP Address':ip_address
        }
        userDb.child('Users').child(t).child('IP Addresses').set(ip)

        

        return redirect('/')

def details(request,user_email):

    return HttpResponse(user_email)

def logout(request):
    print("Logout",request)
    del request.session['uid']
    return redirect('/')



def signup(request):

    if request.method=='GET':
        return render(request, 'signup.html')
    else:

        first_name = request.POST.get('f_name')
        last_name = request.POST.get('l_name')
        dob = request.POST.get('dob')
        phone = request.POST.get('phone_number')
        address = request.POST.get('address')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        confirm = request.POST.get('confirm_pass')

        if password == confirm:
            user = authUser.create_user_with_email_and_password(email, password)
            uid = user['localId']
            session_email = user['email']
            session_id = user['idToken']
            
            request.session['uid'] = str(session_id)
            request.session['email'] = str(session_email)
            full_name = first_name +" " + last_name

            print(user)
            data = {
                'Name':full_name,
                'DOB':dob,
                'Address':address,
                'Email':email,
                'Phone':phone,
            }
            print(data)
            send_mail.sendNewUserEmail(email)
            userDb.child('Users').child(uid).child('Details_Of_Users').set(data)
            
            return redirect('/')

        else:
            print('Incorrect')
            return render(request,'signup.html')
