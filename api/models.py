from django.db import models

# Create your models here.
class Product(models.Model):
    title  = models.CharField(max_length=255,null = True,blank = True)
    description = models.TextField(null = True,blank = True)
    price = models.FloatField(null = True,blank = True)
    
    def __str__(self):
        return self.title
