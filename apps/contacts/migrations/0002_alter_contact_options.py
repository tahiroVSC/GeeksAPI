# Generated by Django 5.0 on 2024-02-22 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': ('Контакт',), 'verbose_name_plural': 'Контакты'},
        ),
    ]