from django.conf import settings
from django.db import models


class UserFollows(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following')

    followed_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followed_by')

    class Meta:
        # unique_together will soon be deprecated according to the documentation
        constraints = [models.UniqueConstraint(fields=['user', 'followed_user'], name="unique_follow")]

    def __str__(self) -> str:
        return f"{self.user} - {self.followed_user}"
