from django.db import models


class New(models.Model):

    image = models.ImageField(
        upload_to='news/',
        verbose_name="Изображение",
        blank=True,
        null=True
    )

    title = models.CharField(
        max_length=256
    )

    description = models.CharField(
        max_length=256
    )


    class Meta:
        verbose_name = "new"
        verbose_name_plural = "news"
    
    def __str__(self) -> str:
        return self.title
    
    