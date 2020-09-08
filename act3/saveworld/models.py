from django.db import models

# Create your models here.
class SaveItem(models.Model):
    content = models.TextField()


class Savior(models.Model):
    salute = models.TextField()
