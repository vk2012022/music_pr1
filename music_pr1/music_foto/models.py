from django.db import models

class MusicPiece(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название произведения")
    photo = models.ImageField(upload_to='photos/', verbose_name="Фото")
    audio = models.FileField(upload_to='audios/', verbose_name="Аудио файл (MP3)")
    description = models.TextField(verbose_name="Описание произведения")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    def __str__(self):
        return self.title
