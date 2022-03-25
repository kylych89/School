# Generated by Django 4.0.3 on 2022-03-25 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=1, verbose_name='Буква класса')),
                ('class_number', models.IntegerField(verbose_name='Номер класса')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher')),
            ],
        ),
    ]
