from django.db import models
from .managers import customusermanager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin
class User(AbstractUser):
    username = models.CharField(max_length=50,null=True)
    email = models.EmailField()
    phone=models.CharField(max_length=15,unique=True,null=True)
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username']
    # objects = customusermanager()
    def __str__(self):
        return self.email
class Product(models.Model):
    product_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    price=models.IntegerField()
    def __str__(self):
        return self.name
    @staticmethod
    def updateprice(product_id, price):
        p = Product.objects.filter(product_id=product_id)
        product = p.first()
        product.price = price
        product.save()
        return product
    """chahe static bnalo ya class same se hi method h"""
    '''@classmethod
    def updateprice(cls,product_id,price):
        p=cls.objects.filter(product_id=product_id)
        product=p.first()
        product.price=price
        product.save()
        return product

    @classmethod
    def create(cls, name, price):
        product = cls(name=name,price=price)  #cls ya class name se call krlo same  hi h
        product.save()
        return product'''
class cartmanager(models.Manager):
    def create_cart(self,user):
        cart=self.create(user=user)
        return cart

class Cart(models.Model):
    cart_id=models.AutoField(primary_key=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    created_on=models.DateTimeField()
    objects=cartmanager()

class Cart_product(models.Model):
    class Meta:
        unique_together=(('cart','product'),)
    cart_product_id=models.AutoField(primary_key=True)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
class Orders(models.Model):
    status_choice=((1,'not placed'),(2,'ready for shipment'),(3,'shipped'),(4,'delivered'))
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.IntegerField(choices=status_choice,default=1)

class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    email_token=models.CharField(max_length=200)
    is_verified=models.BooleanField(default=False)


class student(models.Model):
    username = models.CharField(max_length=50, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15, unique=True, null=True)
    password=models.CharField(max_length=20)



