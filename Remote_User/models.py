from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    gender= models.CharField(max_length=30)
    address= models.CharField(max_length=30)


class detect_data_breach(models.Model):

    Fid= models.CharField(max_length=300)
    Organisation= models.CharField(max_length=300)
    RecordsLost= models.CharField(max_length=300)
    DateTime= models.CharField(max_length=300)
    Breached_Information= models.CharField(max_length=300)
    Individuals_Affected= models.CharField(max_length=300)
    BreachDate= models.CharField(max_length=300)
    FromIPAddress= models.CharField(max_length=300)
    ToIPAddress= models.CharField(max_length=300)
    Prediction= models.CharField(max_length=300)

class detection_accuracy(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

class detection_ratio(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)



