from django.contrib.auth.models import User
from django.db import models


class UserProfileManager(models.Manager):
    def get_by_natural_key(self, user):
        return self.get(user=user)


class UserProfile(models.Model):

    objects = UserProfileManager()

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="models_profile")

    def __str__(self):
        return "%s" % (self.user)

    class Meta:
        unique_together = (('user',),)

    def natural_key(self):
        return (self.user,)
