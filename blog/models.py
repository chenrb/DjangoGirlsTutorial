from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    title = models.CharField('标题', max_length=200)
    text = models.TextField('正文')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def puhlish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
