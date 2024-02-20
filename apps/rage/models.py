from django.db import models


class Rage(models.Model):

    image = models.ImageField(upload_to="rage/")

    name = models.CharField(max_length=560)

    job = models.CharField(
        max_length = 256
    )

    class Meta:
        verbose_name = "rage"
        verbose_name_plural = "rage_team"
    
    def __str__(self) -> str:
        return self.title
    
    