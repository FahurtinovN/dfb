from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    surname = models.CharField(max_length=20)
    gender =models.BooleanField(verbose_name='Гендер')
    birthDay = models.DateField(verbose_name='Дата рождения')

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        verbose_name = 'люди'
        verbose_name_plural = 'ЧЕЛОВЕК'