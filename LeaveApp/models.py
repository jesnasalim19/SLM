from django.db import models

# Create your models here.
class reg_tbl(models.Model):
    fn = models.CharField(max_length=25)
    mb = models.IntegerField()
    gn = models.CharField(max_length=10)
    st = models.CharField(max_length=25)
    em = models.EmailField()
    ps = models.CharField(max_length=25)
    cps = models.CharField(max_length=25)
    
class leave_req(models.Model):
    sn = models.CharField(max_length=25)
    st = models.CharField(max_length=25)
    lt = models.CharField(max_length=25)
    lop = models.IntegerField()
    md = models.FileField(upload_to='medical')
    start = models.DateField()
    end = models.DateField()
    rs = models.TextField()
    rd = models.IntegerField()
    al = models.IntegerField()
    rm = models.IntegerField()
    approved = models.BooleanField(default=False)

class leave_reg_lwa(models.Model):
    sn = models.CharField(max_length=25)
    st = models.CharField(max_length=25)
    lt = models.CharField(max_length=25)
    lop = models.IntegerField()
    md = models.FileField(upload_to='medical')
    start = models.DateField()
    end = models.DateField()
    rs = models.TextField()
    rd = models.IntegerField()
    approved = models.BooleanField(default=False)
  


     