from slugify import slugify

from django.db import models
from django.urls import reverse

from .utils import generate_qr_code
from django.conf import settings


class Book(models.Model):
    class Status(models.TextChoices):
        OPEN = "OPEN", "Open"
        CLOSE = "CLOSE", "Close"

    author = models.CharField(max_length=250,
                              verbose_name="Автор")
    title = models.CharField(max_length=250,
                             verbose_name="Название книги")
    description = models.TextField(max_length=1000,
                                   blank=True,
                                   verbose_name="Краткое описание книги")
    qr_code = models.ImageField(blank=True,
                                null=True)
    slug = models.SlugField(max_length=250,
                            unique=True,
                            blank=True)
    status = models.CharField(max_length=5,
                              choices=Status.choices,
                              default=Status.OPEN,
                              verbose_name="Статус книги")
    reader = models.CharField(max_length=100,
                              blank=True,
                              default='')
    year = models.PositiveSmallIntegerField(default=0,
                                            verbose_name="Дата издания")

    class Meta:
        verbose_name = "Книги"
        verbose_name_plural = "Книги"

    def __str__(self):
        return f"{self.author} {self.title}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.author}-{self.title}")
        book_url = self.get_absolute_url()
        if not self.qr_code:
            self.qr_code = generate_qr_code(instance=self, book_url=book_url)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(viewname="books:detail", args=[self.slug])


class History(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                             related_name="user",
                             on_delete=models.CASCADE)
    book = models.ForeignKey(to=Book,
                             on_delete=models.CASCADE)
    date_start = models.DateTimeField(auto_created=True,
                                      blank=True,
                                      null=True)
    date_end = models.DateTimeField(auto_created=True,
                                    blank=True,
                                    null=True)

    def __str__(self):
        return f"{self.user}"
