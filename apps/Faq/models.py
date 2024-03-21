from django.db import models


class Faq(models.Model):
    question = models.CharField(
        max_length=255,
        verbose_name="Вопрос"
    )
    answer = models.TextField(
        verbose_name="Ответ на вопрос"
    )

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "Часто задаваемые вопросы"
        verbose_name_plural = "Часто задаваемые вопросы"
