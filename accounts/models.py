from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ("exporter", "Exporter"),
        ("importer", "Importer"),
        ("partner", "Partner"),
        ("admin", "Admin"),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="exporter")
    phone = models.CharField(max_length=30, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    gst_number = models.CharField(max_length=64, blank=True, null=True)  # optional

    def __str__(self):
        return f"{self.username} ({self.role})"
