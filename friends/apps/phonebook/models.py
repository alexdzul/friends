import os
from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    phone_number = models.CharField(max_length=200)
    about = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.first_name
