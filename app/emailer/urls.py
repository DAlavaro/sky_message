from django.urls import path

from app.emailer.views.client_view import ClientView, ClientCreateView, ClientUpdateView, ClientDeleteView
from app.emailer.views.mailing_view import MailingView, MailingCreateView, MailingUpdateView, MailingDeleteView
from app.emailer.views.massage_view import MessageView, MessageCreateView, MessageUpdateView, MessageDeleteView

app_name = 'emailer'

urlpatterns = [
    path('message/', MessageView.as_view(), name='message_list'),
    path('message/create/', MessageCreateView.as_view(), name='message_create'),
    path('message/<int:pk>/update/', MessageUpdateView.as_view(), name='message_update'),
    path('message/<int:pk>/delete/', MessageDeleteView.as_view(), name='message_delete'),

    path('client/', ClientView.as_view(), name='client_list'),
    path('client/create/', ClientCreateView.as_view(), name='client_create'),
    path('client/<int:pk>/update/', ClientUpdateView.as_view(), name='client_update'),
    path('client/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),

    path('mailing/', MailingView.as_view(), name='mailing_list'),
    path('mailing/create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing/<int:pk>/update/', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing/<int:pk>/delete/', MailingDeleteView.as_view(), name='mailing_delete'),
]
