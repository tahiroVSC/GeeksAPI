# Generated by Django 5.0.3 on 2024-03-21 05:53

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Abonements', '0002_alter_abonement_options_alter_abonement_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abonement',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Описание'),
        ),
    ]
