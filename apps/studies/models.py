from django.db import models


class Studies(models.Model):

    title = models.CharField(
        max_length=256
    )

    link = models.URLField()

    class Meta:
        verbose_name = "study_video"
        verbose_name_plural = "study_videos"
        # ordering = "-id"
    
    def __str__(self) -> str:
        return self.title
    
    