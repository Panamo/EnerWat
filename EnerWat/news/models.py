from django.db import models


# Create your models here.
class News(models.Model):
    subject = models.CharField(max_length=255)
    date = models.DateField()
    keyword = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.subject
