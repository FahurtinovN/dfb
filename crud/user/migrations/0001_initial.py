# Generated by Django 5.0 on 2023-12-13 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.PositiveIntegerField()),
                ('surname', models.CharField(max_length=20)),
                ('gender', models.BooleanField()),
                ('birthDay', models.DateTimeField()),
            ],
        ),
    ]
