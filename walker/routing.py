# mysite/routing.py
from channels.routing import ProtocolTypeRouter
from django.conf.urls import url

from walker import consumers

application = ProtocolTypeRouter({
    url(r'^ws/$', consumers.WalkerConsumer)
    # (http->django views is added by default)
})