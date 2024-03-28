from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.ratings.models import Rating


@receiver(post_save, sender=Rating)
def create_rating(sender, instance, created, **kwargs):
    if created:
        ratings = Rating.objects.filter(track=instance.track.id)
        stars = [star.rating for star in ratings]
        avg = round(sum(stars) / len(stars), 2)
        instance.track.rating = avg
        instance.track.save()
        print(avg)