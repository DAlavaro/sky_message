from django.contrib import admin

from app.emailer.models import Message, Client, Mailing


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'message')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'comment')


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time', 'end_time', 'period', 'status')
