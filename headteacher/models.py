from django.db import models

# Create your models here.
class HeadTeacher(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    image_head_teacher = models.ImageField(verbose_name='Фото', upload_to='headteacher/%y/%m/%d')

    def __str__(self) -> str:
        return self.first_name


    class Meta:
        verbose_name = 'Зауч'
        verbose_name_plural = 'Заучы'