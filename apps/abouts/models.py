from django.db import models


class About(models.Model):

    title = models.CharField(
        max_length=256
    )

    image = models.ImageField(
        upload_to='about/',
        verbose_name="Изображение",
        blank=True,
        null=True
    )

    description = models.CharField(
        max_length=640
    )


    class Meta:
        verbose_name = "about"
        verbose_name_plural = "abouts"

    
    def __str__(self) -> str:
        return self.title
    
    