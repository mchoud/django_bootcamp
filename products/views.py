from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render

from products.models import Product
# Create your views here.
def home_view(request, *args, **kwargs):
    
    context ={"name": "Justin"}
#    return HttpResponse("<h1>Hello ggworld <h1>")
    return render(request, "home.html", context)

def product_detail_view(request, id):
    # try:
    #     obj = Product.objects.get(id=id)
    # except Product.DoesNotExist:
    #     raise Http404

    try:
        obj = Product.objects.get(id=id)
    except:
        raise Http404

    #return HttpResponse(f"Product id {obj.id}")
    return render(request, "products/detail.html", {"object":obj})

# def product_detail_view(request, *args, **kwargs):
#     obj = Product.objects.get(id=1)
#     return HttpResponse(f"Product id {obj.id}")


# def product_api_detail_view(request, *args, **kwargs):
#     obj = Product.objects.get(id=1)
#     return JsonResponse({"id": obj.id})


def product_api_detail_view(request, id,*args, **kwargs):
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return JsonResponse({"message": "Not found"})
    return JsonResponse({"id": obj.id})

# class HomeView():
#     pass merdeka atau mati