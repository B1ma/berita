from django.db import models

# Create your models here.
class Gamesartikels(models.Model):
    title = models.CharField(max_length=225)
    thumb = models.CharField(max_length=225)
    date = models.CharField(max_length=225)
    desc = models.TextField()
    key = models.CharField(max_length=225)
    

