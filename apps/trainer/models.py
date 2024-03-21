from django.db import models


class Trainer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='trainer/')
    description = models.TextField()

    class Meta:
        verbose_name = 'Тренер',
        verbose_name_plural = 'Тренеры'
