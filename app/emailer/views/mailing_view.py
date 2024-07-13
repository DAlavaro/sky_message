from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from app.emailer.forms import MailingForm
from app.emailer.models import Mailing


class MailingView(ListView):
    model = Mailing


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('emailer:mailing_list')


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('emailer:mailing_list')


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('emailer:mailing_list')
    template_name = 'emailer/mailing_confirm_delete.html'