from django.shortcuts import render


from  .models import brand ,product
# Create your views here.
def brandsview(request):
    ''' this is practic view '''
    # return HttpResponse("Hello, world. You're at the polls index.")
    template_name='makeup/brands.html'
    brands=brand.objects.all()
    context={"name":"samiah",'brands':brands}
    return render(request,template_name,context)


def dashboard(request):
   # return HttpResponse("Hello, world. You're at the polls index.")
    template_name='makeup/index.html'
    return render(request,template_name)



def prodef(request):
    template_name='makeup/products.html'
    prolst=product.objects.all()
    context={"name":"samiah",'prolst':prolst}
    return render(request,template_name,context)