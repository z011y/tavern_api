from django.db import models

# Create your models here.
class Musician(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=45)
    username = models.CharField(max_length=45, unique=True)
    password = models.CharField(max_length=45, unique=True)
    email = models.CharField(max_length=45)
    user_type = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Venue(models.Model):
    venue_id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=80)
    img = models.CharField(max_length=80, null=True)
    slug = models.CharField(max_length=45, null=True)

    def __str__(self):
        return self.name
