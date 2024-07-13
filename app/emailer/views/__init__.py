__all__ = [
    'MessageView',
    'MessageCreateView',
    'MessageUpdateView',
    'MessageDeleteView',

    'ClientView',
    'ClientCreateView',
    'ClientUpdateView',
    'ClientDeleteView',
]

from app.emailer.views.client_view import ClientView, ClientCreateView, ClientUpdateView, ClientDeleteView
from app.emailer.views.massage_view import MessageView, MessageCreateView, MessageUpdateView, MessageDeleteView
