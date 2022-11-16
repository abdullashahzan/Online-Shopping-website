from django.contrib import admin

from auctions.models import auction, bid, comment, watchlist

# Register your models here.
admin.site.register(auction)
admin.site.register(watchlist)
admin.site.register(comment)
admin.site.register(bid)
