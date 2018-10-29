from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE


class ProxyModel(models.Model):
    owner = models.ForeignKey(User, on_delete=CASCADE)
    proxy_id = models.IntegerField(primary_key=True)
    host = models.TextField()
    port = models.IntegerField()
    username = models.TextField()
    password = models.TextField()
    enabled = models.BooleanField()

    class Meta:
        unique_together = ('owner', 'host', 'port', 'username')
