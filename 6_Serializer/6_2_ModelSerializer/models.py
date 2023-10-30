from django.db import models

class Zoo(models.Model):
    name = models.CharField(max_length=10)


class Animal(models.Model):
    name = models.CharField(max_length=10)
    info = models.TextField()
    zoo = models.ForeignKey(Zoo, on_delete=models.CASCADE)