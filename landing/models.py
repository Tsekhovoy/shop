from django.db import models

class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)

    def __str__(self):
        try:
            return 'Пользователь: %s email: %s' % (self.name, self.email)
        except:
            return '%s' % self.name.id

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'