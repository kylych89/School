from django.db import models
from director.models import Director
from headteacher.models import HeadTeacher
from lesson.models import Lesson
from students.models import Students
from teacher.models import Teacher
from klass.models import Classroom
# Create your models here.

class Shkola(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название школы')
    director = models.OneToOneField(Director, on_delete=models.SET_NULL, null=True)
    head_teacher = models.OneToOneField(HeadTeacher, on_delete=models.SET_NULL, null=True)
    lessons = models.ManyToManyField(Lesson, null=True)
    students = models.ManyToManyField(Students, null=True)
    teachers = models.ManyToManyField(Teacher, null=True)
    klass = models.ManyToManyField(Classroom, null=True)


    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name = 'Школа'
        verbose_name_plural = 'Школы'


