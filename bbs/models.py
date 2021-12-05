from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):

    class Meta:
        db_table = "topic"

    comment     = models.CharField(verbose_name="コメント",max_length=2000)
    user        = models.ForeignKey(User, verbose_name="投稿者", on_delete=models.CASCADE, null=True,blank=True)

    def __str__(self):
        return self.comment
