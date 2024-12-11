from django.db import models
from accounts.models import Profile


class ActivityLog(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="activity_logs")
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
