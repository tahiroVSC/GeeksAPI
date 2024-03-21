from django.db import models



class Application(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Имя'
    )
    surname = models.CharField(
        max_length=255,
        verbose_name='Фамилия'
    )
    number = models.CharField(
        verbose_name='номер',
        max_length=255
    )

    def __str__(self):
        return f"{self.name} - {self.surname}"

    class Meta:
        verbose_name = 'Заявление'
        verbose_name_plural = 'Заявления'
