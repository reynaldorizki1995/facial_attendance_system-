from django.db import models
from datetime import date
from django.forms import ModelForm
# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    date_created = models.DateField(auto_now_add=True, null=True)
    



class Anggota(models.Model):
    # id = models.AutoField(primary_key=True)
    nrp = models.IntegerField(primary_key=True)
    nama_depan = models.CharField(max_length=32)
    nama_belakang = models.CharField(max_length=32)
    hp = models.CharField(max_length=32)
    foto = models.ImageField(upload_to='static/profile/', name="Image")
    alamat = models.CharField(max_length=128)
    tmpt_lahir = models.CharField(max_length=32)
    tgl_lahir = models.DateField("Date", default=date.today)
    pendidikan = models.CharField(max_length=128)
    

# class Image(models.Model):
#     id = models.IntegerField(name='ID', unique=True, primary_key=True, editable=False)
#     image = models.ImageField(name='Image')
#     user = models.ForeignKey('User', on_delete=models.CASCADE)