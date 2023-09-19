from django.db import models

class QuoteCategory(models.Model):
    category = models.CharField(max_length=200)