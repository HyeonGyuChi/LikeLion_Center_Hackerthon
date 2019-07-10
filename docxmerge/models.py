from django.db import models
from django import forms

class Resume(models.Model):
    date = models.DateTimeField()
    writer_name = models.CharField(max_length=20)
    writer_address = models.TextField()
    writer_phone = models.CharField(max_length=11)
    writer_email = models.CharField(max_length=30)