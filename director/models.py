from django.db import models

# Create your models here.
class Director(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    image = models.ImageField(verbose_name='Изображение', upload_to='product/%Y/%m/%d')
    phone = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.first_name


    class Meta:
        verbose_name = 'Директор'
        verbose_name_plural = 'Директоры'
