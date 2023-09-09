from django.db import models

class TrainersModels(models.Model):
    name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    image = models.ImageField(upload_to='/images')
    phone = models.CharField(max_length=12)