from django.db import models


# Create your models here.

class Contributors(models.Model):
    id = models.AutoField(primary_key=True)
    owner_name = models.CharField(max_length=128, unique=False)
    repo_name = models.CharField(max_length=128, unique=False)
    con_name = models.CharField(max_length=128, unique=False)
    con_num = models.IntegerField()


class Commits(models.Model):
    id = models.AutoField(primary_key=True)
    owner_name = models.CharField(max_length=128)
    repo_name = models.CharField(max_length=128)
    con_name = models.CharField(max_length=128)


class date01(models.Model):
    id = models.AutoField(primary_key=True)
    repo_name = models.CharField(max_length=128)
    date_newest = models.DateTimeField()  # 项目最新更新时间
    date_local = models.DateTimeField(auto_now=True)  # 上回本地更新时间
    date_lasttime = models.DateTimeField()  # 上回爬到的数据的最新时间


class stargazer_company(models.Model):
    id = models.AutoField(primary_key=True)
    node_id = models.CharField(max_length=32)
    company = models.CharField(max_length=128)
    get_time = models.DateTimeField()


class stargazer_company_statistic(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.CharField(max_length=128)
    count = models.IntegerField()
    total = models.IntegerField()
    update_time = models.DateTimeField()
    duplicate=models.IntegerField()
    flag=models.IntegerField()


class issue_company(models.Model):
    id = models.AutoField(primary_key=True)
    node_id = models.CharField(max_length=32)
    company = models.CharField(max_length=128)
    get_time = models.DateTimeField()


class issue_company_statistic(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.CharField(max_length=128)
    count = models.IntegerField()
    total = models.IntegerField()
    update_time = models.DateTimeField()
    duplicate = models.IntegerField()
    flag = models.IntegerField()


class committer_company(models.Model):
    id = models.AutoField(primary_key=True)
    node_id = models.CharField(max_length=32)
    company = models.CharField(max_length=128)
    get_time = models.DateTimeField()


class committer_company_statistic(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.CharField(max_length=128)
    count = models.IntegerField()
    total = models.IntegerField()  # 这里的total是指有公司记录的人数
    update_time = models.DateTimeField()
    duplicate = models.IntegerField()
    flag = models.IntegerField()

class pandas_stargazer_company(models.Model):
    id = models.AutoField(primary_key=True)
    node_id = models.CharField(max_length=32)
    company = models.CharField(max_length=128)
    get_time = models.DateTimeField()



class pandas_issue_company(models.Model):
    id = models.AutoField(primary_key=True)
    node_id = models.CharField(max_length=32)
    company = models.CharField(max_length=128)
    get_time = models.DateTimeField()



class pandas_committer_company(models.Model):
    id = models.AutoField(primary_key=True)
    node_id = models.CharField(max_length=32)
    company = models.CharField(max_length=128)
    get_time = models.DateTimeField()


class total(models.Model):
    id = models.AutoField(primary_key=True)
    source = models.CharField(max_length=128)  # 数据来源(stargazer/issue/committer)
    total = models.IntegerField()  # 这里的total是指获取时所有的人数,用于更新时比对缺少的条数，仅获取这些并更新


class pandas_total(models.Model):
    id = models.AutoField(primary_key=True)
    source = models.CharField(max_length=128)  # 数据来源(stargazer/issue/committer)
    total = models.IntegerField()  # 这里的total是指获取时所有的人数,用于更新时比对缺少的条数，仅获取这些并更新
