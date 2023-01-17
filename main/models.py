from django.db import models

class Cars(models.Model):
    name = models.CharField(max_length=200)