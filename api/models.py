from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.charField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title
