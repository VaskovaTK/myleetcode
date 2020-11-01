from django.db import models

class Task (models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=120)
    post = models.TextField()
    date = models.DateTimeField()
    # solution = здесь нужно поле для приема данных и нужна кнопка на которую нажмут чтобы отправить данные еще нужна кнопка чтобы посмотреть мое решение
    def __str__(self):
        return self.title
# Create your models here.
