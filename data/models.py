from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name
