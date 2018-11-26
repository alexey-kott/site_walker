from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE

from django.utils import timezone

from datetime import datetime


class Proxy(models.Model):
    owner = models.ForeignKey(User, on_delete=CASCADE)
    proxy_id = models.IntegerField(primary_key=True, auto_created=True)
    host = models.TextField()
    port = models.IntegerField()
    username = models.TextField()
    password = models.TextField()
    enabled = models.BooleanField()

    class Meta:
        unique_together = ('owner', 'host', 'port', 'username')


class City(models.Model):
    name = models.CharField(max_length=30, unique=True, default='')

    def __str__(self):
        return self.name


class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=CASCADE)
    name = models.TextField(default='')
    status = models.BooleanField(default=True)

    search_query = models.TextField(null=True)
    target_url = models.TextField(null=True)
    competitor_sites = models.TextField(null=True)
    region = models.ForeignKey(City, on_delete=CASCADE, default=None, null=True)
    last_start = models.DateTimeField(default=timezone.now, null=True)
    delay = models.IntegerField(null=True)


class Log(models.Model):
    owner = models.ForeignKey(User, on_delete=CASCADE)
    action = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now)
