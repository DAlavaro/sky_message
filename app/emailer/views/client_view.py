from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from app.emailer.forms import ClientForm
from app.emailer.models import Message, Client


class ClientView(ListView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('emailer:client_list')


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('emailer:client_list')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('emailer:client_list')
    template_name = 'emailer/client_confirm_delete.html'