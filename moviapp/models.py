from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Navbar(models.Model):
    poster=models.ImageField(upload_to='movi/navbar',default="movi/navbar/not.jpg")




class Cinema(models.Model):
    cinema = models.AutoField(primary_key=True)
    role = models.CharField(max_length=30, default='manager')
    movi_name = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='movi/navbar', default="movi/navbar/not.jpg")
    screen = models.CharField(max_length=10, default="null")
    phoneno = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    adress = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.movi_name


class Movie(models.Model):
    movie=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    trailer=models.CharField(max_length=200,default="null")
    date=models.CharField(max_length=20,default="null")
    movi_desc=models.TextField()
    rating=models.DecimalField(max_digits=3,decimal_places=1)
    poster=models.ImageField(upload_to='movi/poster',default="movi/poster/not.jpg")
    genre=models.CharField(max_length=50,default="Action | Romance | comdey")
    duration=models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Show(models.Model):
    shows=models.AutoField(primary_key=True)
    cinema=models.ForeignKey('Cinema',on_delete=models.CASCADE,related_name="cinema_shows")
    movi=models.ForeignKey('Movie',on_delete=models.CASCADE,related_name="movi_shows")
    time=models.CharField(max_length=50)
    date=models.CharField(max_length=100)
    price=models.IntegerField()

    def __str__(self):
        return self.cinema.movi_name +" | "+ self.movi.name +" | "+self.time

class Booking(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    shows=models.ForeignKey(Show,on_delete=models.CASCADE)
    seat=models.CharField(max_length=100)

    @property
    def seat_as__list(self):
        return self.seat.split('')
    def __str__(self):
        return self.user.username +" | "+ self.shows.cinema.movi_name +" | "+ self.seat


