from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

STATUS_CHOICES = [
    ('Создан', 'Создан'),
    ('Запущен', 'Запущен'),
    ('Остановлен', 'Остановлен')
]


class User(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'


# Create your models here.
class Object(models.Model):
    priority = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name='Приоритет')
    status = models.TextField(max_length=20, default='created', choices=STATUS_CHOICES, verbose_name='Статус')
    time_created = models.TimeField(verbose_name='Время создания')
    users = models.ManyToManyField(User, related_name='objects', verbose_name='Исполнитель', blank=True, null=True)

    def __str__(self):
        return f'Объект | {self.time_created} | {self.status} | {self.priority}'

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'
