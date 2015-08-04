from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Article(models.Model):
    writer_id = models.IntegerField()
