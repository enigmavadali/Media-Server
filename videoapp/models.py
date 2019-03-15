from django.db import models
from random import randint
from django.contrib.auth.models import User
from django import forms
from django_mysql.models import ListCharField

# Create your models here.
class Document(models.Model):
    #id = models.IntegerField(default = randint(10**3, (10**4)), unique=True,primary_key=True)
    id = models.AutoField(primary_key=True)
    title = models.TextField(blank=False)
    description = models.TextField(blank=False)
    docfile = models.FileField(upload_to='videos/admin/')
    #like = models.ManyToManyField(User, related_name='likes' )
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default = 0)
    thumbnail = models.ImageField(default = 0)
    mpdfile=models.FileField(default=0)
    tag = models.TextField(null=False,default="")
    is_time_started = models.BooleanField(default=True)
    duration = models.CharField(default='',max_length=10)
    #upload_date = models.DateTimeField(auto_now_add=True)

class History(models.Model):
    user = models.TextField(default="")
    vid_id = models.IntegerField(default=0)
    tag = models.TextField(default="")

class Lecture(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(blank=False)
    docfile = models.FileField(upload_to='videos/professor/')
    antim_tarikh  = models.DateField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    start_hour = models.IntegerField()
    start_min = models.IntegerField()
    end_hour = models.IntegerField()
    end_min = models.IntegerField()
    views = models.IntegerField(default = 0)
    thumbnail = models.ImageField(default=0)
    tag = models.TextField(null=False,default="")
    mpdfile=models.FileField(default=0)
    is_time_started = models.BooleanField(default=False)
    reg_students = ListCharField(default="",base_field = models.CharField(max_length=50),size=800,max_length=(51*800))
    duration = models.CharField(default='',max_length=10)

class Like(models.Model):
    username = models.TextField(null=True)
    vid_id = models.IntegerField(default=0)
    liked = models.BooleanField(default=False)

class Comment(models.Model):
    user_id = models.TextField(default="")
    v_id = models.IntegerField(default=0)
    body = models.TextField(default="")
    obj_type = models.CharField(default="" , max_length=10)
