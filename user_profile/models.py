from django.db import models

class UserProfile(models.Model):
    user_id = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    bio = models.CharField(max_length=500, blank=True)
    emoji = models.CharField(max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nickname
