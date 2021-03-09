from django.contrib import admin

from .models import Tag, Item, CollectionSet

admin.site.register(Tag)
admin.site.register(Item)
admin.site.register(CollectionSet)
