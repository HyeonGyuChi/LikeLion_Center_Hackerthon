import os, uuid
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.dispatch import receiver

class Resume(models.Model):
    resume_name = models.CharField(default="이력서 템플릿", max_length=50)
    file = models.FileField(upload_to="resume_templates", null=True)
    download_num = models.IntegerField(default=0)
    coin = models.IntegerField(default=0)
    like_user_set = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name='like_user_set',
        through='Like')
    download_user_set = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name='download_user_set',
        through='Download')

    def __str__(self):
        return ("{}").format(self.resume_name)

    def like_count(self):
        return self.like_user_set.count()

    def download_count(self):
        return self.download_user_set.count()

class ResumeInfo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    info_name = models.CharField(max_length=50)
    writer_name = models.CharField(max_length=20)
    writer_address = models.TextField()
    writer_phone = models.CharField(max_length=13)
    writer_email = models.CharField(default='', blank=True, max_length=30)

    writer_career_whenstart = models.CharField(default='', blank=True, max_length=9)
    writer_career_whenstop = models.CharField(default='', blank=True, max_length=9)
    writer_career_name = models.CharField(default='', blank=True, max_length= 10)
    writer_career_detail = models.TextField(default='', blank=True)
    writer_career_title = models.CharField(default='', blank=True, max_length=10)

    writer_school_whenstart = models.CharField(default='', blank=True,max_length=9)
    writer_school_whenstop = models.CharField(default='', blank=True,max_length=9)
    writer_school_name = models.CharField(default='', blank=True,max_length= 12)
    writer_school_study = models.TextField(default='', blank=True)

    writer_prizeandetc_whenstart = models.CharField(default='', blank=True,max_length=9)
    writer_prizeandetc_whenstop = models.CharField(default='', blank=True,max_length=9)
    writer_prizeandetc_name = models.CharField(default='', blank=True,max_length= 10)
    writer_prizeandetc_detail = models.TextField(default='', blank=True)

    writer_ability_name = models.CharField(default='', blank=True,max_length= 25)





    def __str__(self):
        return ("{} - {}").format(self.writer_name, str(self.date))

    # def get_absolute_url(self):
    #     print("get_absolute_url 사용됨")
    #     return reverse('views.resume_detail', args=[str(self.id)])

class ResumeMerged(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    resume = models.ForeignKey('Resume', on_delete=models.CASCADE)
    resume_info = models.ForeignKey('ResumeInfo', on_delete=models.CASCADE)
    docx_file = models.FileField(null=True)
    pdf_file = models.FileField(null=True)
    img_file = models.ImageField(null=True)

    def __str__(self):
        return ("{} - {}").format(self.user.username, self.resume.resume_name)

    @property
    def download_num(self):
        return self.resume.download_count()

    @property
    def like_num(self):
        return self.resume.like_count()

class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    resume = models.ForeignKey('Resume', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (
            ('user', 'resume')
        )

class Download(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    resume = models.ForeignKey('Resume', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (
            ('user', 'resume')
        )

@receiver(models.signals.post_delete, sender=Resume)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """Deletes file from filesystem
    when corresponding `Resume` object is deleted.
    """
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)