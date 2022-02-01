from django.db import models

# Create your models here.

class Student(models.Model):
    std_name = models.CharField(max_length=20)
    std_roll_num = models.CharField(max_length=20)

    def __str__(self):
        return self.std_name


