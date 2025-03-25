from django.db import models
from config.settings import AUTH_USER_MODEL


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название курса', help_text='Укажите название курса')
    preview = models.ImageField(upload_to="users/avatars", blank=True, null=True, verbose_name="Превью",
                                help_text='Загрузите превью')
    description = models.TextField(blank=True, null=True, verbose_name='Описание курса',
                                   help_text='Укажите описание курса')
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Владелец курса", blank=True,
                              null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название урока', help_text='Укажите название урока')
    description = models.TextField(blank=True, null=True, verbose_name='Описание урока',
                                   help_text='Укажите описание урока')
    preview = models.ImageField(upload_to="users/avatars", blank=True, null=True, verbose_name="Превью",
                                help_text='Загрузите превью')

    video_link = models.URLField(blank=True, null=True, verbose_name='Ссылка на видео',
                                 help_text='Укажите ссылку на видео')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons', null=True)
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Владелец урока", blank=True,
                              null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
