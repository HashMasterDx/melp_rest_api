from django.db import models
from uuid import uuid4


class Restaurant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    rating = models.IntegerField()
    name = models.CharField(max_length=255)
    site = models.URLField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return self.name
