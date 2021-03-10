from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from .base import BaseUpdateView, BaseDeleteView
from .models import Item, CollectionSet

User = get_user_model()


class CreateItemView(LoginRequiredMixin, CreateView):
    model = Item
    template_name = 'items/create_item.html'
    context_object_name = 'item'


class UpdateItemView(LoginRequiredMixin, BaseUpdateView):
    model = Item
    template_name = 'items/update_item.html'
    context_object_name = 'item'


class DeleteItemView(LoginRequiredMixin, BaseDeleteView):
    model = Item
    template_name = 'items/delete_item.html'
    context_object_name = 'item'


class ItemView(DetailView):
    model = Item
    template_name = 'items/item.html'
    context_object_name = 'item'


class CreateCollectionSetView(LoginRequiredMixin, CreateView):
    model = CollectionSet
    template_name = 'items/create_collection_set.html'
    context_object_name = 'collection_set'


class UpdateCollectionSetView(LoginRequiredMixin, BaseUpdateView):
    model = CollectionSet
    template_name = 'items/update_collection_set.html'
    context_object_name = 'collection_set'


class DeleteCollectionSetView(LoginRequiredMixin, BaseDeleteView):
    model = CollectionSet
    template_name = 'items/delete_collection_set.html'
    context_object_name = 'collection_set'


class CollectionSetView(DetailView):
    model = CollectionSet
    template_name = 'items/collection_set.html'
    context_object_name = 'collection_set'


class UserItemsView(ListView):
    template_name = 'items/user_items.html'
    context_object_name = 'items'

    def get_queryset(self):
        user_id = self.kwargs['pk']
        user = get_object_or_404(User, pk=user_id)

        return user.items.all()


class UserCollectionSetsView(ListView):
    template_name = 'items/user_collection_sets.html'
    context_object_name = 'collection_sets'

    def get_queryset(self):
        user_id = self.kwargs['pk']
        user = get_object_or_404(User, pk=user_id)

        return user.collection_sets.all()
