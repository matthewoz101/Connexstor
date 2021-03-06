from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profilePicture = models.ImageField(null=True, blank=True, upload_to='uploads/profile_pictures', default='uploads/profile_pictures/default.png')

    def __str__(self):
        return str(self.user)