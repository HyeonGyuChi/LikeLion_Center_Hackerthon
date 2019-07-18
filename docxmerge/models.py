import os, uuid
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.dispatch import receiver

class ResumeInfo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    writer_name = models.CharField(max_length=20)
    writer_address = models.TextField()
    writer_phone = models.CharField(max_length=13)
    writer_email = models.CharField(max_length=30)
    
    def __str__(self):
        return ("{} - {}").format(self.writer_name, str(self.date))

    def get_absolute_url(self):
        print("get_absolute_url 사용됨")
        return reverse('views.resume_detail', args=[str(self.id)])

class Resume(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    resume_name = models.CharField(default=uuid.uuid4, max_length=50)
    file = models.FileField(upload_to="resume_templates", null=True)

    def __str__(self):
        return ("{}").format(self.resume_name)

@receiver(models.signals.post_delete, sender=Resume)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """Deletes file from filesystem
    when corresponding `Resume` object is deleted.
    """
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)