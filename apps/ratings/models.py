from django.db import models

from apps.users.models import User
from apps.tracks.models import Track


class Rating(models.Model):
    class RatingIntegerChoice(models.IntegerChoices):
        ONE = 1,
        TWO = 2,
        THREE = 3,
        FOUR = 4,
        FIVE = 5,

    rating = models.IntegerField(choices=RatingIntegerChoice.choices, default=RatingIntegerChoice.ONE)

    feedback = models.TextField(max_length=560, null=True)
    
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="author_rating"
    )
    track = models.ForeignKey(
        Track,
        on_delete=models.CASCADE,
        related_name="track_rating"
    )


    class Meta:
        verbose_name = "rating"
        verbose_name_plural = "ratings"
    
    def __str__(self) -> str:
        return self.title
    
    