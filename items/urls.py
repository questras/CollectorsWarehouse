from django.urls import path

from .views import (
    ItemView,
    CreateItemView,
    UpdateItemView,
    DeleteItemView,
    CollectionSetView,
    CreateCollectionSetView,
    UpdateCollectionSetView,
    DeleteCollectionSetView,
    UserItemsView,
    UserCollectionSetsView
)

urlpatterns = [
    path('items/create/', CreateItemView.as_view(), name='create-item'),
    path('items/<int:pk>/', ItemView.as_view(), name='item'),
    path('items/<int:pk>/update/', UpdateItemView.as_view(), name='update-item'),
    path('items<int:pk>/delete/', DeleteItemView.as_view(), name='delete-item'),

    path('sets/create/', CreateCollectionSetView.as_view(), name='create-collection-set'),
    path('sets/<int:pk>/', CollectionSetView.as_view(), name='collection-set'),
    path('sets/<int:pk>/update/', UpdateCollectionSetView.as_view(), name='update-collection-set'),
    path('sets/<int:pk>/delete/', DeleteCollectionSetView.as_view(), name='delete-collection-set'),

    path('users/<int:pk>/items/', UserItemsView.as_view(), name='user-items'),
    path('users/<int:pk>/sets/', UserCollectionSetsView.as_view(), name='user-collection-sets'),
]
