from django.db import models
from django.core.validators import MaxValueValidator


class RSVP(models.Model):

    family_name = models.CharField(
    max_length=100,
    unique=True
    )
    guest_count = models.PositiveIntegerField(
    validators=[MaxValueValidator(20)]
)

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.family_name