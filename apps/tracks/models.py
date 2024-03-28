from django.db import models

    
class Track(models.Model):

    title = models.CharField(
        max_length=256
    )
    artist = models.CharField(
        max_length=256
    )
    image = models.ImageField(
        upload_to='track/',
        verbose_name="Изображение",
        blank=True,
        null=True
    )
    music = models.FileField(
        upload_to="musics",
        verbose_name="Музыка"
    )
    date = models.DateTimeField(
        auto_now_add=True
    )
    
    rating = models.FloatField(
        default=0, blank=True, null=True
    ) 

    class Meta:
        verbose_name = "track"
        verbose_name_plural = "tracks"
    
    def __str__(self) -> str:
        return self.title
    
    