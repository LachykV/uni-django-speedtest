from django.db import models
from django.utils import timezone

class SpeedTestResult(models.Model):
    download_speed = models.FloatField()
    upload_speed = models.FloatField()
    ping = models.FloatField()
    timestamp = models.DateTimeField(default=timezone.now)  # Use timezone.now instead of auto_now_add

    class Meta:
        ordering = ['-timestamp']