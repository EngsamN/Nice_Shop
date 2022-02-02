from django.shortcuts import render
from django.shortcuts import (get_object_or_404,
							render,
							HttpResponseRedirect)

from django.views.generic.edit import FormView 
from django.views.generic import  DetailView

from makeup import admin
from .form  import EditproForm
from  .models import brand ,product
# Create your views here.
def brandsview(request):
    ''' this is practic view '''
    # return HttpResponse("Hello, world. You're at the polls index.")
    template_name='makeup/brands.html'
    brands=brand.objects.all()
    context={"name":"samiah",'brands':brands}
    return render(request,template_name,context)

#show all number of products and brands view
def dashboard(request):
   # return HttpResponse("Hello, world. You're at the polls index.")
    template_name='makeup/index.html'
    prolst=product.objects.all()
    procount_count=prolst.count()
    brands=brand.objects.all()
    brand_count=brands.count()
    context={"name":"samiah",'prolst':prolst,'procount_count':procount_count,'brand_count':brand_count}
    return render(request,template_name,context)

def adminfun(request):
    return render(request,admin.site)
#show all products view
def prodef(request):
    template_name='makeup/product.html'
    prolst=product.objects.all()
    procount_count=prolst.count()
  
    context={"name":"samiah",'prolst':prolst,'procount_count':procount_count}
    return render(request,template_name,context)

#show pro detials view
def detail(request,id): 
    """
    this is post detail page show product model
    """
    context = {}
    try:
       proditals = product.objects.get(id=id)
       context['proditals'] = proditals
    except product.DoesNotExist:
        context['error'] = "Not found"
    
    template_name='makeup/product_detials.html'

    return render(request, template_name, context)
#show brand  detials view
def brandetail(request,id): 
    """
    this is post detail page show brands model
    """
    context = {}
    try:
       branditals = brand.objects.get(id=id)
       context['branditals'] = branditals
    except product.DoesNotExist:
        context['error'] = "Not found"
    
    template_name='makeup/brands_detials.html'

    return render(request, template_name, context)

#creat view to edit
def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
    # add the dictionary during initialization
    form = EditproForm(request.POST or None)
    if form.is_valid():
        form.save()     
    context['form']= form
    return render(request, "makeup/editpro_form.html", context)


class EmpImageDisplay(DetailView):
    model = product
    prolst=product.objects.all()
    template_name = 'products.html'
    context_object_name = 'prolst'

# # after updating it will redirect to detail_View
# def detail_view(request, id):
# 	# dictionary for initial data with
# 	# field names as keys
# 	context ={}

# 	# add the dictionary during initialization
# 	context["data"] = EditproForm.objects.get(id = id)
		
# 	return render(request, "editpro_form.html", context)

# # update view for details
# def update_view(request, id):
# 	# dictionary for initial data with
# 	# field names as keys
# 	context ={}

# 	# fetch the object related to passed id
# 	obj = get_object_or_404(product, id = id)

# 	# pass the object as instance in form
# 	form = EditproForm(request.POST or None, instance = obj)

# 	# save the data from the form and
# 	# redirect to detail_view
# 	if form.is_valid():
# 		form.save()
# 		return HttpResponseRedirect("/"+id)

# 	# add form dictionary to context
# 	context["form"] = form

# 	return render(request, "editpro_form.html", context)

