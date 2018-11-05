from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE


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


class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=CASCADE)
    name = models.TextField(default='Task')
    status = models.BooleanField(default=True)

    search_query = models.TextField(null=True)
    target_url = models.TextField(null=True)
    competitor_sites = models.TextField(null=True)

