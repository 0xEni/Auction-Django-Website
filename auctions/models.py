from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import URLValidator


class User(AbstractUser):
    pass


class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    starting_bid = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=32)
    image_url = models.TextField(blank=True, validators=[URLValidator()])
    creator = models.ForeignKey(User, on_delete=models.CASCADE,  related_name="user", null=True)


    def __str__(self):
        return f"{self.id}: {self.title} - {self.description}"

class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bid")
    bid = models.DecimalField(max_digits=6, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE,  related_name="%(class)s_user")

class Comment(models.Model):
    comment =  models.CharField(max_length=512)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="%(class)s_listing")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,  related_name="%(class)s_user")

class Watchlist(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="%(class)s_listing")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,  related_name="%(class)s_user")


    def save(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        if user:
            self.user = user
        super().save(*args, **kwargs)
        

