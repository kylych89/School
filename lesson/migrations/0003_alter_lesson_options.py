# Generated by Django 4.0.3 on 2022-03-26 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0002_remove_lesson_classroom_lesson_teacher'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'verbose_name': 'Урок', 'verbose_name_plural': 'Уроки'},
        ),
    ]
