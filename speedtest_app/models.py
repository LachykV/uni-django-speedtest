# speedtest_app/models.py
from django.db import models
from django.utils import timezone

class SpeedTestResult(models.Model):
    download_speed = models.FloatField()
    upload_speed = models.FloatField()
    ping = models.FloatField()
    timestamp = models.DateTimeField(default=timezone.now)
    server_location = models.CharField(max_length=255, blank=True)  # Add this field
    server_name = models.CharField(max_length=255, blank=True)      # Add this field
    server_country = models.CharField(max_length=100, blank=True)   # Add this field

    class Meta:
        ordering = ['-timestamp']