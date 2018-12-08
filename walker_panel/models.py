from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE

from django.utils import timezone

from datetime import datetime, timedelta


class Proxy(models.Model):
    owner = models.ForeignKey(User, on_delete=CASCADE)
    host = models.TextField()
    port = models.IntegerField()
    username = models.TextField(null=True)
    password = models.TextField(null=True)
    enabled = models.BooleanField()
    status = models.BooleanField(default=True)

    class Meta:
        unique_together = ('owner', 'host', 'port')


class City(models.Model):
    name = models.CharField(max_length=30, unique=True, default='')

    def __str__(self):
        return self.name


class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=CASCADE)
    name = models.TextField(default='')
    status = models.BooleanField(default=True)
    is_running = models.BooleanField(default=False)

    search_query = models.TextField(null=True)
    target_url = models.TextField(null=True)
    competitor_sites = models.TextField(null=True)
    city = models.TextField(default=None, null=True)
    last_start = models.DateTimeField(default=timezone.now, null=True)
    delay = models.IntegerField(default=0)
    launches_per_day = models.IntegerField(default=0)

    @property
    def launches_today(self):
        return Log.objects \
            .filter(action='TASK_ACTIVATED') \
            .filter(task=self).filter(datetime__gt=timezone.now().date()) \
            .filter(datetime__lte=timezone.now().date() + timedelta(days=1)).count()


class Log(models.Model):
    owner = models.ForeignKey(User, on_delete=CASCADE)
    action = models.TextField(null=True)
    task = models.ForeignKey(Task, on_delete=CASCADE, null=True)
    datetime = models.DateTimeField(default=timezone.now)
    level = models.TextField(default='INFO')
    extra = models.TextField(null=True, default='')
    uid = models.TextField()
