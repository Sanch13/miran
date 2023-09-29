from django.db import models


class Book(models.Model):
    class Status(models.TextChoices):
        OPEN = "OPEN", "Open"
        CLOSE = "CLOSE", "Close"

    author = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=1000)
    qr_code = models.ImageField(upload_to=f"books/{author}_{title}/",
                                blank=True,
                                null=True)
    status = models.CharField(max_length=5,
                              choices=Status.choices,
                              default=Status.OPEN)
