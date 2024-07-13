from django import forms
from .models import Message, Client, Mailing


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'message']


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'comment']


class MailingForm(forms.ModelForm):
    clients = forms.ModelMultipleChoiceField(
        queryset=Client.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label='Клиенты'
    )

    start_time = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        label='Время начала отправки рассылки'
    )
    end_time = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        label='Время окончания отправки рассылки'
    )

    class Meta:
        model = Mailing
        fields = ['name', 'start_time', 'end_time', 'period', 'status', 'message', 'clients']