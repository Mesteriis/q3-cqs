from django.db import models


class TgUser(models.Model):
    tg_chat = models.PositiveIntegerField(verbose_name='ID чата Telegram')
    tg_user = models.CharField(verbose_name='ID пользователя Telegram', max_length=32)
