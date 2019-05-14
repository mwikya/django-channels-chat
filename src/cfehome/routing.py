from channels.auth import AuthMiddlewareStack
from django.conf.urls import url
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator,OriginValidator
import chat.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
	        URLRouter(
	            chat.routing.websocket_urlpatterns
	        )
        )
    ),
})