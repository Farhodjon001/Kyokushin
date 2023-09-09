from django.db import models

# Create your models here.
class News(models.Model):
    title=models.CharField(max_length=250)
    desc=models.TextField()
    created_time=models.DateField(auto_now_add=True)
    updated_time=models.DateField(auto_now=True)

