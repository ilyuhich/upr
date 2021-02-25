from django.db import models


# Create your models here.
class District(models.Model):
    # районы города
    district_name = models.CharField(max_length=20, verbose_name='Район')

    def __str__(self):
        return self.district_name

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'


class Place(models.Model):
    # объекты размещения оборудования
    uid = models.CharField(max_length=12, null=True, verbose_name='Идентификатор')  # Числовой идентификатор площадки
    ident = models.CharField(max_length=10, null=True, verbose_name='Код площадки')  # AIS2531
    addr = models.CharField(max_length=200, null=True, verbose_name='Адрес')
    district = models

    def __str__(self):
        return self.ident + ' ' + self.addr

    class Meta:
        verbose_name = 'Размещение'
        verbose_name = 'Размещение'


class Companies(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Problem(models.Model):
    num = models.CharField(max_length=10, verbose_name='Проблема')
    obj = models.ForeignKey(Place, on_delete=models.PROTECT, null=True)
    time_created = models.DateTimeField(verbose_name='Время создания')
    time_closed = models.DateTimeField(verbose_name='Время закрытия')
    description = models.TextField(blank=True, verbose_name='Описание проблемы')
    responsible = models.ForeignKey(Companies, on_delete=models.PROTECT, verbose_name='Текущий исполнитель')


class ProblemTemp(models.Model):
    num = models.CharField(max_length=10, verbose_name='Временная')
