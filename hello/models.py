from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=60)
    condition = models.TextField()
