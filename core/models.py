from django.db import models

class VendorData(models.Model):
    name = models.CharField(max_length=60)
    email=models.EmailField()
    shop_name=models.CharField(max_length=100)
    info=models.TextField()
    def __str__(self):
        return self.name

class Feedback(models.Model):
    name=models.CharField(max_length=50)
    email = models.EmailField()
    info= models.TextField()
    def __str__(self):
        return self.name
class VendorData_bennett(models.Model):
    name = models.CharField(max_length=60)
    email=models.EmailField()
    shop_name=models.CharField(max_length=100)
    info=models.TextField()
    def __str__(self):
        return self.name
class VendorData_Galgotia(models.Model):
    name = models.CharField(max_length=60)
    email=models.EmailField()
    shop_name=models.CharField(max_length=100)
    info=models.TextField()
    def __str__(self):
        return self.name
class VendorData_sharda(models.Model):
    name = models.CharField(max_length=60)
    email=models.EmailField()
    shop_name=models.CharField(max_length=100)
    info=models.TextField()
    def __str__(self):
        return self.name
class VendorData_Dtu(models.Model):
    name = models.CharField(max_length=60)
    email=models.EmailField()
    shop_name=models.CharField(max_length=100)
    info=models.TextField()
    def __str__(self):
        return self.name
    