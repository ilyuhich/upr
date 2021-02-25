from django.db import models

# Create your models here.
from django.urls import reverse


class District(models.Model):
    # районы города
    district_name = models.CharField(max_length=20, verbose_name='Район')

    def __str__(self):
        return self.district_name

    def get_absolute_url(self):
        return reverse('district-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'


class Place(models.Model):
    # объекты размещения оборудования
    uid = models.CharField(max_length=12, null=True, default=' ', blank=True, verbose_name='Идентификатор')  # Числовой идентификатор площадки
    ident = models.CharField(max_length=10, null=True, default=' ', blank=True, verbose_name='Код площадки')  # AIS2531
    addr = models.CharField(max_length=200, null=True, verbose_name='Адрес')
    district = models

    def __str__(self):
        return self.addr

    def get_absolute_url(self):
        return reverse('problem-create')

    class Meta:
        verbose_name = 'Размещение'
        verbose_name_plural = 'Размещения'


class Rig(models.Model):
    addr = models.ForeignKey(Place, on_delete=models.PROTECT, verbose_name='Размещение')
    ident = models.CharField(null=True, max_length=100, verbose_name='Идентификатор')
    model = models.CharField(max_length=100, verbose_name='Модель')

    def __str__(self):
        return self.addr.ident + ' ' + self.model

    class Meta:
        verbose_name = 'Устройство'
        verbose_name_plural = 'Устройства'


class Companies(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Customer(models.Model):
    name = models.CharField(max_length=100, verbose_name='Заказчик')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'


class Problem(models.Model):
    num = models.CharField(max_length=10, verbose_name='Проблема', unique=True)
    obj = models.ForeignKey(Place, on_delete=models.PROTECT, null=True)
    time_created = models.DateTimeField(null=True, verbose_name='Время создания')
    time_closed = models.DateTimeField(blank=True, null=True, verbose_name='Время закрытия')
    description = models.TextField(blank=True, verbose_name='Описание проблемы')
    responsible = models.ForeignKey(Companies, default=0, blank=True, on_delete=models.PROTECT,
                                    verbose_name='Текущий исполнитель')

    def __str__(self):
        return self.num + ' ' + self.obj.ident + ' ' + self.responsible.name

    def get_absolute_url(self):
        return reverse('problem-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Проблема'
        verbose_name_plural = 'Проблемы'


class ProblemTemp(models.Model):
    num = models.CharField(max_length=10, verbose_name='Временная')


class Comment(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.PROTECT, verbose_name='К проблеме')
    datetime = models.DateTimeField(blank=True, verbose_name='Время добавления')
    text = models.TextField(max_length=255, verbose_name='Содержание')

    def __str__(self):
        return str(self.problem.num) + ' ' + str(self.datetime)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Installation(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.PROTECT, null=True, verbose_name='Проблема')
    added = models.DateTimeField(verbose_name='Добавлено', null=True)
    description = models.CharField(max_length=100, verbose_name='Описание')

    def __str__(self):
        return self.problem.num + ' ' + ' ' + self.description

    class Meta:
        verbose_name_plural = 'Установки'
        verbose_name = 'Установка'
