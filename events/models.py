from django.db import models

from SoftUDjangoProject.accounts.models import Profile


class Event(models.Model):
    name = models.CharField(
        max_length=150
        )

    date = models.DateField(

    )

    location = models.CharField(

    )

    description = models.TextField(
        max_length=300
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    created_by = models.CharField(
        max_length=150,
        null=True,
        blank=True
    )


    def __str__(self):
        return self.name



class Comment(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='comments',
    )

    author = models.CharField(
        max_length=100,
    )

    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )