from django.db import models

class todos(models.Model):
  items = models.CharField(max_length=255)
  created_at = models.DateField(auto_now=True)
