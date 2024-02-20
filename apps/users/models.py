from django.db import models

class User(models.Model):
    
    fullname = models.CharField(
        max_length=256
    )
    age = models.PositiveSmallIntegerField()

    job = models.CharField(
        max_length=256
    )

    phone_number = models.CharField(
        max_length=13
    )

    email = models.EmailField()


    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
    
    def __str__(self) -> str:
        return self.fullname
    