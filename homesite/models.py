from django.db import models

class homesite(models.Model):
    summary=models.CharField(max_length=200)

class gaminglaptop(models.Model):
    forwardlink=models.URLField(max_length=200,default='')
    photolink=models.URLField(max_length=200,default='')
    laptopname=models.TextField(max_length=150,default='')
    price=models.IntegerField(null=True, blank=True, default=None)
    site=models.CharField(max_length=20,default='')
    
    def __str__(self):
        return self.laptopname


class homepagemobile(models.Model):
    forwardlink=models.URLField(max_length=200,default='')
    photolink=models.URLField(max_length=200,default='')
    mobilename=models.TextField(max_length=150,default='')
    price=models.IntegerField(null=True, blank=True, default=None)
    def __str__(self):
        return self.mobilename


class apple(models.Model):
    forwardlink=models.URLField(max_length=200,default='')
    photolink=models.URLField(max_length=200,default='')
    laptopname=models.TextField(max_length=150,default='')
    price=models.IntegerField(null=True, blank=True, default=None)
    site=models.CharField(max_length=20,default='')
    def __str__(self):
        return self.laptopname

class asus(models.Model):
    forwardlink=models.URLField(max_length=200,default='')
    photolink=models.URLField(max_length=200,default='')
    laptopname=models.TextField(max_length=150,default='')
    price=models.IntegerField(null=True, blank=True, default=None)
    site=models.CharField(max_length=20,default='')
    def __str__(self):
        return self.laptopname
  

class acer(models.Model):
    forwardlink=models.URLField(max_length=200,default='')
    photolink=models.URLField(max_length=200,default='')
    laptopname=models.TextField(max_length=150,default='')
    price=models.IntegerField(null=True, blank=True, default=None)
    site=models.CharField(max_length=20,default='')
    def __str__(self):
        return self.laptopname

class hp(models.Model):
    forwardlink=models.URLField(max_length=200,default='')
    photolink=models.URLField(max_length=200,default='')
    laptopname=models.TextField(max_length=150,default='')
    price=models.IntegerField(null=True, blank=True, default=None)
    site=models.CharField(max_length=20,default='')
    def __str__(self):
        return self.laptopname

class dell(models.Model):
    forwardlink=models.URLField(max_length=200,default='')
    photolink=models.URLField(max_length=200,default='')
    laptopname=models.TextField(max_length=150,default='')
    price=models.IntegerField(null=True, blank=True, default=None)
    site=models.CharField(max_length=20,default='')
    def __str__(self):
        return self.laptopname

class msi(models.Model):
    forwardlink=models.URLField(max_length=200,default='')
    photolink=models.URLField(max_length=200,default='')
    laptopname=models.TextField(max_length=150,default='')
    price=models.IntegerField(null=True, blank=True, default=None)
    site=models.CharField(max_length=20,default='')
    def __str__(self):
        return self.laptopname

class razerblade(models.Model):
    forwardlink=models.URLField(max_length=200,default='')
    photolink=models.URLField(max_length=200,default='')
    laptopname=models.TextField(max_length=150,default='')
    price=models.IntegerField(null=True, blank=True, default=None)
    site=models.CharField(max_length=20,default='')
    def __str__(self):
        return self.laptopname

class msi(models.Model):
    forwardlink=models.URLField(max_length=200,default='')
    photolink=models.URLField(max_length=200,default='')
    laptopname=models.TextField(max_length=150,default='')
    price=models.IntegerField(null=True, blank=True, default=None)
    site=models.CharField(max_length=20,default='')
    def __str__(self):
        return self.laptopname

class lenovo(models.Model):
    forwardlink=models.URLField(max_length=200,default='')
    photolink=models.URLField(max_length=200,default='')
    laptopname=models.TextField(max_length=150,default='')
    price=models.IntegerField(null=True, blank=True, default=None)
    site=models.CharField(max_length=20,default='')
    def __str__(self):
        return self.laptopname

class alllaptops(models.Model):
    forwardlink=models.URLField(max_length=200,default='')
    photolink=models.URLField(max_length=200,default='')
    laptopname=models.TextField(max_length=150,default='')
    price=models.IntegerField(null=True, blank=True, default=None)
    site=models.CharField(max_length=20,default='')
    def __str__(self):
        return self.laptopname


