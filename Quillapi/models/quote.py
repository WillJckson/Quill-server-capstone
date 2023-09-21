from django.db import models
from .quote_category import QuoteCategory
from .quill_user import QuillUser
class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=255)
    quill_user = models.ForeignKey(QuillUser, on_delete=models.CASCADE)
    quote_category = models.ForeignKey(QuoteCategory, on_delete=models.CASCADE)
