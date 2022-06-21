from django.db import models

class Foot_size(models.Model):
    size = models.DecimalField(max_digits=2, decimal_places=1) 

class Clothes_number_size(models.Model):
    size = models.DecimalField(max_digits=2, decimal_places=1) 
    
class Clothes_Letter_size(models.Model):
    size = models.CharField(max_length=3) 
    
class Foot(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    size = models.ForeignKey(Foot_size, on_delete=models.DO_NOTHING) 
    qtd = models.DecimalField(max_digits=3, decimal_places=1)

class Pants(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    size = models.ForeignKey(Clothes_number_size, on_delete=models.DO_NOTHING) 
    qtd = models.DecimalField(max_digits=3, decimal_places=1)

class Shirt(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    size = models.ForeignKey(Clothes_Letter_size, on_delete=models.DO_NOTHING)
    qtd = models.DecimalField(max_digits=3, decimal_places=1)

class Hoobies(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    size = models.ForeignKey(Clothes_Letter_size, on_delete=models.DO_NOTHING) 
    qtd = models.DecimalField(max_digits=3, decimal_places=1)
