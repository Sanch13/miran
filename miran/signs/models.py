from django.db import models
from django.conf import settings


class Sign(models.Model):
    sign = models.CharField(max_length=5)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                             related_name="sign",
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.sign
