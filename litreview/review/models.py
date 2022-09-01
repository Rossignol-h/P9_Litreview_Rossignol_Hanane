from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from django.db import models
from ticket.models import Ticket


class Review(models.Model):
    """ Model for managing a review """

    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)], verbose_name='Note')
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    headline = models.CharField(
        max_length=128, unique=True, verbose_name='Titre')
    body = models.TextField(max_length=8192, blank=True,
                            verbose_name='Commentaires')
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.headline

    def __str__(self):
        return f"{self.ticket.title} - {self.headline}"
