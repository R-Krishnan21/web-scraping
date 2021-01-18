from django.db import models

# Create your models here.
class Questions(models.Model):
    question = models.CharField(max_length=200)
    detail = models.TextField()
    votes = models.IntegerField(default=0)
    link = models.URLField(max_length=200)
    views = models.IntegerField(default=0)
    tags = models.CharField(max_length=200)

    def __str__(self):
        return self.question
