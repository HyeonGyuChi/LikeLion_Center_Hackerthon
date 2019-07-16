from django.db import models
from django import forms
from django.urls import reverse

class Resume(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    writer_name = models.CharField(max_length=20)
    writer_address = models.TextField()
    writer_phone = models.CharField(max_length=13)
    writer_email = models.CharField(max_length=30)
    
    def __str__(self):
        return ("{} - {}").format(self.writer_name, str(self.date))

    def get_absolute_url(self):
        return reverse('views.resume_detail', args=[str(self.id)])