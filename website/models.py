from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Resume(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextUploadingField()
    file = models.FileField(upload_to='resumes/', blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    file = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ContactInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    t_me = models.CharField(max_length=100)

    def __str__(self):
        return self.name
