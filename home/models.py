from django.db import models

# Create your models here.
class stuinfo(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    intro=models.CharField(max_length=100)
    sex=models.CharField(max_length=4)
    grade=models.CharField(max_length=10)
    phone=models.IntegerField()
    address=models.CharField(max_length=100)
class scuinfo_pic(models.Model):
    hre_f=models.CharField(max_length=200)
    titl_e=models.CharField(max_length=200)
    pic_url=models.CharField(max_length=100)
    cday=models.CharField(max_length=10)
class scuinfo_content(models.Model):
    href_1=models.CharField(max_length=500)
    tit_1=models.CharField(max_length=100)
    date_1=models.CharField(max_length=30)
    cday = models.CharField(max_length=10)
class main_pic(models.Model):
    hre_f = models.CharField(max_length=200)
    titl_e = models.CharField(max_length=200)
    pic_url = models.CharField(max_length=100)
    cday = models.CharField(max_length=10)