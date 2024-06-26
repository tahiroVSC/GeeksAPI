# Generated by Django 5.0.3 on 2024-03-14 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Review', '0004_review_dol_ky_review_dol_ru_review_photo_ky_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='dol',
            new_name='jobtitle',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='dol_ky',
            new_name='jobtitle_ky',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='dol_ru',
            new_name='jobtitle_ru',
        ),
        migrations.AlterField(
            model_name='review',
            name='discription',
            field=models.TextField(verbose_name='Отзыв'),
        ),
        migrations.AlterField(
            model_name='review',
            name='discription_ky',
            field=models.TextField(null=True, verbose_name='Отзыв'),
        ),
        migrations.AlterField(
            model_name='review',
            name='discription_ru',
            field=models.TextField(null=True, verbose_name='Отзыв'),
        ),
    ]