class samsungmobile(models.Model):
    forwardlink=models.URLField(max_length=200,default='')
    photolink=models.URLField(max_length=200,default='')
    mobilename=models.TextField(max_length=150,default='')
    price=models.IntegerField(null=True, blank=True, default=None)
    site=models.CharField(max_length=20,default='')
    def __str__(self):
        return self.mobilename

        
class xiaomi(models.Model):
    forwardlink=models.URLField(max_length=200,default='')
    photolink=models.URLField(max_length=200,default='')
    mobilename=models.TextField(max_length=150,default='')
    price=models.IntegerField(null=True, blank=True, default=None)
    site=models.CharField(max_length=20,default='')
    def __str__(self):
        return self.mobilename
    
class applemobile(models.Model):
    forwardlink=models.URLField(max_length=200,default='')
    photolink=models.URLField(max_length=200,default='')
    mobilename=models.TextField(max_length=150,default='')
    price=models.IntegerField(null=True, blank=True, default=None)
    site=models.CharField(max_length=20,default='')
    def __str__(self):
        return self.mobilename

class oppo(models.Model):
    forwardlink=models.URLField(max_length=200,default='')
    photolink=models.URLField(max_length=200,default='')
    mobilename=models.TextField(max_length=150,default='')
    price=models.IntegerField(null=True, blank=True, default=None)
    site=models.CharField(max_length=20,default='')
    def __str__(self):
        return self.mobilename
class vivo(models.Model):
    forwardlink=models.URLField(max_length=200,default='')
    photolink=models.URLField(max_length=200,default='')
    mobilename=models.TextField(max_length=150,default='')
    price=models.IntegerField(null=True, blank=True, default=None)
    site=models.CharField(max_length=20,default='')
    def __str__(self):
        return self.mobilename
class realme(models.Model):
    forwardlink=models.URLField(max_length=200,default='')
    photolink=models.URLField(max_length=200,default='')
    mobilename=models.TextField(max_length=150,default='')
    price=models.IntegerField(null=True, blank=True, default=None)
    site=models.CharField(max_length=20,default='')
    def __str__(self):
        return self.mobilename
class oneplus(models.Model):
    forwardlink=models.URLField(max_length=200,default='')
    photolink=models.URLField(max_length=200,default='')
    mobilename=models.TextField(max_length=150,default='')
    price=models.IntegerField(null=True, blank=True, default=None)
    site=models.CharField(max_length=20,default='')
    def __str__(self):
        return self.mobilename

class poco(models.Model):
    forwardlink=models.URLField(max_length=200,default='')
    photolink=models.URLField(max_length=200,default='')
    mobilename=models.TextField(max_length=150,default='')
    price=models.IntegerField(null=True, blank=True, default=None)
    site=models.CharField(max_length=20,default='')
    def __str__(self):
        return self.mobilename

class nokia(models.Model):
    forwardlink=models.URLField(max_length=200,default='')
    photolink=models.URLField(max_length=200,default='')
    mobilename=models.TextField(max_length=150,default='')
    price=models.IntegerField(null=True, blank=True, default=None)
    site=models.CharField(max_length=20,default='')
    def __str__(self):
        return self.mobilename


class allmobiles(models.Model):
    forwardlink=models.URLField(max_length=200,default='')
    photolink=models.URLField(max_length=200,default='')
    mobilename=models.TextField(max_length=150,default='')
    price=models.IntegerField(null=True, blank=True, default=None)
    site=models.CharField(max_length=20,default='')
    def __str__(self):
        return self.mobilename

class bestmidranger(models.Model):
    forwardlink=models.URLField(max_length=200,default='')
    photolink=models.URLField(max_length=200,default='')
    mobilename=models.TextField(max_length=150,default='')
    price=models.IntegerField(null=True, blank=True, default=None)
    site=models.CharField(max_length=20,default='')
    def __str__(self):
        return self.mobilename

class latestflagship(models.Model):
    forwardlink=models.URLField(max_length=200,default='')
    photolink=models.URLField(max_length=200,default='')
    mobilename=models.TextField(max_length=150,default='')
    price=models.IntegerField(null=True, blank=True, default=None)
    site=models.CharField(max_length=20,default='')
    def __str__(self):
        return self.mobilename