from django.db import models
from user_profile.models import UserProfile


class GuestBookMessage(models.Model):
    writer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='messages_written')
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='messages_received')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('writer', 'owner')

    def __str__(self):
        return f'{self.writer.nickname} -> {self.owner.nickname}'