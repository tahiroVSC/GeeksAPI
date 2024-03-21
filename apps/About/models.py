from django.db import models


class AboutUs(models.Model):
    text = models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name = 'О нас',
        verbose_name_plural = 'О нас'
