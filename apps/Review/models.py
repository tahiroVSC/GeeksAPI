from django.db import models


class Review(models.Model):
    photo = models.ImageField(
        verbose_name= "Фотография",
        upload_to= "images/"
    )
    name = models.CharField(
        max_length=255,
        verbose_name="ФИО"
    )
    jobtitle = models.CharField(
        max_length = 255,
        verbose_name = "Должность"
    )
    discription = models.TextField(
        verbose_name="Отзыв"
    )
    created = models.DateField(
        auto_now=True,
        verbose_name="Дата публикации"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
