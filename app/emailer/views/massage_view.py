from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from app.emailer.forms import MessageForm
from app.emailer.models import Message


class MessageView(ListView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('emailer:message_list')


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('emailer:message_list')


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('emailer:message_list')
    template_name = 'emailer/message_confirm_delete.html'
