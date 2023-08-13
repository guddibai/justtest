from django.db import models


class StudentModel(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    contactno = models.IntegerField()
    gender = models.CharField(max_length=10)
    username = models.CharField(max_length=30)


class LoginModel(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    type = models.CharField(max_length=30)