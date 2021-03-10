"""Base class-based view classes to inherit from."""

from django.http import Http404
from django.views.generic import UpdateView, DeleteView


class BaseUpdateView(UpdateView):
    def get_object(self, queryset=None):
        obj = super().get_object()

        if self.request.user != obj.owner:
            raise Http404()

        return obj


class BaseDeleteView(DeleteView):
    def get_object(self, queryset=None):
        obj = super().get_object()

        if self.request.user != obj.owner:
            raise Http404()

        return obj
