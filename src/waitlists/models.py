from django.db import models

class WailistEntry(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)
