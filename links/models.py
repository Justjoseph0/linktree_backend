from django.db import models
from users.models import UserProfile


# Create your models here.

class Link(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="links")
    title = models.CharField(max_length=100)
    url = models.URLField()
    logo_url = models.URLField(blank=True, null=True)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title