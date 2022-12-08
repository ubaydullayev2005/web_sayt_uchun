from django.db import models

# Create your models here.

class Type(models.Model):
    nomi = models.CharField(max_length=30)
    def __str__(self):
        return self.nomi

class Portfolio(models.Model):
    nomi = models.CharField(max_length=50)
    tur = models.ForeignKey(Type,on_delete=models.CASCADE)
    rasm = models.ImageField(upload_to='media')
    vatq = models.DateTimeField(auto_now=True)

class Team(models.Model):
    ism = models.CharField(max_length=50)
    martaba = models.CharField(max_length=50)
    rasm = models.ImageField(upload_to='media')
    twiter = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    instagram = models.CharField(max_length=200)
    linced = models.CharField(max_length=100)

class Message(models.Model):
    name = models.CharField(max_length=40)
    mail = models.EmailField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    time = models.DateTimeField(auto_now=True)




