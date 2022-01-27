from django.shortcuts import render

# Create your views here.
def brand(request):
    ''' this is practic view '''
    # return HttpResponse("Hello, world. You're at the polls index.")
    template_name='makeup/index.html'
    return render(request,template_name)