"""Views."""

from django.shortcuts import render


def home_view(request):
    """."""
    return render(request, 'ca_website/base.html', {})
