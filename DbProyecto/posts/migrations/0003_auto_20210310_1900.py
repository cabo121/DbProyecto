# Generated by Django 3.1.7 on 2021-03-11 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20210309_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
        migrations.AddField(
            model_name='post',
            name='descripcion',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='post',
            name='fecha',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='post',
            name='personaje',
            field=models.TextField(default=''),
        ),
    ]
