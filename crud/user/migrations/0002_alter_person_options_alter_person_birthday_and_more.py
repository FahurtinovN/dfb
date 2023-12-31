# Generated by Django 5.0 on 2023-12-13 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'люди', 'verbose_name_plural': 'ЧЕЛОВЕК'},
        ),
        migrations.AlterField(
            model_name='person',
            name='birthDay',
            field=models.DateField(verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.BooleanField(verbose_name='Гендер'),
        ),
    ]
