from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import related

from django.utils import timezone

from django.shortcuts import reverse

import datetime
import uuid

# Create your models here.

class Language(models.Model):
    languages = models.CharField(max_length=32)

    def __str__(self):
        return(self.languages)

class Status(models.Model):
    stages = models.CharField(max_length=27)
        
    def __str__(self):
        return(self.stages)

class Branch(models.Model):
    branches = models.CharField(max_length=32)

    def __str__(self):
        return(self.branches)

class Project(models.Model):

    class ProjectObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().all()#filter(status='published')

    title = models.CharField(max_length=200)
    abstract = models.TextField(max_length=9000, default=" ", help_text='Proje özeti...')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    published = models.DateField(default=datetime.datetime.now)
    #published = models.DateField(default=timezone.now)

    language = models.ForeignKey(Language, null=True, on_delete=models.PROTECT, related_name='language')
    status = models.ForeignKey(Status, null=True, on_delete=models.PROTECT, related_name='current_stage')
    branches = models.ManyToManyField(Branch)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='keci_project')

    document = models.FileField(upload_to='documents/deneme/', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('help')

    objects = models.Manager() #default manager
    projectobjects = ProjectObjects() #custom manager

    class Meta:
        ordering = ('-published',)

        def __str__(self):
            return(self.title)
