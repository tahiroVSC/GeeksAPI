from django.db import models


class Contact(models.Model):
    phone_number = models.CharField(
        max_length=16, verbose_name="Номер телефона")
    p_number = models.CharField(max_length=16, verbose_name="Второй номер")
    email = models.EmailField(
        verbose_name="Введите почту", blank=True, null=True)
    work_time = models.CharField(
        verbose_name="Время работы по будням", max_length=100)
    w_time = models.CharField(
        verbose_name="Время работы по выходным", max_length=100)
    address = models.CharField(max_length=150, verbose_name="Адрес")
    links = models.URLField(
        verbose_name="Введите ссылку", blank=True, null=True)

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = 'Контакт',
        verbose_name_plural = 'Контакты'
