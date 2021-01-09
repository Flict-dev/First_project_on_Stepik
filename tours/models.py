from django.db import models
from django.urls import reverse


class Depature(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название пути')
    slug = models.SlugField(max_length=20, verbose_name='Слаг', null=True, blank=True)

    class Meta:
        verbose_name = 'Путь'
        verbose_name_plural = 'Пути'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('depature', kwargs={"slug": self.slug})


class Tour(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(max_length=3000, verbose_name='Описание тура')
    depature = models.ForeignKey(Depature, on_delete=models.CASCADE, verbose_name='Название пути', blank=True,
                                 null=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Изображение')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    stars = models.PositiveIntegerField(blank=True, null=True, default=0, verbose_name='Кол-во звёзд')
    country = models.CharField(max_length=30, verbose_name='Страна тура', blank=True, null=True)
    date = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Дата начла тура', blank=True, null=True)
    duration = models.PositiveSmallIntegerField(default=0, verbose_name='Продолжительность тура')

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tour_detail', args=[str(self.id)])
