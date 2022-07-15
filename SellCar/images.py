import pyrebase

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

firebase = pyrebase.initialize_app(config)

db = firebase.database()

imagesOfCar = db.child('Car Images').get()

print(imagesOfCar.val())
