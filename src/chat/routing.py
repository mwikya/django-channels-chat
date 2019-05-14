from django.conf.urls import url

from .consumers import ChatConsumer

websocket_urlpatterns = [
    url(r"^messages/(?P<username>[\w.@+-]+)/$", ChatConsumer),
]