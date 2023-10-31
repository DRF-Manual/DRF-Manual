from django.db import models

class Zoo(models.Model):
    zoo_name = models.CharField()

    def __str__(self):
        return f'{self.zoo_name}'

class Animal(models.Model):
    name = models.CharField()
    info = models.TextField()
    zoo = models.ForeignKey(Zoo, on_delete=models.CASCADE)
    medical_check = models.BooleanField()
    birth_at = models.DateTimeField()

    def __str__(self):
        return f'{self.name}'