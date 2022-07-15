# import firestore_model
# import firestore
# import firebase_admin

# from firebase_admin import credentials
# from firebase_admin import firestore
# # Create your models here.
# cred = credentials.Certificate("serviceAccountKey.json")
# firebase_admin.initialize_app(cred)
# db = firestore.client()
# class Cars(Model):

#     Name = 
#     Brand = 

from firebase_orm import models


class Cars(models.Model):

    name = models.CharField(max_length=200)
    

    