# Generated by Django 4.0.3 on 2022-03-25 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('image', models.ImageField(upload_to='product/%Y/%m/%d', verbose_name='Изображение')),
                ('phone', models.CharField(max_length=25)),
            ],
        ),
    ]
