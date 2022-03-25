from django.db import models

# Create your models here.
class Teacher(models.Model):
    teacher_name = models.CharField(max_length=50, verbose_name='Имя')
    teacher_last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    image = models.ImageField(verbose_name='Фото', upload_to='product/%Y/%m/%d')
    phone = models.CharField(max_length=25)
    address = models.CharField(max_length=250, verbose_name='Место проживания:')
    
    
    def __str__(self) -> str:
        return self.teacher_name


    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'