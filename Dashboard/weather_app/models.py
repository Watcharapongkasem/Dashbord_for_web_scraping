from django.db import models

class Category(models.Model):
    type_air = models.CharField(max_length=50)
 
    def __str__(self) :
        return self.type_air

class resoure(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self) :
        return self.name   

class location(models.Model):
    code= models.IntegerField(unique=True)
    name=models.CharField(max_length=50, unique=True)
    air2_5=models.FloatField(default=0)
    description=models.TextField(null=True)
    updated=models.DateTimeField(auto_now=True)
    resoure=models.ManyToManyField(resoure,blank=True)
    category=models.ManyToManyField(Category,blank=True)
    
    def __str__(self):
        return self.name
