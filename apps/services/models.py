from django.db import models


class Service(models.Model):

    title = models.CharField(
        max_length=256
    )

    description = models.CharField(
        max_length=256
    )


    class Meta:
        verbose_name = "service"
        verbose_name_plural = "services"
    
    def __str__(self) -> str:
        return self.title
    
    