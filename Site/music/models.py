from django.db import models
from django.conf import settings
from django.core import validators
import os


class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    full_text = models.TextField('Описание')
    date = models.DateTimeField('Дата добавления')
    audio = models.FileField('Введите файл расширения .mp3', upload_to='media/', validators=[validators.FileExtensionValidator(['mp3'], message="Файл должен быть расширения .mp3")])

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.audio.name))
        super(Articles, self).delete(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/music/{self.id}'

    class Meta:
        verbose_name = 'Трек'
        verbose_name_plural = 'Треки'