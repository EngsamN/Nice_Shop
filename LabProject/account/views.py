from django.http import JsonResponse

def example_view(request):
    """
    Example view function that returns a JSON response.

    Args:
        request (HttpRequest): The request object.

    Returns:
        JsonResponse: A JSON response containing a greeting message.
    """
    data = {
        'message': 'Hello, world!'
    }
    return JsonResponse(data)