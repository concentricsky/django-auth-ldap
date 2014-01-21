from django.db import models
from django.conf import settings


class TestProfile(models.Model):
    """
    A user profile model for use by unit tests. This has nothing to do with the
    authentication backend itself.
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    is_special = models.BooleanField(default=False)
    populated = models.BooleanField(default=False)
