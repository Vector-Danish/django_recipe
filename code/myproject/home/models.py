from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    email = models.EmailField(null = True, blank = True)
    address = models.TextField()
    image = models.FileField()  


class product(models.Model):
    pass