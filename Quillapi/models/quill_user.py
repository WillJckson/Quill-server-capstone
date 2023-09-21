
from django.db import models
from django.contrib.auth.models import User

class QuillUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=100)
    
    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'
    @property
    def username(self):
        return f'{self.user.username}'