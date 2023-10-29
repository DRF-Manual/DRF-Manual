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
