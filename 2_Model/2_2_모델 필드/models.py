from django.db import models


class Zoo(models.Model):
    zoo_name = models.CharField(max_length=10)
    info = models.TextField()


class Animal(models.Model):
    name = models.CharField(max_length=20)
    info = models.TextField()
    age = models.IntegerField()
    zoo = models.ForeignKey(Zoo, on_delete=models.CASCADE)
    medical_check = models.BooleanField()
    birth_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    name = models.CharField(max_length=10)
    price = models.FloatField()


class FinancialTransaction(models.Model):
    name = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=10, decimal_places=2)


class Company(models.Model):
    name = models.CharField(max_length=20)
    info = models.TextField()
    data = models.FileField(upload_to='files/')
    photo_height = models.FloatField()
    photo_width = models.FloatField()
    photo = models.ImageField(
        upload_to='images/',
        height_field=photo_height,
        width_field=photo_width
    )
