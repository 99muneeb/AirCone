from django.db import models


# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    ser_image = models.ImageField('photos/%Y/%m/%d/')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Team(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    team_image = models.ImageField('photos/%Y/%m/%d/')
    facebook = models.URLField(max_length=255)
    twitter = models.URLField(max_length=255)
    Intstagram = models.URLField(max_length=255)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Contect(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Appointment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address = models.TextField()
    date = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    message=models.TextField()
    datatime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
