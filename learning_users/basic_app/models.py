from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfileInfo(models.Model):
    # Extending attributes to default admin user class
    user = models.OneToOneField(User, on_delete=models.deletion.CASCADE)

    # Adding attributes
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(blank=True, upload_to='profile_pics')

    def __str__(self):
        return self.user.username
