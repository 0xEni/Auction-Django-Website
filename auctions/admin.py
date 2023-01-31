from django.contrib import admin

from .models import Listing, User, Bid, Comment, Watchlist

# Register your models here.
class AuctionAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description")

admin.site.register(Listing)
admin.site.register(User)
admin.site.register(Bid)
admin.site.register(Comment)
admin.site.register(Watchlist)
