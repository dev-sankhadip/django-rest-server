from django.db import models
from django.contrib.postgres.fields import ArrayField



# Create your models here.

class Products(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50, default="")
    subcategory=models.CharField(max_length=50, default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    image=models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name



class UserModel(models.Model):
    userid=models.AutoField
    username=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)


class TestModel(models.Model):
    test=ArrayField(models.CharField(max_length=200), blank=True)