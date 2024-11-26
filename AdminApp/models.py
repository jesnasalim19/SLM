from django.db import models

# Create your models here.
class admin_log(models.Model):
    usr = models.CharField(max_length=25)
    psw = models.CharField(max_length=25)
class Leaveinfo(models.Model):
    sn = models.CharField(max_length=25)
    st = models.CharField(max_length=25)
    cs = models.IntegerField()
    sl = models.IntegerField()
    cl = models.IntegerField()
    ml = models.IntegerField()
    pl = models.IntegerField()
    vc = models.IntegerField()

class payroll_tbl(models.Model):
    sn = models.CharField(max_length=25)
    lt = models.CharField(max_length=25)
    st = models.CharField(max_length=25)
    start = models.CharField(max_length=25)
    end = models.CharField(max_length=25)
    al = models.IntegerField()
    nl = models.IntegerField()
    rm = models.IntegerField()
    basic = models.IntegerField()
    lop = models.IntegerField()
    net = models.FloatField()

class lwa_payroll_tbl(models.Model):
    sn = models.CharField(max_length=25)
    lt = models.CharField(max_length=25)
    st = models.CharField(max_length=25)
    start = models.CharField(max_length=25)
    end = models.CharField(max_length=25)
    basic = models.IntegerField()
    lop = models.IntegerField()
    net = models.FloatField()

class assign_tbl(models.Model):
    sn = models.CharField(max_length=25)
    start = models.CharField(max_length=25)
    end = models.CharField(max_length=25)
    nl = models.IntegerField()
    fn = models.CharField(max_length=25)