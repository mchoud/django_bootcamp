
from django.contrib import admin
from django.urls import path

from products import views

urlpatterns = [
    path('search/', views.home_view),
    path('products/1/', views.product_detail_view),
    path('admin/', admin.site.urls),
]
