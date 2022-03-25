# Generated by Django 4.0.3 on 2022-03-25 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('teacher_last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('image', models.ImageField(upload_to='product/%Y/%m/%d', verbose_name='Фото')),
                ('phone', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=250, verbose_name='Место проживания:')),
            ],
        ),
    ]