from django.db import models
from ckeditor.fields import RichTextField



class Abonement(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    gruppa = models.CharField(max_length=250, verbose_name='Группа')
    description = RichTextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='abonement/',
                              null=True, verbose_name='Фото')
    weekdays = models.CharField(max_length=150, verbose_name='Время секции')
    price_month = models.CharField(
        max_length=20, verbose_name='Стоимость в месяц')
    price_year = models.CharField(
        max_length=20, verbose_name='Стоимость в год')

    class Meta:
        verbose_name = 'Абонемент',
        verbose_name_plural = 'Абонементы'
