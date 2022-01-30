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
    prolst=product.objects.all()
    procount_count=prolst.count()
    brands=brand.objects.all()
    brand_count=brands.count()
    context={"name":"samiah",'prolst':prolst,'procount_count':procount_count,'brand_count':brand_count}
    return render(request,template_name,context)




def prodef(request):
    template_name='makeup/products.html'
    prolst=product.objects.all()
    procount_count=prolst.count()
  
    context={"name":"samiah",'prolst':prolst,'procount_count':procount_count}
    return render(request,template_name,context)


def detail(request):
    proditals=product.objects.all()
    context={'product':proditals}
    template_name='makeup/product_detials.html'
    return render(request,template_name,context) 

