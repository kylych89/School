from django.db import models
 

# Create your models here.
class Students(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='Имя студента')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия студента')
    number_parents = models.IntegerField(verbose_name='Номер родителей')
    place_of_residence = models.CharField(max_length=255, verbose_name='Место проживания')
    photo_student = models.ImageField(verbose_name='Фото студента', upload_to = 'product/%Y/%m/%d')
    class_ = models.ForeignKey('class.Classroom', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Имя студента {self.first_name} \n Класс {self}'


    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'