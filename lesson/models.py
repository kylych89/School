from django.db import models
from teacher.models import Teacher

# Create your models here.
class Lesson(models.Model):
    teacher = models.ForeignKey(Teacher, related_name='teacher_lesson', null=True,
                                on_delete=models.SET_NULL, verbose_name='Учитель/ница')
    lesson_name = models.CharField(max_length=50, verbose_name='Название урока')
    

    def __str__(self) -> str:
        return f'Урок {self.lesson_name}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
