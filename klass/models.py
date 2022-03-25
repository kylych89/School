from django.db import models
from teacher.models import Teacher
# Create your models here.


class Classroom(models.Model):
    class_name = models.CharField(max_length=1, verbose_name='Буква класса')
    class_number = models.IntegerField(verbose_name='Номер класса')
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)



    def __str__(self) -> str:
        return f'Класс:{self.class_number}\nБуква класса:{self.class_name}'



    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'


