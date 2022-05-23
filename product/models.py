from distutils.command.upload import upload
from django.db import models

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=200)
    desciption = models.TextField()
    def __str__(self):
        return self.name
class product(models.Model):
    name = models.CharField(max_length=200)
    desciption = models.TextField()
    image = models.ImageField(upload_to='photo/%y/%m/%d')
    price = models.DecimalField(max_digits=7,decimal_places=2)
    category_id = models.ForeignKey(category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class order(models.Model):
    productid = models.IntegerField()
    user_id = models.IntegerField()
    num =models.IntegerField()


