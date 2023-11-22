from django.db import models

class Women(models.Model):
    titile = models.CharField(max_length=255)
    conten = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

class Pupil(models.Model):
        surname = models.CharField(max_length=30)
        mame = models.CharField(max_length=30)
        patronymic = models.CharField(max_length=30,blank=True)
        age = models.IntegerField(default=10)
        class_p = models.IntegerField(default=15)


class Workers(models.Model):
    FIO = models.CharField(max_length=30)
    Home = models.CharField(max_length=30)
    Date = models.DateTimeField(blank=True)
    Education = models.CharField(default="Высшее")
    Language = models.IntegerField(max_length=30, blank=True)
    Trips = models.BooleanField(defauit=true)
    Post = models.CharField(max_length=30)
    Salary = models.IntegerField(default=19000000000000000000000000000000000000000000000000)




