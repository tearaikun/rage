from django.db import models


class Contact(models.Model):

    phone_number = models.CharField(max_length=13)
    email = models.EmailField()
    instagram = models.URLField(
        blank=True, null=True
    )
    tiktok = models.URLField(
        blank=True, null=True
    )

    class Meta:
        verbose_name = "contact"
        verbose_name_plural = "contacts"
    
    def __str__(self) -> str:
        return self.title
    
    