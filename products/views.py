from django.http import HttpResponse, JsonResponse
from django.http.response import Http404
from django.shortcuts import render

from products.models import Product
# Create your views here.
def home_view(request, *args, **kwargs):

    return HttpResponse("<h1>Hello ggworld <h1>")

def product_detail_view(request, id):
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
        
    return HttpResponse(f"Product id {obj.id}")

# def product_detail_view(request, *args, **kwargs):
#     obj = Product.objects.get(id=1)
#     return HttpResponse(f"Product id {obj.id}")


def product_api_detail_view(request, *args, **kwargs):
    obj = Product.objects.get(id=1)
    return JsonResponse({"id": obj.id})

# class HomeView():
#     pass merdeka atau mati