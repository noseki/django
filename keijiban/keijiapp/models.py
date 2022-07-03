from django.db import models

class ThreadModel(models.Model):
    title = models.CharField(max_length=15)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title