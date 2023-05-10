from django.db import models

class Employee(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    phone=models.CharField(max_length=10)
