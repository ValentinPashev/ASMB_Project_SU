from django.db import models


class CampaginChoices(models.TextChoices):
    LOCAL = "Local", "Local"
    NATIONAL = "National", "National"