from datetime import datetime

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


class VIPpersons(models.Model):
    FIO = models.CharField(max_length=30)
    Home = models.CharField(max_length=30)
    Date = models.DateTimeField(default=datetime.now)
    Education = models.CharField(default="Высшее", max_length=30)
    Language = models.CharField(default="English", max_length=30)
    Trips = models.BooleanField(default=True)
    Post = models.CharField(max_length=30)
    Salary = models.IntegerField(default=70000)

class Book_Love(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, blank=True, db_index=True, default='')
    content = models.TextField(blank=True)
    auther = models.CharField(max_length=70)
    bithday = models.DateField()
    is_interesting = models.BooleanField(default=True)
    year_public = models.DateTimeField()
    genre = models.CharField(max_length=30)
    size = models.IntegerField()

#python manage.py makemigrations
#python manage.py sqmigrate women 000_
#python manage.py migrate
#python manage.py shell_plus




