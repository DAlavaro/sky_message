from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from app.emailer.forms import MailingForm
from app.emailer.models import Mailing
from config import settings
from django.core.mail import send_mail

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


class MailingSendView(View):
    def get(self, request, pk):
        mailing = Mailing.objects.get(pk=pk)
        clients = mailing.clients.all()
        message = mailing.message.message
        subject = mailing.message.name

        for client in clients:
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[client.email],
            )

        messages.success(request, f'Рассылка "{mailing.name}" была успешно отправлена.')
        return redirect('emailer:mailing_list')
