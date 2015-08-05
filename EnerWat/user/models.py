from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models


class User(AbstractUser):
    def get_absolute_url(self):
        return reverse('user_detail', args=[str(self.pk)])


class Article(models.Model):
    writer_id = models.IntegerField()
