from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.TextField()
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name


