from django.db import models

# Create your models here.
# from practice.forms import MessageForm


class Message(models.Model):
    name = models.CharField(
        max_length=100
    )

    title = models.CharField(
        max_length=100, blank=True
    )
    content = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )
