# Generated by Django 4.0.3 on 2022-03-26 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('headteacher', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='headteacher',
            options={'verbose_name': 'Зауч', 'verbose_name_plural': 'Заучы'},
        ),
        migrations.AlterField(
            model_name='headteacher',
            name='image_head_teacher',
            field=models.ImageField(upload_to='headteacher/%y/%m/%d', verbose_name='Фото'),
        ),
    ]
