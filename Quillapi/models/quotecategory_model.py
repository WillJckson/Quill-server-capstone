from django.db import models
from .quote_model import Quote
from .category_model import Category

class QuoteCategory(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)