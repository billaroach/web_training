from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.forms import Select


class Beer(models.Model):

    color_choices = (('Светлое', 'Светлое'), ('Тёмное', 'Тёмное'))

    mark = models.CharField(max_length=20, help_text='Марка пива')
    color = models.CharField(max_length=10, choices=color_choices, default='Светлое', help_text='Цвет пива')
    style = models.CharField(max_length=40, help_text='Сорт пива')
    strength = models.DecimalField(max_digits=3, decimal_places=1)
    country = models.CharField(max_length=30, help_text='Страна происхождения')
    info = models.TextField(help_text='Краткая информация')

    class Meta:
        db_table = 'beer'

    def __str__(self):
        return '{0}. {1} - {2}, {3}, {4} %'.format(self.id, self.mark, self.color, self.style, self.strength)


class Comments(models.Model):

    class Meta:

        db_table = 'comments'

    comments_name = models.CharField(max_length=40, default='Unknown user')
    comments_text = models.TextField()
    comments_article = models.ForeignKey(Beer,on_delete=models.CASCADE)


