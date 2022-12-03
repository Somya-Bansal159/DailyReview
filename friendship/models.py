from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Friendship(models.Model):
    from_user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, blank=False, related_name="fs_from"
    )
    to_user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, blank=False, related_name="fs_to"
    )

    class Meta:
        unique_together = ("from_user", "to_user")


class FriendshipRequests(models.Model):
    from_user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, blank=False, related_name="fr_from"
    )
    to_user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, blank=False, related_name="fr_to"
    )

    class Meta:
        unique_together = ("from_user", "to_user")