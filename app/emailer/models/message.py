from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=255, verbose_name='Тема', unique=True)
    message = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
