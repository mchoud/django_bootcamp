
from django.contrib import admin
from django.urls import path, re_path

from products import views

urlpatterns = [
    path('search/', views.home_view),
    path('products/<int:id>/', views.product_detail_view),
    #path('products/1/', views.product_detail_view),
    # path('api/products/1/', views.product_api_detail_view),
    re_path(r'api/products/(?P<id>\d+)/', views.product_api_detail_view),
    path('admin/', admin.site.urls),
]
