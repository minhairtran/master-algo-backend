from django.db import models

# Create your models here.

class Algorithm(models.Model):
    title = models.TextField()
    subtitle = models.TextField()
    image = models.FileField(upload_to='images/')