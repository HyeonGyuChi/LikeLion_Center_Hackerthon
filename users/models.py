from django.db import models
from authtools.models import AbstractEmailUser

class User(AbstractEmailUser):
    username = models.CharField('full name', max_length=255, blank=True)
    usercoin = models.IntegerField(default=0)

    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        return self.username