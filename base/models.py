from django.db import models

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    interests = models.CharField(max_length=255, blank=True)
    # Add other profile-related fields (e.g., age, gender, photos, etc.)

    def __str__(self):
        return self.user.username
    

class Match(models.Model):
    user1 = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='matches_as_user1')
    user2 = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='matches_as_user2')
    matched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user1.user.username} and {self.user2.user.username}'


class Message(models.Model):
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.sender.user.username} to {self.receiver.user.username}'
    
    
class Like(models.Model):
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='sent_likes')
    receiver = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='received_likes')
    liked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender.user.username} likes {self.receiver.user.username}'

