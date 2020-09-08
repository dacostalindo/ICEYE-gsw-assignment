from django.db import models

# Create your models here.
class SaveItem(models.Model):

    content = models.TextField()

    congratulations = models.TextField()
