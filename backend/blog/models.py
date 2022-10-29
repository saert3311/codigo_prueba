from django.db import models

class Client(models.Model):
    post_text = models.CharField(max_length=150, verbose_name='Post Text')
    post_type = models.CharField(max_length=150, verbose_name='Post Type')
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.post_text}'

    class Meta:
        ordering = ['-created', ]
