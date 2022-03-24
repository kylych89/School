from django.db import models

# Create your models here.
class Lesson(models.Model):
    # teacher = models.CharField(Teacher, related_name='teacher', null=True,
    #                             on_delete=models.SET_NULL, verbose_name='Учитель/ница')
    lesson_name = models.CharField(max_length=50, verbose_name='Название урока')
    classroom = models.IntegerField(verbose_name='Кабинет')

    def __str__(self) -> str:
        return f'Урок {self.lesson_name}'
