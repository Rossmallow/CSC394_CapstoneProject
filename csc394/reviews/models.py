from django.db import models

# Create your models here.


class Review(models.Model):
    name = models.TextField(max_length=200)
    performance = models.TextField(max_length=100)
    improvement = models.TextField(max_length=1000)
    additionalInfo = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
