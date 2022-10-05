from django.db import models
# Create your models here.

class Contributors(models.Model):
    id = models.AutoField(primary_key=True)
    owner_name = models.CharField(max_length=128,unique=False)
    repo_name = models.CharField(max_length=128,unique=False)
    con_name = models.CharField(max_length=128,unique=False)
    con_num = models.IntegerField()

class Commits(models.Model):
    id = models.AutoField(primary_key=True)
    owner_name = models.CharField(max_length=128)
    repo_name = models.CharField(max_length=128)
    con_name = models.CharField(max_length=128)

class date01(models.Model):
    id = models.AutoField(primary_key=True)
    repo_name = models.CharField(max_length=128)
    date_newest = models.DateTimeField()#项目最新更新时间
    date_local = models.DateTimeField(auto_now=True)#上回本地更新时间
    date_lasttime = models.DateTimeField()#上回爬到的数据的最新时间


