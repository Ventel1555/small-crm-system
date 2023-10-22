# Generated by Django 4.2.5 on 2023-10-22 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='class_id',
        ),
        migrations.AddField(
            model_name='user',
            name='classes_id',
            field=models.ManyToManyField(to='edu.classes', verbose_name='Доступы к классам'),
        ),
        migrations.AddField(
            model_name='user',
            name='subjects_id',
            field=models.ManyToManyField(to='edu.subjects', verbose_name='Доступы к предметам'),
        ),
    ]