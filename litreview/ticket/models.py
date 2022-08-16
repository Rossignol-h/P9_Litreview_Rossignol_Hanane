from django.conf import settings
from django.db import models
from PIL import Image


class Ticket(models.Model):

    title = models.CharField(max_length=128, verbose_name='Titre')
    description = models.TextField(
        max_length=2048, blank=True, verbose_name='Description')
    image = models.ImageField(
        default="default-cover/default.jpg", null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    has_review = models.BooleanField(default=False)

    IMAGE_MAX_SIZE = (700, 700)

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        try:
            self.resize_image()
        except ValueError:
            pass
