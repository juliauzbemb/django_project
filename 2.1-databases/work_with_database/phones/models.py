from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Название', null=False)
    price = models.IntegerField(default=None, verbose_name='Стоимость')
    image = models.URLField(default=None, verbose_name='Изображение')
    release_date = models.DateField(default=None, verbose_name='Дата выхода')
    lte_exists = models.BooleanField(default=None, verbose_name='Наличие lte')
    slug = models.SlugField(max_length=255, default=None, verbose_name='slug')

    def __str__(self):
        return f'{self.id}. {self.name}'



