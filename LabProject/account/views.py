# account/views.py

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

def home(request):
    """
    View function for the home page of the site.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response containing the rendered template.
    """
    return HttpResponse("Welcome to the Home Page")

class HomeView(View):
    """
    Class-based view for the home page.

    Methods:
        get: Handles GET requests.
    """

    def get(self, request):
        """
        Handles GET requests.

        Args:
            request (HttpRequest): The request object.

        Returns:
            HttpResponse: The response containing the rendered template.
        """
        return HttpResponse("Welcome to the Home Page")
