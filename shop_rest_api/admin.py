from django.contrib import admin

from shop_rest_api.models import Item, Review


class ItemAdmin(admin.ModelAdmin):
    search_fields = ['name']


class ReviewAdmin(admin.ModelAdmin):
    list_filter = ['approved']


admin.site.register(Item, ItemAdmin)
admin.site.register(Review, ReviewAdmin)
