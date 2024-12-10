from django.db import models


class EventChoices(models.TextChoices):
    LOCAL = "Local", "Local"
    NATIONAL = "National", "National"