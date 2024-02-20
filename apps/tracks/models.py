from django.db import models


class Track(models.Model):

    title = models.CharField(
        max_length=256
    )

    image = models.ImageField(
        upload_to='track/',
        verbose_name="Изображение",
        blank=True,
        null=True
    )

    date = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = "track"
        verbose_name_plural = "tracks"
    
    def __str__(self) -> str:
        return self.title
    
    