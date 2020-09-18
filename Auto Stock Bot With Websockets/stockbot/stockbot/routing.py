from channels.routing import ProtocolTypeRouter
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from sierrabot import consumers

websocket_urlpatterns = [
    path("ws/stockdata/", consumers.StockData),
]

application = ProtocolTypeRouter(
    {"websocket": AuthMiddlewareStack(URLRouter(websocket_urlpatterns)),}
)

