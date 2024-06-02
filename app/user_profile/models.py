from django.db import models
from account.models import User
import uuid
# Create your models here.
class Profile(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_online = models.BooleanField(default=False)
    friends = models.ManyToManyField("self", related_name='my_friends', blank=True,symmetrical=False)
    
    
    @property
    def friends_count(self):
        return self.friends.all().count()


    def __str__(self):
        return f'{self.user.name} Profile'







class FriendRequests(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='friend_sender')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='friend_receiver')
    STATUS_CHOICES = (
    ('send','send'),
    ('accepted','accepted'),
    ('rejected','rejected')
    )

    status = models.CharField(max_length=8, choices=STATUS_CHOICES,default=STATUS_CHOICES[0][0])
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"