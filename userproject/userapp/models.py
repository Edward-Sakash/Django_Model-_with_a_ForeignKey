from django.db import models
from django.contrib.auth import get_user_model

class Profile(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    bio = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username
    