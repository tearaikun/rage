from django.db import models


class Rating(models.Model):

    rating = models.IntegerField(null=True)

    feedback = models.TextField(max_length=560, null=True)
    
    author = models.CharField(
        max_length = 256
    )


    class Meta:
        verbose_name = "rating"
        verbose_name_plural = "ratings"
    
    def __str__(self) -> str:
        return self.title
    
    