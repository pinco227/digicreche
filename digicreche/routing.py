from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from chat.routing import websocket_urlpatterns as chat_ws_route

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(chat_ws_route),
    ),
})
