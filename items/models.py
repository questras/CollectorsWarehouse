from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


class Tag(models.Model):
    """Tag of an item. E.g book, game, etc."""
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Item(models.Model):
    """Item, that will be added to users' collections."""
    name = models.CharField(max_length=512)
    description = models.CharField(max_length=1024, null=True, blank=True)
    collected_at = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE,
                              related_name='items')
    tags = models.ManyToManyField(to=Tag, related_name='items', blank=True)

    def __str__(self):
        return f'{self.name} in collection owned by {self.owner}'


class CollectionSet(models.Model):
    """Subset of user's items."""
    name = models.CharField(max_length=512)
    description = models.CharField(max_length=1024, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE,
                              related_name='collection_sets')
    items = models.ManyToManyField(to=Item, related_name='collection_sets', blank=True)

    def add_item(self, item: Item):
        """Add item to collection set, checking whether the item belongs
        to collection set owner - if not, raise ValidationError."""

        if item.owner != self.owner:
            raise ValidationError(
                message='Collection Set owner and item owner are not the same user.'
            )

        self.items.add(item)

    def __str__(self):
        return f'{self.name} collection set owned by {self.owner}'
