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
        class_p = models.IntegerField(max_length=30)


