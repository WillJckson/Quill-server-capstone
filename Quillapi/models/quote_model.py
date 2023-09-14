from django.db import models
from django.contrib.auth.models import User
from .category_model import Category

class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, through='QuoteCategory')