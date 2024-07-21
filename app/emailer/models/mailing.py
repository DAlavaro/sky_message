from django.db import models
from django.apps import apps


class Mailing(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название рассылки')
    start_time = models.DateTimeField(verbose_name='Время начала отправки рассылки')

    PERIOD_CHOICES = [
        ('daily', 'Раз в день'),
        ('weekly', 'Раз в неделю'),
        ('monthly', 'Раз в месяц'),
    ]
    period = models.CharField(max_length=20, verbose_name='Периодичность', choices=PERIOD_CHOICES)

    STATUS_CHOICES = [
        ('created', 'Создана'),
        ('started', 'Запущена'),
        ('completed', 'Завершена'),
    ]
    status = models.CharField(max_length=20, verbose_name='Статус', choices=STATUS_CHOICES, default='created')

    message = models.ForeignKey('emailer.Message', on_delete=models.CASCADE, verbose_name='Сообщение')
    clients = models.ManyToManyField('emailer.Client', verbose_name='Клиенты')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
