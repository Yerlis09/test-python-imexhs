from django.db import models

class MedicalImageResult(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    device_name = models.CharField(max_length=255)
    mean_before_normalization = models.FloatField()
    mean_after_normalization = models.FloatField()
    data_size = models.IntegerField()
    raw_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.device_name} - {self.id}"
