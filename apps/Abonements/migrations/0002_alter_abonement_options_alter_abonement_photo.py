# Generated by Django 5.0 on 2024-02-22 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Abonements', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='abonement',
            options={'verbose_name': ('Абонемент',), 'verbose_name_plural': 'Абонементы'},
        ),
        migrations.AlterField(
            model_name='abonement',
            name='photo',
            field=models.ImageField(null=True, upload_to='abonement/', verbose_name='Фото'),
        ),
    ]
