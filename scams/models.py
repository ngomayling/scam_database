from django.db import models

class Scam(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    scam_type = models.CharField(max_length=100)
    date_seen = models.DateField()
    url_or_contact = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending')

    def __str__(self):
        return self.title