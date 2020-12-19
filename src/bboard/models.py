from django.db import models

class Bboard(models.Model):
    title = models.CharField(max_length=55, verbose_name='Название')
    content = models.TextField(null=True, blank=True, verbose_name='Содержание')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата создания') #db_index=True --- укажет создать полю Индекс
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    rubric = models.ForeignKey('Rubric', on_delete=models.PROTECT, null=True, verbose_name='Рубрика')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Обьявление'
        verbose_name_plural = 'Обьявления'
        ordering = ['-published']

class Rubric(models.Model):
    name = models.CharField(max_length=33, db_index=True, verbose_name='Название')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'
        ordering = ['name']